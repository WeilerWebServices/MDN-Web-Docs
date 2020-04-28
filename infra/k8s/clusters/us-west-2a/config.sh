#!/bin/bash

source ../common.sh

export KOPS_REGION="us-west-2"
export CLUSTER_ALT_NAME="oregon"
export KOPS_SHORTNAME="k8s.${KOPS_REGION}a"
export KOPS_CLUSTER="k8s.${KOPS_REGION}a.${KOPS_DOMAIN}"
export KOPS_CLUSTER_NAME="${KOPS_CLUSTER}"

export KOPS_MASTER_ZONE="us-west-2a"
export KOPS_MASTER_COUNT=1
export KOPS_ZONE="us-west-2a"
export KOPS_NODE_COUNT="10"

# This is the path of of your services manifests
export KOPS_INSTALLER="../../install"

# secrets path
export SECRETS_PATH="${HOME}/scm/mdn-k8s-private"
export TF_SECRETS_PATH="${SECRETS_PATH}/terraform/k8s"
