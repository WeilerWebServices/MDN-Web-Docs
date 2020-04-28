output "cdn-primary-arn" {
  value = element(
    concat(aws_cloudfront_distribution.mdn-primary-cf-dist.*.arn, [""]),
    0,
  )
}

output "cdn-primary-dns" {
  value = element(
    concat(
      aws_cloudfront_distribution.mdn-primary-cf-dist.*.domain_name,
      [""],
    ),
    0,
  )
}

output "cdn-primary-logging-bucket" {
  value = element(concat(aws_s3_bucket.logging.*.id, [""]), 0)
}

