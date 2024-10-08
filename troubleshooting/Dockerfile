FROM ccr.ccs.tencentyun.com/niewx/troubleshooting:tke
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache go redis mysql-client vim tcpdump curl bind-tools mtr nmap-ncat busybox-extras bash bash-doc bash-completion
RUN mkdir /app && mkdir /data && mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
COPY demo /app
WORKDIR /app
CMD ["/app/demo"]
