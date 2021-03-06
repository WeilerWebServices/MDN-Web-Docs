# Define defaults for environment variables that personalize the commands.
export TARGET_ENVIRONMENT ?= dev
export K8S_NAMESPACE ?= mdn-${TARGET_ENVIRONMENT}
export AWS_RESOURCE_STACK=MDN-${TARGET_ENVIRONMENT}
export AWS_REGION ?= us-west-2
export KUBECTL ?= kubectl

# Note PVs are available within ALL namespaces, so delimit them with
# the name of the target environment.
export SHARED_PV_NAME ?= mdn-shared-${TARGET_ENVIRONMENT}
export SHARED_PV_SIZE ?= 1000Gi
export SHARED_PV_RECLAIM_POLICY ?= Retain
export SHARED_PV_MOUNT_PATH ?= /
export SHARED_PV_STORAGE_CLASS_NAME ?= efs

export SHARED_PVC_NAME ?= mdn-shared
export SHARED_PVC_SIZE ?= 40Gi

export WEB_SERVICE_NAME ?= web
export WEB_SERVICE_TYPE ?= LoadBalancer
export WEB_SERVICE_PORT ?= 443
export WEB_SERVICE_TARGET_PORT ?= 8000
export WEB_SERVICE_PROTOCOL ?= TCP

export API_SERVICE_NAME ?= api
export API_SERVICE_TYPE ?= ClusterIP
export API_SERVICE_PORT ?= 80
export API_SERVICE_TARGET_PORT ?= 8000
export API_SERVICE_PROTOCOL ?= TCP

export KUMASCRIPT_SERVICE_NAME ?= kumascript
export KUMASCRIPT_SERVICE_TYPE ?= ClusterIP
export KUMASCRIPT_SERVICE_PORT ?= 9080
export KUMASCRIPT_SERVICE_TARGET_PORT ?= 9080
export KUMASCRIPT_SERVICE_PROTOCOL ?= TCP

export SSR_SERVICE_NAME ?= ssr
export SSR_SERVICE_TYPE ?= ClusterIP
export SSR_SERVICE_PORT ?= 80
export SSR_SERVICE_TARGET_PORT ?= 8000
export SSR_SERVICE_PROTOCOL ?= TCP

export WEB_NAME ?= web
export WEB_REPLICAS ?= 1
export WEB_GUNICORN_WORKERS ?= 4
export WEB_GUNICORN_TIMEOUT ?= 118
export WEB_GUNICORN_WORKER_MAX_REQUESTS ?= 1000
export WEB_GUNICORN_WORKER_MAX_REQUESTS_JITTER ?= 200
export WEB_CPU_LIMIT ?= 2
export WEB_CPU_REQUEST ?= 100m
export WEB_MEMORY_LIMIT ?= 4Gi
export WEB_MEMORY_REQUEST ?= 256Mi
export WEB_ALLOWED_HOSTS ?= "*"
export WEB_RATELIMIT_ENABLE ?= True

export API_NAME ?= api
export API_REPLICAS ?= 1
export API_GUNICORN_WORKERS ?= 4
export API_GUNICORN_TIMEOUT ?= 120
export API_GUNICORN_WORKER_MAX_REQUESTS ?= 500
export API_GUNICORN_WORKER_MAX_REQUESTS_JITTER ?= 100
export API_CPU_LIMIT ?= 2
export API_CPU_REQUEST ?= 100m
export API_MEMORY_LIMIT ?= 4Gi
export API_MEMORY_REQUEST ?= 256Mi
export API_ALLOWED_HOSTS ?= ${API_SERVICE_NAME}

export SSR_NAME ?= ssr
export SSR_REPLICAS ?= 1
export SSR_CPU_LIMIT ?= 1
export SSR_CPU_REQUEST ?= 100m
export SSR_MEMORY_LIMIT ?= 2Gi
export SSR_MEMORY_REQUEST ?= 256Mi
export SSR_CONTAINER_PORT ?= ${SSR_SERVICE_TARGET_PORT}

export CELERY_WORKERS_NAME ?= celery-worker
export CELERY_WORKERS_REPLICAS ?= 1
export CELERY_WORKERS_CPU_LIMIT ?= 2
export CELERY_WORKERS_CPU_REQUEST ?= 100m
export CELERY_WORKERS_MEMORY_LIMIT ?= 4Gi
export CELERY_WORKERS_MEMORY_REQUEST ?= 256Mi
export CELERY_WORKERS_CONCURRENCY ?= 4
export CELERY_WORKERS_QUEUES ?= mdn_purgeable,mdn_search,mdn_emails,mdn_wiki,mdn_api,celery

