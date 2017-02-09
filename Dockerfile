FROM    docker.io/centos:7       
MAINTAINER netb2c <netb2c@qq.com> #A simple little man .

ENV TZ "Asia/Shanghai"
ENV TERM vt100

ADD aliyun-mirror.repo /etc/yum.repos.d/CentOS-Base.repo
ADD aliyun-epel.repo /etc/yum.repos.d/epel.repo

RUN yum install -y curl wget tar tcpdump iftop vim-enhanced passwd sudo yum-utils hostname net-tools rsync man pip && \
 yum clean all

RUN mkdir -p /data && \
  touch /tmp/test.txt

EXPOSE 22

ENTRYPOINT ["/usr/bin/echo", "Container is OK."]    
