#!/bin/sh

cd /home/tyhall51/gm/Django-GM/

DIR=./backup/mysql
if [ ! -e $DIR ]
then
mkdir -p $DIR
fi

# mysqldump
# docker-compose exec mysql mysqldump -uroot -p123456 management > "$DIR/data_`date +%Y%m%d`.sql"
# 绝对路径
docker exec -i mysql5.7 bash <<'EOF'

# 备份指定数据库
mysqldump -uroot -p123456 management > /backup/zuma_$(date +%Y%m%d).sql
 
exit
 
EOF
 
docker cp mysql5.7:/backup/zuma_$(date +%Y%m%d).sql $DIR

# 删除mysqldump错误
sed -i '/mysqldump/d' "$DIR/zuma_`date +%Y%m%d`.sql"

# 查找更改时间在30日以前的sql备份文件并删除
find $DIR -mtime +30 -name "zuma_[1-9]*.sql" -exec rm -rf {} \;

# git
git add "$DIR/*"
git add media/*
git commit -m 'backup'
git push