export CELERY_BEAT_NAME ?= celery-beat
export CELERY_BEAT_REPLICAS ?= 1
export CELERY_BEAT_CPU_LIMIT ?= 2
export CELERY_BEAT_CPU_REQUEST ?= 100m
export CELERY_BEAT_MEMORY_LIMIT ?= 4Gi
export CELERY_BEAT_MEMORY_REQUEST ?= 256Mi

export KUMASCRIPT_NAME ?= kumascript
export KUMASCRIPT_REPLICAS ?= 1
export KUMASCRIPT_CONTAINER_PORT ?= ${KUMASCRIPT_SERVICE_TARGET_PORT}
export KUMASCRIPT_IMAGE ?= mdnwebdocs/kumascript
export KUMASCRIPT_IMAGE_PULL_POLICY ?= IfNotPresent
export KUMASCRIPT_CPU_LIMIT ?= 2
export KUMASCRIPT_CPU_REQUEST ?= 100m
export KUMASCRIPT_MEMORY_LIMIT ?= 4Gi
export KUMASCRIPT_MEMORY_REQUEST ?= 256Mi
export KUMASCRIPT_CACHE_MEGABYTES ?= 80
export KUMASCRIPT_CACHE_MINUTES ?= 60

export KUMA_IMAGE ?= mdnwebdocs/kuma
export KUMA_IMAGE_PULL_POLICY ?= IfNotPresent
# "KUMA_MOUNT_PATH" sets the mount path for the claim of the shared volume.
export KUMA_MOUNT_PATH ?= /mdn

# Defaults for the Kuma environment.
export KUMA_ACCOUNT_DEFAULT_HTTP_PROTOCOL ?= "https"
export KUMA_ADMIN_NAMES ?= "MDN devs"
export KUMA_ATTACHMENT_HOST ?= dev.mdn.mozit.cloud
export KUMA_ATTACHMENTS_AWS_STORAGE_BUCKET_NAME ?= ""
export KUMA_ATTACHMENTS_AWS_S3_REGION_NAME ?= "us-west-2"
export KUMA_ATTACHMENTS_AWS_S3_CUSTOM_DOMAIN ?= ""
export KUMA_ATTACHMENTS_USE_S3 ?= False
export KUMA_CELERY_TASK_ALWAYS_EAGER ?= False
export KUMA_CELERY_WORKER_MAX_TASKS_PER_CHILD ?= 0
export KUMA_CSRF_COOKIE_SECURE ?= True
export KUMA_CSP_ENABLE_MIDDLEWARE ?= False
export KUMA_CSP_REPORT_ENABLE ?= False
export KUMA_CSP_REPORT_ONLY ?= True
export KUMA_CSP_REPORT_URI ?= /csp-violation-capture
export KUMA_DEBUG ?= False
export KUMA_DEBUG_TOOLBAR ?= False
export KUMA_DOMAIN ?= dev.mdn.mozit.cloud
export KUMA_EMAIL_BACKEND ?= django.core.mail.backends.smtp.EmailBackend
export KUMA_ENABLE_CONTRIBUTIONS ?= False
export KUMA_ENABLE_CONTRIBUTIONS_CONFIRMATION_EMAIL ?= False
export KUMA_ES_INDEX_PREFIX ?= mdn
export KUMA_ES_LIVE_INDEX ?= False
export KUMA_GOOGLE_ANALYTICS_ACCOUNT ?= 0
export KUMA_LEGACY_ROOT ?= /mdn/www
export KUMA_MAINTENANCE_MODE ?= False
export KUMA_MEDIA_ROOT ?= /mdn/www
export KUMA_MEDIA_URL ?= /media/
export KUMA_PROTOCOL ?= "https://"
export KUMA_SECURE_HSTS_SECONDS ?= 0
export KUMA_SERVE_LEGACY ?= True
export KUMA_SESSION_COOKIE_SECURE ?= True
export KUMA_SSR_TIMEOUT ?= 5
export KUMA_STATIC_URL ?= /static/
export KUMA_STRIPE_PLAN_ID ?= ""
export KUMA_STRIPE_PUBLIC_KEY ?= ""
export KUMA_WEB_CONCURRENCY ?= 4
export KUMA_WIKI_HOST ?= wiki.${KUMA_DOMAIN}

