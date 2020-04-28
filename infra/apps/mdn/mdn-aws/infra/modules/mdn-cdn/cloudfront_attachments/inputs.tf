variable "enabled" {
}

variable "distribution_name" {
}

variable "environment" {
}

variable "comment" {
}

variable "domain_name" {
}

variable "acm_cert_arn" {
}

variable "aliases" {
  type = list(string)
}

variable "standard_transition_days" {
  default = "60"
}

variable "glacier_transition_days" {
  default = "90"
}

variable "expiration_days" {
  default = "180"
}

variable "cloudfront_log_cookies" {
  default = false
}

variable "cloudfront_log_prefix" {
  default = ""
}

