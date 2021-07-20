# burb 🐦
Share sounds

|Components| Description
|--|--|
|[Web](web/README.md)  | Web interface for burb |
|[API](api/README.md)  | Uploades audio to server |
|[Burb](burb/README.md)| Audio parsing engine |
|[DB](db/README.md)    | Keep organized! |
|[FTP](ftp/README.md)  | Admin upload! |
|[App](app/README.md)  | _Future feature!_ 🚀 |

# Local setup

## Development

Run API server locally:
```
cd api
node index.js # API availible at localhost:3000
```

Run WEB with hot-reload locally (needs api running on :3000):
```
cd web
npm run serve # web interface localhost:8080
```

## Docker

Run full system
```
docker-compose build
docker-compose up -d
```
WEB available at `localhost:8080` and API at `localhost:3000`