export INTERACTIVE_EXAMPLES_BASE_URL ?= https://interactive-examples.mdn.mozilla.net

# Derived environment variables for both Kuma and Kumascript. These are always set.
export KUMA_SSR_URL=http://${SSR_SERVICE_NAME}/ssr
export KUMASCRIPT_DOCUMENT_URL=http://${API_SERVICE_NAME}
export KUMA_URL_TEMPLATE_FOR_KUMASCRIPT=http://${KUMASCRIPT_SERVICE_NAME}:${KUMASCRIPT_SERVICE_PORT}/docs/{path}
export KUMASCRIPT_DOCUMENT_URL_TEMPLATE=${KUMASCRIPT_DOCUMENT_URL}/en-US/docs/{path}?raw=1&redirect=no
export KUMASCRIPT_LIVE_SAMPLES_BASE_URL=${KUMA_PROTOCOL}${KUMA_ATTACHMENT_HOST}

# MDN backup tool
export BACKUP_SERVICE_NAME ?= mdn-backup-${TARGET_ENVIRONMENT}
export RESTORE_SERVICE_NAME ?= mdn-restore-${TARGET_ENVIRONMENT}
export SYNC_FROM_S3_SERVICE_NAME ?= mdn-s3-sync-${TARGET_ENVIRONMENT}
export BACKUP_SECRETS_NAME ?= mdn-backup-secrets

export BACKUP_MOUNT_DIR ?= "/mdn"

export BACKUP_BUCKET ?= s3://mdn-efs-backup-c2037ed87dd96008
export AWS_BACKUP_REGION ?= us-west-2
export AWS_BACKUP_PAGE_SIZE ?= 100

export BACKUP_LOCAL_DIR ?= "/mdn/www/"
# note, this is different than the sync directory in S3
export BACKUP_REMOTE_DIR ?= "/backups/mdn/"

export SYNC_BUCKET ?= s3://mdn-efs-backup-c2037ed87dd96008
export AWS_SYNC_REGION ?= us-west-2
export AWS_SYNC_PAGE_SIZE ?= 100
export SYNC_LOCAL_DIR ?= "/mdn/www/"
export SYNC_REMOTE_DIR ?= "/backups/efs/"

export BACKUP_CONTAINER_NAME ?= mdn-backup
export SYNC_FROM_S3_CONTAINER_NAME ?= mdn-sync
export BACKUP_IMAGE ?= mdnwebdocs/mdn-backup:51ae821
# cronjob syntax here: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
export BACKUP_SERVICE_SCHEDULE ?= "@hourly"
export RESTORE_SERVICE_SCHEDULE ?= "@hourly"
export SYNC_FROM_S3_SCHEDULE ?= "@hourly"

export RDS_BACKUP_DIR ?= /backup
export RDS_BACKUP_DBTYPE ?= MYSQL
export RDS_BACKUP_DEBUG_MODE ?= false
export RDS_BACKUP_IMAGE_TAG ?= d7d259b
export RDS_BACKUP_IMAGE ?= mdnwebdocs/mdn-rds-backup
export RDS_BACKUP_SCHEDULE ?= "@daily"
export RDS_BACKUP_BUCKET ?= s3://mdn-rds-backup-7752d5ca6f3744a0/backups

export FAILED_JOBS_HISTORY_LIMIT ?= 3
export SUCCESSFUL_JOBS_HISTORY_LIMIT ?= 3

# https://kubernetes.io/docs/concepts/configuration/secret/
# the values below are NOT real access/secret keys
export BACKUP_ACCESS_KEY ?= foo
export BACKUP_SECRET_KEY ?= bar
export BACKUP_ACCESS_KEY_BASE64 ?= $(shell echo -n "${BACKUP_ACCESS_KEY}" | base64)
export BACKUP_SECRET_KEY_BASE64 ?= $(shell echo -n "${BACKUP_SECRET_KEY}" | base64)
export BACKUP_DEADMANSSNITCH_URL ?= baz
export BACKUP_DEADMANSSNITCH_URL_BASE64 ?= $(shell echo -n "${BACKUP_DEADMANSSNITCH_URL}" | base64)

