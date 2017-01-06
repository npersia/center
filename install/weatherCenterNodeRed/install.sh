ENV_NAME=$NAME_WEATHERCENTER_NODERED-$ENV_WEATHERCENTER_NODERED

docker stop $ENV_NAME
docker rm $ENV_NAME
docker create -it  -p $PORT_WEATHERCENTER_NODERED:1880 -v $FILES_WEATHERCENTER_NODERED:/data --link $LINK_REDIS_WEATHERCENTER_NODERED:redisweathercenter --name=$ENV_NAME $IMAGE_WEATHERCENTER_NODERED
docker start $ENV_NAME

