# TaskFlow

Tiny task list for a DevOps lab. Not a product. Not SAP.

## What it does
- API with GET /health
- Create a task, list tasks
- Postgres in Docker Compose
- One simple web page

## What it does not
- Login / users
- Kubernetes / EKS
- Full CD
- Anything I did not run myself

## Architecture
GitHub → CI → image → one EC2 (Compose): UI → API → Postgres
Region: eu-central-1 when we use AWS.

## Path I already proved (Week 6)
Terraform created EC2. Ansible installed Docker.
Compose ran an app. curl 200 on the box. Then destroy.
