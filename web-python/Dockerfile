FROM python:3.7
RUN sed -i 's/http:\/\/deb.debian.org/http:\/\/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN  apt-get update &&  apt-get install  curl net-tools vim   wget tcpdump mtr redis -y && apt-get clean
COPY web.py /
CMD ["python","/web.py"]

