# Twitter-Clone-Docker
### This is a dockerized twitter clone application

This application is currently API only application.
To start the application, simply clone the application and then run the following commands

#### Start the containers
`sudo docker-compose up`

#### Run the alembic upgrade for grpc service
`sudo docker exec <grpc_container_id> alembic upgrade head`

### Useful docker commands
#### List all images
`sudo docker image ls -a`
#### List all containers
`sudo docker container ls -a`

For more docker commands visit [docker documentation](https://docs.docker.com/)
