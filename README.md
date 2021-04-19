# amplify-docker

See article [here](https://aws.amazon.com/de/blogs/mobile/zero-effort-container-deployment-for-graphql-and-rest-apis-and-web-hosting-with-amplify-cli/) on how to create this example.

## Run locally
Replace _localhost_ with _python_ on lines 20 and 65 in _amplify/backend/api/multicontainer/src/express/index.js_.

```bash
cd amplify/backend/api/multicontainer/src
docker-compose up --build
```