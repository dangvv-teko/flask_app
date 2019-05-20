# add service account kubeconfig
## b1: cài đặt jq
- Đứng ở master hoặc kubectl client (đã config để connect tới K8s cluster) cài đặt:
  - `sudo apt-get install jq`
## b2: create namespace
- ví dụ ở đây là:
  - `kubectl create ns teko-flask`
## b3: run script
- `sh kubernetes_add_service_account_kubeconfig.sh teko-flask teko-flask`
- trong đó:
  - `teko-flask` đầu tiên là tên service account sẽ tạo
  - `teko-flask` thứ 2 là tên namespace vừa tạo ở bước 2
## b4: create RBAC permissions for service account (ở đây là cho nó quyền cluster admin)
- `kubectl create -f rbac-teko-flask.yaml`