export ADMIN_NODE_NAME ?= mdn-admin

export ELB_S3_LOGGING_ENABLED ?= false
# Logging interval specified in minutes.
export ELB_S3_LOGGING_INTERVAL ?= 60
# S3 bucket name without the s3:// prefix.
export ELB_S3_LOGGING_BUCKET ?= mdn-elb-logs-c2037ed87dd96008
# ELB_S3_LOGGING_PREFIX can't end with a slash!
export ELB_S3_LOGGING_PREFIX ?= ${TARGET_ENVIRONMENT}
# Connection-idle timeout specified in seconds.
export ELB_CONNECTION_IDLE_TIMEOUT ?= 60

### New Relic configuration
export NEW_RELIC_SECRETS_NAME ?= newrelic-secrets
export NEW_RELIC_LICENSE_KEY ?= foo
export NEW_RELIC_LICENSE_KEY_BASE64 ?= $(shell echo -n "${NEW_RELIC_LICENSE_KEY}" | base64)
export NEW_RELIC_CONFIG_FILE ?= /app/etc/newrelic.ini
export NEW_RELIC_MONITOR_MODE ?= 1
export NEW_RELIC_LOG ?= stderr
export NEW_RELIC_BROWSER_MONITOR_ENABLE ?= false
export NEW_RELIC_LABELS ?= Project:MDN;Cluster:${K8S_CLUSTER_SHORT_NAME};Namespace:${K8S_NAMESPACE}
export NEW_RELIC_LOG_LEVEL ?= info

# New Relic app names
export NEW_RELIC_MONITOR_SUFFIX ?= ${TARGET_ENVIRONMENT}-${K8S_CLUSTER_SHORT_NAME}
export NEW_RELIC_ROLLUP_NAME ?= kuma-${NEW_RELIC_MONITOR_SUFFIX}
export NEW_RELIC_WEB_NAME ?= "kuma-web-${NEW_RELIC_MONITOR_SUFFIX};${NEW_RELIC_ROLLUP_NAME}"
export NEW_RELIC_API_NAME ?= "kuma-backend-${NEW_RELIC_MONITOR_SUFFIX};${NEW_RELIC_ROLLUP_NAME}"
export NEW_RELIC_KUMASCRIPT_NAME ?= "kumascript-${NEW_RELIC_MONITOR_SUFFIX}"
export NEW_RELIC_CELERY_NAME ?= "kuma-backend-${NEW_RELIC_MONITOR_SUFFIX};${NEW_RELIC_ROLLUP_NAME}"
export NEW_RELIC_SSR_NAME ?= "ssr-${NEW_RELIC_MONITOR_SUFFIX}"

export DATADOG_REDIS_DEPLOYMENT_NAME ?= mdn-dd-redis
export DATADOG_SECRETS_NAME ?= datadog-secrets

export DATADOG_API_KEY ?= foo
export DATADOG_API_KEY_BASE64 ?= $(shell echo -n "${DATADOG_API_KEY}" | base64)

export DATADOG_REDIS_CONFIG ?= foo
# Note that the string should never be split w/newlines.
# see https://kubernetes.io/docs/concepts/configuration/secret/
export DATADOG_REDIS_CONFIG_BASE64 ?= $(shell echo -n "${DATADOG_REDIS_CONFIG}" | base64)

export PERCONA_TOOLKIT_NS ?= percona-toolkit
export PERCONA_TOOLKIT_IMAGE ?= mdnwebdocs/percona-toolkit:226571b

###############################
### core tasks

k8s-ns: check-service-env
	${KUBECTL} create ns ${K8S_NAMESPACE} | true

k8s-delete-ns: check-service-env
	${KUBECTL} delete --ignore-not-found ns ${K8S_NAMESPACE}

k8s-shared-storage: k8s-pv-shared k8s-pvc-shared k8s-efs-setup-job

k8s-delete-shared-storage: k8s-delete-efs-setup-job k8s-delete-pvc-shared \
						   k8s-delete-pv-shared

k8s-services: k8s-web-svc k8s-api-svc k8s-kumascript-svc k8s-ssr-svc

k8s-delete-services: k8s-delete-web-svc k8s-delete-api-svc \
					 k8s-delete-kumascript-svc k8s-delete-ssr-svc

k8s-deployments: k8s-kuma-deployments k8s-kumascript-deployments

