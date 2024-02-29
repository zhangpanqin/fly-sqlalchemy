## 环境搭建
### 安装依赖
```shell
pip install -r requirements.txt
```

### 数据库

1. 
```shell
docker volume inspect mysql_data
docker run -d \
    --name local_mysql \
    -p 3306:3306 \
    -v mysql_data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -e MYSQL_PASSWORD=123456 \
    -e MYSQL_USER=xiaozhang \
    -e MYSQL_DATABASE=sandbox \
    mysql:8.0.36-bullseye
```

2. 修改 [alembic.ini](alembic.ini)
```text
sqlalchemy.url = mysql+pymysql://root:123456@localhost/sandbox?charset=utf8mb4
```

### 使用
```shell
# 查看 migration 脚本历史记录
alembic history --verbose

# 根据脚本解析出 migration 脚本
alembic revision -m "Add a column"

# 更新到最新版本，依次执行 python 脚本
alembic upgrade head

# 初始化数据库
alembic upgrade base
```