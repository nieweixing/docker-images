#!/bin/bash

python /root/get_cluster_token_and_ca.py

TOKEN=`cat /root/token`

apiserver_ip=`echo $KUBERNETES_PORT_443_TCP | awk -F'[/:]' '{print $4}'`
APISRRVICE=https://${apiserver_ip}

kubectl config set-cluster ${ClusterId} --certificate-authority='/root/ca.crt' --embed-certs=true --server=${APISRRVICE} --kubeconfig=${ClusterId}.kubeconfig

kubectl config set-credentials ${ClusterId} --token=${TOKEN} --kubeconfig=${ClusterId}.kubeconfig

kubectl config set-context ${ClusterId}-default --cluster=${ClusterId} --user=${ClusterId} --kubeconfig=${ClusterId}.kubeconfig

kubectl config use-context ${ClusterId}-default --kubeconfig=${ClusterId}.kubeconfig

mkdir -p /root/.kube

mv ${ClusterId}.kubeconfig /root/.kube/config

tail -f /dev/null
