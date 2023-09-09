FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

ENV NV_CUDNN_VERSION 8.6.0.163
ENV NV_CUDNN_PACKAGE_NAME "libcudnn8"

ENV NV_CUDNN_PACKAGE "$NV_CUDNN_PACKAGE_NAME=$NV_CUDNN_VERSION-1+cuda11.8"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ${NV_CUDNN_PACKAGE} \
    unzip \
    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update -y \
    && apt-get install -y python3-pip espeak
RUN echo 'alias python=python3' >> ~/.bashrc
RUN echo 'NCCL_SOCKET_IFNAME=lo' >> ~/.bashrc

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

RUN cd /app/monotonic_align && python3 setup.py build_ext --inplace

ENTRYPOINT [ "bash" ]
