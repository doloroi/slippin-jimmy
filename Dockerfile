FROM python:2.7.11-slim
MAINTAINER Javi <me@javi.yt>

RUN pip install slippinj

CMD ["-"]
ENTRYPOINT ["jimmy", "-h"]
