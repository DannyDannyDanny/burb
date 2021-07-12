# Database
Database for indexing file system and storing labels.


## Redis
```yml
redis:
    container_name: "burb-redis"
    image: redis:latest
    volumes:
        - "./db/redis/data:/data"
    ports:
        - '6379:6379'
    networks:
        - default
    environment:
```

## PostgreSQL
```yml
db:
    container_name: "burb-db"
    image: postgres:latest
    volumes:
        - "./db/postgresql/data:/var/lib/postgresql/data/"
    # ports:
        # - 5432:5432
    networks:
        - default
    environment:
        POSTGRES_USER: username 
        # The PostgreSQL user (useful to connect to the database)
        POSTGRES_PASSWORD: password 
        # The PostgreSQL password (useful to connect to the database)
        POSTGRES_DB: default_database 
        # The PostgreSQL default database (automatically created at first launch)"
```