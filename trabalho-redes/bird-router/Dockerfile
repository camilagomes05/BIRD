FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    bird2 \
    iproute2 \
    iputils-ping \
    traceroute \
    tcpdump \
    iptables \
    nano \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /run/bird

CMD ["bird", "-d", "-c", "/etc/bird/bird.conf"]
