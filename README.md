# burb 🐦
* upload audio to burb
* generate url per distinct audio
* browse uploaded audio


# Local setup 

## Development

Run API server locally:
* cd api
* node index.js
* API availible at localhost:3000

Run WEB with hot-reload locally (needs api running on :3000):
* cd web
* npm run serve
* browse to localhost:8080

## Docker

Run full system 
* docker-compose build
* docker-compose up -d
* WEB availible at localhost:8080 and API at localhost:3000