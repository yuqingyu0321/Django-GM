#!/bin/sh

DIR=./backup/mysql
if [ ! -e $DIR ]
then
mkdir -p $DIR
fi

# mysqldump
docker-compose exec mysql mysqldump -uroot -p123456 management > "$DIR/data_`date +%Y%m%d`.sql"

# 查找更改时间在30日以前的sql备份文件并删除
find $DIR -mtime +30 -name "data_[1-9]*.sql" -exec rm -rf {} \;

# git
git add '$DIR/*'
git commit -m 'backup'
git push origin master