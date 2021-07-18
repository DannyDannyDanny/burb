# burb 🐦
* upload audio to burb
* validate audio
* generate url per distinct audio
* browse uploaded audio

## Components
* API
* App
* Burb
* DB
* FTP
* Web

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
