ENV_NAME=$NAME_WEATHERCENTER_REDIS-$ENV_WEATHERCENTER_REDIS

docker stop $ENV_NAME
docker rm $ENV_NAME
docker create -it --name=$ENV_NAME $IMAGE_WEATHERCENTER_REDIS
docker start $ENV_NAME