k8s-delete-deployments: k8s-delete-kuma-deployments \
						k8s-delete-kumascript-deployments

k8s-kuma-deployments: k8s-web k8s-api k8s-celery k8s-ssr

k8s-delete-kuma-deployments: k8s-delete-web k8s-delete-api k8s-delete-celery \
							 k8s-delete-ssr

k8s-kumascript-deployments: k8s-kumascript

k8s-delete-kumascript-deployments: k8s-delete-kumascript

k8s-rollout-status: k8s-kuma-rollout-status k8s-kumascript-rollout-status

k8s-kuma-rollout-status:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${WEB_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${API_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${CELERY_WORKERS_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${CELERY_BEAT_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${SSR_NAME}

k8s-kumascript-rollout-status:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout status deploy ${KUMASCRIPT_NAME}

k8s-rollback: k8s-kuma-rollback k8s-kumascript-rollback

k8s-kuma-rollback:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${WEB_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${API_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${CELERY_WORKERS_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${CELERY_BEAT_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${SSR_NAME}

k8s-kumascript-rollback:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout undo deploy ${KUMASCRIPT_NAME}

k8s-history: k8s-kuma-history k8s-kumascript-history

k8s-kuma-history:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${WEB_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${API_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${CELERY_WORKERS_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${CELERY_BEAT_NAME}
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${SSR_NAME}

k8s-kumascript-history:
	${KUBECTL} -n ${K8S_NAMESPACE} rollout history deploy ${KUMASCRIPT_NAME}

k8s-db-migration-job: k8s-delete-db-migration-job
	env KUMA_NAME=mdn-db-migration \
		KUMA_CPU_LIMIT=${WEB_CPU_LIMIT} \
		KUMA_MEMORY_LIMIT=${WEB_MEMORY_LIMIT} \
		KUMA_CPU_REQUEST=${WEB_CPU_REQUEST} \
		KUMA_MEMORY_REQUEST=${WEB_MEMORY_REQUEST} \
		KUMA_ALLOWED_HOSTS=${WEB_ALLOWED_HOSTS} \
		KUMA_RATELIMIT_ENABLE=False \
		NEW_RELIC_APP_NAME=${NEW_RELIC_WEB_NAME} \
		j2 mdn-db-migration-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -
	env JOB_NAME=mdn-db-migration ./wait_for_job.sh

k8s-delete-db-migration-job:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found job mdn-db-migration

k8s-kuma-record-deployment-job: k8s-kuma-delete-record-deployment-job
	@ echo FROM_REVISION_HASH=${FROM_REVISION_HASH}
	@ echo TO_REVISION_HASH=${TO_REVISION_HASH}
	env APP_NAME=kuma \
		j2 mdn-record-deployment-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -
	env JOB_NAME=mdn-kuma-record-deployment ./wait_for_job.sh

k8s-kuma-delete-record-deployment-job:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found job mdn-kuma-record-deployment

k8s-kumascript-record-deployment-job: k8s-kumascript-delete-record-deployment-job
	@ echo FROM_REVISION_HASH=${FROM_REVISION_HASH}
	@ echo TO_REVISION_HASH=${TO_REVISION_HASH}
	env APP_NAME=kumascript \
		j2 mdn-record-deployment-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -
	env JOB_NAME=mdn-kumascript-record-deployment ./wait_for_job.sh

k8s-kumascript-delete-record-deployment-job:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found job mdn-kumascript-record-deployment

### end core tasks
###############################

k8s-pv-shared: check-service-env
	j2 shared.pv.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-pv-shared: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found pv ${SHARED_PV_NAME}

k8s-pvc-shared: check-service-env
	j2 shared.pvc.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-pvc-shared: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found pvc ${SHARED_PVC_NAME}

k8s-efs-setup-job: check-service-env
	j2 mdn-efs-setup-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-efs-setup-job: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found job mdn-efs-setup

k8s-web-svc: check-service-env
	env SERVICE_NAME=${WEB_SERVICE_NAME} \
		SERVICE_TYPE=${WEB_SERVICE_TYPE} \
		SERVICE_PORT=${WEB_SERVICE_PORT} \
		SERVICE_TARGET_PORT=${WEB_SERVICE_TARGET_PORT} \
		SERVICE_PROTOCOL=${WEB_SERVICE_PROTOCOL} \
		SERVICE_CERT_ARN=${WEB_SERVICE_CERT_ARN} \
		TARGET_ENVIRONMENT=${TARGET_ENVIRONMENT} \
		ELB_S3_LOGGING_ENABLED=false \
		ELB_CONNECTION_IDLE_TIMEOUT=${WEB_GUNICORN_TIMEOUT} \
		j2 cert.svc.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-web-svc: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		svc ${WEB_SERVICE_NAME}

k8s-api-svc: check-service-env
	env SERVICE_NAME=${API_SERVICE_NAME} \
		SERVICE_TYPE=${API_SERVICE_TYPE} \
		SERVICE_PORT=${API_SERVICE_PORT} \
		SERVICE_TARGET_PORT=${API_SERVICE_TARGET_PORT} \
		SERVICE_PROTOCOL=${API_SERVICE_PROTOCOL} \
		j2 svc.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-api-svc: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		svc ${API_SERVICE_NAME}

k8s-kumascript-svc: check-service-env
	env SERVICE_NAME=${KUMASCRIPT_SERVICE_NAME} \
		SERVICE_TYPE=${KUMASCRIPT_SERVICE_TYPE} \
		SERVICE_PORT=${KUMASCRIPT_SERVICE_PORT} \
		SERVICE_TARGET_PORT=${KUMASCRIPT_SERVICE_TARGET_PORT} \
		SERVICE_PROTOCOL=${KUMASCRIPT_SERVICE_PROTOCOL} \
		j2 svc.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-kumascript-svc: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		svc ${KUMASCRIPT_SERVICE_NAME}

k8s-ssr-svc: check-service-env
	env SERVICE_NAME=${SSR_SERVICE_NAME} \
		SERVICE_TYPE=${SSR_SERVICE_TYPE} \
		SERVICE_PORT=${SSR_SERVICE_PORT} \
		SERVICE_TARGET_PORT=${SSR_SERVICE_TARGET_PORT} \
		SERVICE_PROTOCOL=${SSR_SERVICE_PROTOCOL} \
		j2 svc.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-ssr-svc: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		svc ${SSR_SERVICE_NAME}

###############################
### administrative tasks
# not referenced from parent targets

k8s-newrelic-secrets: check-service-env
	j2 mdn-newrelic-secrets.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-newrelic-secrets: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found secret ${NEW_RELIC_SECRETS_NAME}

k8s-backup-secrets: check-service-env
	j2 mdn-backup-secrets.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-backup-secrets: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found secret ${BACKUP_SECRETS_NAME}

# backup EFS to S3, for production
k8s-backup-cron: check-service-env
	j2 mdn-backup-cron.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-backup-cron: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found cronjob ${BACKUP_SERVICE_NAME}


# test backup pod
k8s-backup-test-pod: check-service-env
	j2 mdn-backup-test-pod.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-backup-test-pod: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found pod mdn-backup-test


# restore data from S3 to EFS
k8s-restore-cron: check-service-env
	j2 mdn-restore-cron.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-restore-cron: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found cronjob ${RESTORE_SERVICE_NAME}

# pull files from S3 (SCL3), for dev/stage
k8s-sync-from-s3-cron: check-service-env
	j2 mdn-sync-from-s3-cron.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-sync-from-s3-cron: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found cronjob ${SYNC_FROM_S3_SERVICE_NAME}

k8s-admin-node: check-service-env
	j2 mdn-admin-node.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-admin-node: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found deployment ${ADMIN_NODE_NAME}

k8s-datadog-secrets: check-service-env
	j2 datadog-secrets.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-datadog-secrets: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found secret ${DATADOG_SECRETS_NAME}

k8s-redis-dd: check-service-env
	j2 mdn-dd-redis.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-redis-dd: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found deployment ${DATADOG_REDIS_DEPLOYMENT_NAME}

k8s-rds-backup-cron: check-service-env
	j2 mdn-rds-backup-cron.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-rds-backup-cron: check-service-env
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found cronjob mdn-rds-backup

# one-time job to push EFS to S3
k8s-sync-efs-to-s3-job: check-service-env
	env PUSH_OR_PULL=PUSH \
		JOB_NAME=mdn-sync-efs-to-s3 \
		j2 mdn-sync-efs-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

# one-time job to load EFS from S3
k8s-sync-efs-from-s3-job: check-service-env
	env PUSH_OR_PULL=PULL \
		JOB_NAME=mdn-sync-efs-from-s3 \
		j2 mdn-sync-efs-job.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -


#check-service-env
k8s-percona-toolkit-ptkill: check-service-env
	j2 percona-toolkit-ptkill.yaml.j2 | ${KUBECTL} apply -n ${PERCONA_TOOLKIT_NS} -f -

k8s-delete-percona-toolkit-ptkill: check-service-env
	${KUBECTL} delete -n ${PERCONA_TOOLKIT_NS} --ignore-not-found deployment percona-toolkit-ptkill


### end administrative tasks
###############################

k8s-web:
	env KUMA_NAME=${WEB_NAME} \
		KUMA_REPLICAS=${WEB_REPLICAS} \
		KUMA_APP_LABEL=${WEB_SERVICE_NAME} \
		KUMA_CONTAINER_PORT=${WEB_SERVICE_TARGET_PORT} \
		KUMA_GUNICORN_WORKERS=${WEB_GUNICORN_WORKERS} \
		KUMA_GUNICORN_TIMEOUT=${WEB_GUNICORN_TIMEOUT} \
		KUMA_GUNICORN_WORKER_MAX_REQUESTS=${WEB_GUNICORN_WORKER_MAX_REQUESTS} \
		KUMA_GUNICORN_WORKER_MAX_REQUESTS_JITTER=${WEB_GUNICORN_WORKER_MAX_REQUESTS_JITTER} \
		KUMA_CPU_LIMIT=${WEB_CPU_LIMIT} \
		KUMA_MEMORY_LIMIT=${WEB_MEMORY_LIMIT} \
		KUMA_CPU_REQUEST=${WEB_CPU_REQUEST} \
		KUMA_MEMORY_REQUEST=${WEB_MEMORY_REQUEST} \
		KUMA_ALLOWED_HOSTS=${WEB_ALLOWED_HOSTS} \
		KUMA_RATELIMIT_ENABLE=${WEB_RATELIMIT_ENABLE} \
		NEW_RELIC_APP_NAME=${NEW_RELIC_WEB_NAME} \
		j2 kuma.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-web:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found deploy ${WEB_NAME}

k8s-api:
	env KUMA_NAME=${API_NAME} \
		KUMA_REPLICAS=${API_REPLICAS} \
		KUMA_APP_LABEL=${API_SERVICE_NAME} \
		KUMA_CONTAINER_PORT=${API_SERVICE_TARGET_PORT} \
		KUMA_GUNICORN_WORKERS=${API_GUNICORN_WORKERS} \
		KUMA_GUNICORN_TIMEOUT=${API_GUNICORN_TIMEOUT} \
		KUMA_GUNICORN_WORKER_MAX_REQUESTS=${API_GUNICORN_WORKER_MAX_REQUESTS} \
		KUMA_GUNICORN_WORKER_MAX_REQUESTS_JITTER=${API_GUNICORN_WORKER_MAX_REQUESTS_JITTER} \
		KUMA_CPU_LIMIT=${API_CPU_LIMIT} \
		KUMA_MEMORY_LIMIT=${API_MEMORY_LIMIT} \
		KUMA_CPU_REQUEST=${API_CPU_REQUEST} \
		KUMA_MEMORY_REQUEST=${API_MEMORY_REQUEST} \
		KUMA_ALLOWED_HOSTS=${API_ALLOWED_HOSTS} \
		KUMA_RATELIMIT_ENABLE=False \
		KUMA_WIKI_HOST=${API_SERVICE_NAME} \
		NEW_RELIC_APP_NAME=${NEW_RELIC_API_NAME} \
		j2 kuma.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-api:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found deploy ${API_NAME}

k8s-kumascript:
	env KUMASCRIPT_APP_LABEL=${KUMASCRIPT_SERVICE_NAME} \
		NEW_RELIC_APP_NAME=${NEW_RELIC_KUMASCRIPT_NAME} \
		j2 kumascript.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-kumascript:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		deploy ${KUMASCRIPT_NAME}

k8s-celery: k8s-celery-workers k8s-celery-beat

k8s-delete-celery: k8s-delete-celery-workers k8s-delete-celery-beat

k8s-celery-workers:
	env KUMA_NAME=${CELERY_WORKERS_NAME} \
		KUMA_APP_LABEL=${CELERY_WORKERS_NAME} \
		KUMA_REPLICAS=${CELERY_WORKERS_REPLICAS} \
		KUMA_CPU_LIMIT=${CELERY_WORKERS_CPU_LIMIT} \
		KUMA_MEMORY_LIMIT=${CELERY_WORKERS_MEMORY_LIMIT} \
		KUMA_CPU_REQUEST=${CELERY_WORKERS_CPU_REQUEST} \
		KUMA_MEMORY_REQUEST=${CELERY_WORKERS_MEMORY_REQUEST} \
		KUMA_ALLOWED_HOSTS="" \
		KUMA_RATELIMIT_ENABLE=False \
		NEW_RELIC_APP_NAME=${NEW_RELIC_CELERY_NAME} \
		j2 celery.workers.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-celery-workers:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		deploy ${CELERY_WORKERS_NAME}

k8s-celery-beat:
	env KUMA_NAME=${CELERY_BEAT_NAME} \
		KUMA_APP_LABEL=${CELERY_BEAT_NAME} \
		KUMA_REPLICAS=${CELERY_BEAT_REPLICAS} \
		KUMA_CPU_LIMIT=${CELERY_BEAT_CPU_LIMIT} \
		KUMA_MEMORY_LIMIT=${CELERY_BEAT_MEMORY_LIMIT} \
		KUMA_CPU_REQUEST=${CELERY_BEAT_CPU_REQUEST} \
		KUMA_MEMORY_REQUEST=${CELERY_BEAT_MEMORY_REQUEST} \
		KUMA_ALLOWED_HOSTS="" \
		KUMA_RATELIMIT_ENABLE=False \
		NEW_RELIC_APP_NAME="" \
		j2 celery.beat.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-celery-beat:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found \
		deploy ${CELERY_BEAT_NAME}

k8s-ssr:
	j2 ssr.deploy.yaml.j2 | ${KUBECTL} apply -n ${K8S_NAMESPACE} -f -

k8s-delete-ssr:
	${KUBECTL} delete -n ${K8S_NAMESPACE} --ignore-not-found deploy ${SSR_NAME}

check-service-env:
	./check_infra_lock.sh

k8s-get-kuma-revision-hash:
	@ ${KUBECTL} -n ${K8S_NAMESPACE} exec $(shell ${KUBECTL} -n ${K8S_NAMESPACE} get pods --selector app=${WEB_SERVICE_NAME} -o jsonpath='{.items[0].metadata.name}') -- printenv REVISION_HASH

k8s-get-kumascript-revision-hash:
	@ ${KUBECTL} -n ${K8S_NAMESPACE} exec $(shell ${KUBECTL} -n ${K8S_NAMESPACE} get pods --selector app=${KUMASCRIPT_SERVICE_NAME} -o jsonpath='{.items[0].metadata.name}') -- printenv REVISION_HASH

# These tasks don't have file targets
.PHONY: k8s-services k8s-delete-services k8s-ns k8s-delete-ns k8s-pv-shared \
		k8s-delete-pv-shared k8s-pvc-shared k8s-delete-pvc-shared \
		k8s-shared-storage k8s-delete-shared-storage \
		k8s-web-svc k8s-delete-web-svc k8s-api-svc k8s-delete-api-svc \
		k8s-ssr-svc k8s-delete-ssr-svc k8s-kumascript-svc \
		k8s-delete-kumascript-svc k8s-deployments k8s-delete-deployments \
		k8s-web k8s-delete-web k8s-api k8s-delete-api k8s-kumascript \
		k8s-delete-kumascript k8s-celery k8s-delete-celery k8s-celery-workers \
		k8s-delete-celery-workers k8s-celery-beat k8s-delete-celery-beat \
		k8s-kuma-deployments \
		k8s-delete-kuma-deployments k8s-kumascript-deployments \
		k8s-delete-kumascript-deployments k8s-rollout-status \
		k8s-kuma-rollout-status k8s-kumascript-rollout-status \
		k8s-kuma-record-deployment-job k8s-kumascript-record-deployment-job \
		k8s-kuma-delete-record-deployment-job \
		k8s-kumascript-delete-record-deployment-job \
		k8s-get-kuma-revision-hash k8s-get-kumascript-revision-hash \
		k8s-rds-backup-cron k8s-delete-rds-backup-cron k8s-ssr k8s-delete-ssr \
		check-service-env
