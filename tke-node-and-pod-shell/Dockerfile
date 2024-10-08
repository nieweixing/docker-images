FROM alpine:latest
COPY . /root
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
apk add --no-cache redis mysql-client vim tcpdump curl bind-tools mtr nmap-ncat busybox-extras bash bash-doc bash-completion python3 py3-pip && \
pip3 install tencentcloud-sdk-python-tke --break-system-packages && \
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.22.5/bin/linux/amd64/kubectl && \
chmod +x ./kubectl && \
mv ./kubectl /usr/local/bin/kubectl && \
mv /root/kubectl-node_shell /usr/local/bin/
CMD ["sh", "-c", "/root/start.sh"]

