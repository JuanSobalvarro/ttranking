FROM postgres:17

# Install dependencies for pgloader
RUN apt-get update && apt-get install -y \
    pgloader \
    sudo \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Default entrypoint for PostgreSQL
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]
