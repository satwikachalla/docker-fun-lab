FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        cowsay figlet fortune-mod fortunes-min lolcat \
    && rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/games:${PATH}"
COPY run.sh /run.sh
RUN chmod +x /run.sh
ENTRYPOINT ["/run.sh"]
