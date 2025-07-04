output "repository-ssh-url" {
  value = aws_codecommit_repository.argocd-poc-repository.clone_url_ssh
}

output "repository-arn" {
  value = aws_codecommit_repository.argocd-poc-repository.arn
}

output "repository-name" {
  value = aws_codecommit_repository.argocd-poc-repository.repository_name
}