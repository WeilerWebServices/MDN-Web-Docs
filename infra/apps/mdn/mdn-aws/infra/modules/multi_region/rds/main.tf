provider "aws" {
  region = var.region
}

resource "aws_db_parameter_group" "mdn-params" {
  count = var.enabled ? 1 : 0

  name        = "${var.mysql_identifier}-params"
  family      = "mysql5.6"
  description = "Paramter group for ${var.mysql_identifier}"

  # https://stackoverflow.com/questions/8744813/mysql-error-2006-hy000-at-line-406-mysql-server-has-gone-away#10709964
  parameter {
    name  = "max_allowed_packet"
    value = "26214400"
  }
}

resource "aws_db_subnet_group" "rds" {
  count = var.enabled ? 1 : 0

  name        = "mdn-${var.environment}-rds-subnet-group"
  description = "mdn-${var.environment}-rds-subnet-group"

  subnet_ids = split(",", var.subnets)

  tags = {
    Name        = "mdn-${var.environment}-rds-subnet-group"
    Environment = var.environment
    Stack       = "mdn-rds-${var.environment}"
    Region      = var.region
  }
}

resource "aws_db_instance" "mdn_rds" {
  count = var.enabled ? 1 : 0

  allocated_storage           = var.mysql_storage_gb
  allow_major_version_upgrade = var.mysql_allow_major_version_upgrade
  auto_minor_version_upgrade  = var.mysql_auto_minor_version_upgrade
  backup_retention_period     = var.mysql_backup_retention_days
  backup_window               = var.mysql_backup_window

  # note: this resource already existed at time of provisioning from
  # our k8s install automation
  #db_subnet_group_name        = "main_subnet_group"
  db_subnet_group_name = element(aws_db_subnet_group.rds.*.name, count.index)

  depends_on = [aws_security_group.mdn_rds_sg]
  engine     = var.mysql_engine

  engine_version               = var.mysql_engine_version
  identifier                   = var.mysql_identifier
  instance_class               = var.mysql_instance_class
  maintenance_window           = var.mysql_maintenance_window
  multi_az                     = true
  name                         = var.mysql_db_name
  parameter_group_name         = aws_db_parameter_group.mdn-params[0].name
  password                     = var.mysql_password
  publicly_accessible          = false
  storage_encrypted            = var.mysql_storage_encrypted
  storage_type                 = var.mysql_storage_type
  username                     = var.mysql_username
  vpc_security_group_ids       = [aws_security_group.mdn_rds_sg[0].id]
  skip_final_snapshot          = true
  apply_immediately            = true
  monitoring_interval          = var.monitoring_interval
  performance_insights_enabled = var.performance_insights_enabled

  tags = {
    Name        = "MDN-rds-${var.environment}"
    Stack       = "MDN-rds-${var.mysql_env}"
    Environment = var.environment
    Region      = var.region
  }
}

resource "aws_security_group" "mdn_rds_sg" {
  count = var.enabled ? 1 : 0

  name        = var.mysql_security_group_name
  description = "Allow all inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = var.mysql_port
    to_port     = var.mysql_port
    protocol    = "TCP"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "mdn_rds_sg-${var.environment}"
    Stack       = "MDN-rds-${var.environment}"
    Environment = var.environment
    Region      = var.region
  }
}

