#!/bin/bash

set -u

if [ ! -f ./config.sh ]; then
    echo "config.sh not found"
    exit 1
fi

source ./config.sh

die() {
    echo "$*" 1>&2
    exit 1
}

validate_cluster() {
    echo "Validating cluster ${KOPS_CLUSTER_NAME}"
    kops validate cluster
    RV=$?

    return "${RV}"
}

set_tf_resource_name() {
    export TF_RESOURCE_NAME=$(echo ${KOPS_CLUSTER_NAME} | tr "." "-")
}

generate_cluster_autoscaler_tf() {
    set_tf_resource_name
    # we can now specify the exact ASG instead of "*" for the autoscaler policy
    # https://github.com/kubernetes/autoscaler/pull/527
    # https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources
    cat <<BASHEOF > ./out/terraform/cluster_autoscaler.tf
# This file is generated via post-install.sh
resource "aws_iam_policy" "nodes-${TF_RESOURCE_NAME}-autoscaler-policy" {
    name        = "nodes-${TF_RESOURCE_NAME}-autoscaler-policy"
    path        = "/"
    description = "Policy for K8s AWS autoscaler"

    policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "autoscaling:SetDesiredCapacity",
                "autoscaling:TerminateInstanceInAutoScalingGroup"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "autoscaler-attach" {
    role       = "\${aws_iam_role.nodes-${TF_RESOURCE_NAME}.name}"
    policy_arn = "\${aws_iam_policy.nodes-${TF_RESOURCE_NAME}-autoscaler-policy.arn}"
}
BASHEOF

    DEFAULT_MAX=$(echo "$((4 * ${KOPS_NODE_COUNT}))")
    # set ASG max size so to allow the cluster autoscaler to scale up
    # retains whitespace for easier reading :-)
    echo "Editing kubernetes.tf to increase max_size"
    sed -ri "s/max_size(\s*)=(\s*)$KOPS_NODE_COUNT/max_size\\1=\2$DEFAULT_MAX/" ./out/terraform/kubernetes.tf
}

install_newrelic() {
    echo "Installing New Relic"
    kubectl create -f "${KOPS_INSTALLER}/services/newrelic/newrelic-namespace.yaml"
    ( cd ${KOPS_INSTALLER}/services/newrelic && make CLUSTER_NAME=${KOPS_SHORTNAME} )
}

install_calico_rbac() {
    if [ ${KOPS_NETWORKING} != "calico" ]; then
        echo "Networking not using calico, not doing anything"
        continue
    else
        kubectl apply -f "https://docs.projectcalico.org/${CALICO_VERSION:-v3.2}/getting-started/kubernetes/installation/rbac.yaml"
    fi
}

install_fluentd() {

    PAPERTRAIL_CONFIG="${SECRETS_PATH}/k8s/secrets/${CLUSTER_ALT_NAME}/papertrail.sh"
    if [ ! -f "${PAPERTRAIL_CONFIG}" ]; then
        echo "Can't find papertrail.sh"
        exit 1
    fi

    source "${PAPERTRAIL_CONFIG}"
    echo "Installing fluentd"
    (cd ${KOPS_INSTALLER}/services/fluentd && make FLUENTD_SYSLOG_HOST=${SYSLOG_HOST} FLUENTD_SYSLOG_PORT=${SYSLOG_PORT})
}

install_redirector_service() {
    (cd ${KOPS_INSTALLER}/services/http_to_https_redirector && make deploy)
}

install_cluster_autoscaler() {
    MAX_NODES=20

    echo "Installing cluster autoscaler"
    # https://github.com/kubernetes/dashboard/issues/2326#issuecomment-326651713
    kubectl create clusterrolebinding \
        --user system:serviceaccount:kube-system:default \
        kube-system-cluster-admin --clusterrole cluster-admin
    (cd ${KOPS_INSTALLER}/services/cluster-autoscaler && make MAX_NODES=${MAX_NODES} KOPS_CLUSTER_NAME=${KOPS_CLUSTER_NAME} AWS_REGION=${KOPS_REGION})
}

install_datadog() {
    echo "Installing datadog"
    kubectl apply -f "${KOPS_INSTALLER}/services/datadog/datadog-namespace.yaml"
    kubectl apply -f "${SECRETS_PATH}/k8s/secrets/${CLUSTER_ALT_NAME}/datadog-cluster.yaml"
    kubectl apply -f "${KOPS_INSTALLER}/services/datadog/datadog-agent.yaml"
    kubectl apply -f "${KOPS_INSTALLER}/services/datadog/datadog_statsd_svc.yaml"
}

install_block-aws() {
    echo "Install block-aws"
    kubectl apply -f "${KOPS_INSTALLER}/services/block-aws/block-aws-namespace.yaml"
    kubectl apply -f "${SECRETS_PATH}/k8s/secrets/${CLUSTER_ALT_NAME}/block-aws-secrets.yaml"
    kubectl apply -f "${KOPS_INSTALLER}/services/block-aws/block-aws-cron.yaml"
    kubectl apply -f "${KOPS_INSTALLER}/services/block-aws/block-aws-networkpolicy.yaml"
}

install_metrics-server() {
    echo "Install metrics-server"
    kubectl apply -f "${KOPS_INSTALLER}/services/metrics-server/"
}

install_ark() {
    echo "Install ark"
    kubectl apply -f "${KOPS_INSTALLER}/ark/ark-prereqs.yaml"
    kubectl -n heptio-ark create secret generic cloud-credentials \
        --from-file cloud="${SECRETS_PATH}/k8s/secret/${CLUSTER_ALT_NAME}/credentials-ark"

    export AWS_REGION=${KOPS_REGION}
    export ARK_BUCKET=$(terraform output ark_bucket)
    (cd "${KOPS_INSTALLER}/ark" && make deploy)

    kubectl apply -f "${KOPS_INSTALLER}/ark/ark-deployment.yaml"

}

install_services() {
    install_cluster_autoscaler
    install_calico_rbac
    install_fluentd
    install_datadog
    install_redirector_service
    install_block-aws
    install_ark
}
