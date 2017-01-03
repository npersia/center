docker stop $NAME_CENTER-dev
docker rm $NAME_CENTER-dev
docker create -it -p 8000:8000 -v $MYFILES:/myfiles --name=$NAME_CENTER-dev npersia/bottle-dev /bin/bash
docker start $NAME_CENTER-dev
