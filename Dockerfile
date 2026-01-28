FROM node:22.21.1-bookworm
RUN apt-get update && apt-get install -y \
  python3 \
  git \
  build-essential \
  bash \
  sudo \
  --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV COMMIT_HASH=b39c1f5
ENV REPO_URL=https://github.com/gvaishnavi-jpg/weather-cli-refactor.git
ENV REPO_NAME=weather-cli-refactor

WORKDIR /testbed/${REPO_NAME}
RUN git init && \
  git remote add origin ${REPO_URL} && \
  git fetch --depth 1 origin ${COMMIT_HASH} && \
  git checkout FETCH_HEAD && \
  git remote remove origin
RUN chmod -R 777 /testbed/${REPO_NAME}

CMD ["/bin/bash"]
