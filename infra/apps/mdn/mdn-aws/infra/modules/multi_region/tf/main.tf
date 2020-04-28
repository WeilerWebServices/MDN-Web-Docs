provider "aws" {
  region = "${var.region}"
}

module "info" {
  source      = "github.com/nubisproject/nubis-terraform//info?ref=v2.2.0"
  region      = "${var.region}"
  environment = "${var.environment}"
  account     = "${var.account}"
}

data "aws_security_group" "kube_master" {
  count = "${var.enabled}"

  filter {
    name = "group-name"

    values = [
      "masters.k8s.*",
    ]
  }
}

data "aws_security_group" "kube_nodes" {
  count = "${var.enabled}"

  filter {
    name = "group-name"

    values = [
      "nodes.k8s.*",
    ]
  }
}

locals {
  kube_master_sg  = "${list(element(concat(data.aws_security_group.kube_master.*.id, list("")),0))}"
  kube_node_sg    = "${list(element(concat(data.aws_security_group.kube_nodes.*.id, list("")),0))}"
  security_groups = "${compact(concat(split(",", module.info.instance_security_groups), local.kube_node_sg, local.kube_master_sg))}"
}

#########################################
# EFS
#########################################

module "efs" {
  source               = "./efs"
  enabled              = "${var.enabled * var.enable_efs}"
  environment          = "${var.environment}"
  region               = "${var.region}"
  efs_name             = "${var.environment}"
  subnets              = "${module.info.private_subnets}"
  nodes_security_group = "${local.security_groups}"
}

#module "efs-dev" {
#    source = "efs"
#    efs_name = "dev"
#    subnets = "${var.subnets}"
#    nodes_security_group = "${var.nodes_security_group}"
#}

#########################################
# Redis
#########################################

module "redis" {
  source = "./redis"

  enabled              = "${var.enabled * var.enable_redis}"
  region               = "${var.region}"
  environment          = "${var.environment}"
  redis_name           = "${var.environment}"
  redis_node_size      = "${var.redis_node_size}"
  redis_num_nodes      = "${var.redis_num_nodes}"
  subnets              = "${module.info.private_subnets}"
  nodes_security_group = "${split(",",module.info.instance_security_groups)}"
  nodes_security_group = "${local.security_groups}"
}

#module "redis-dev" {
#    source = "redis"
#    redis_name = "dev"
#    redis_node_size = "cache.t2.micro"
#    redis_num_nodes = 1
#    subnets = "${var.subnets}"
#    nodes_security_group = "${var.nodes_security_group}"
#}

#########################################
# MySQL
#########################################

module "mysql" {
  source = "./rds"

  enabled                     = "${var.enabled * var.enable_rds}"
  region                      = "${var.region}"
  environment                 = "${var.environment}"
  mysql_env                   = "${var.environment}"
  mysql_db_name               = "${var.mysql_db_name}"
  mysql_username              = "${var.mysql_username}"
  mysql_password              = "${var.mysql_password}"
  mysql_identifier            = "mdn-${var.environment}"
  mysql_instance_class        = "${var.mysql_instance_class}"
  mysql_backup_retention_days = "${var.mysql_backup_retention_days}"
  mysql_security_group_name   = "${var.mysql_security_group_name}_${var.environment}"
  mysql_storage_gb            = "${var.mysql_storage_gb}"
  mysql_storage_type          = "${var.mysql_storage_type}"
  vpc_id                      = "${module.info.vpc_id}"
  vpc_cidr                    = "${module.info.network_cidr}"
  subnets                     = "${module.info.private_subnets}"
}

#module "mysql-stage" {
#    source = "rds"
#    # DBName must begin with a letter and contain only alphanumeric characters
#
#    mysql_env     = "stage"
#    mysql_db_name = "developer_allizom_org"
#    mysql_username = "root"
#    mysql_password = "${var.mysql_stage_password}"
#    mysql_identifier = "mdn-stage"
#    mysql_instance_class = "db.t2.large"
#    mysql_backup_retention_days = 0
#   mysql_security_group_name = "mdn_rds_sg"
#    mysql_storage_gb = 100
#    mysql_storage_type = "gp2"
#    vpc_id = "${var.vpc_id}"
#    vpc_cidr = "${var.vpc_cidr}"
#}


#module "mysql-prod" {
#    source = "rds"
#    # DBName must begin with a letter and contain only alphanumeric characters
#    mysql_env     = "prod"
#    mysql_db_name = "developer_mozilla_org"
#    mysql_username = "root"
#    mysql_password = "${var.mysql_prod_password}"
#    mysql_identifier = "mdn-prod"
#    mysql_instance_class = "db.m4.xlarge"
#    mysql_backup_retention_days = 7
#    mysql_security_group_name = "mdn_rds_sg_prod"
#    mysql_storage_gb = 200
#    mysql_storage_type = "gp2"
#    vpc_id = "${var.vpc_id}"
#    vpc_cidr = "${var.vpc_cidr}"
#}

