# 在线简历系统
###  环境配置
* Python 3.6 
```
安装 python 的时候全部按默认设置
```
* Django 2.0.5
```
# 安装好python后，打开cmd输入命令安装 Django 及需要的包
pip install -r requestments.txt
```
### 项目基本简介
#### 使用技术
```
前端在线编辑简历使用的是 JS 技术，后端则使用 Django 技术，前端通过 ajax 方式将数据传递到后台
```
#### 项目运行
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
# 打开浏览器访问 http://127.0.0.1:8000 即可
```
#### 数据库
1. 该系统使用的是系统自带的 SQLite 数据库，可以通过安装 Navicat for SQLite 来查看数据库内容，数据库在项目下的 db.sqlite3 这个数据库文件。如果要查看里面表结构，安装Navicat for SQLite (https://navicat.com.cn/products/navicat-for-sqlite) 即可查看里面数据.
2. 由于 Python 的 Django 框架只带数据库操作接口，也就是直接用 Python语句就可以操纵数据库，（http://www.cnblogs.com/linjiqin/archive/2014/07/01/3817954.html）这篇教程讲了 Django 的 ORM 映射。
3. 如需使用项目的后台管理，则需在项目目录下输入一下命令创建超级管理员,然后输入网址 http://127.0.0.1:8000/admin 进行登陆。
```
python manage.py createsuperuser
```
4. 如需更换 MySQL 数据库，在部署好数据库后，只需更改该项目下的 resume/settings.py 下的 DATABASES 即可，同时不要忘记在 resume/__init__.py 文件中添加如下命令：
```
import pymysql
pymysql.install_as_MySQLdb()
```
修改前：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
修改后：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'mydb',         # 数据库名（事先要创建）
        'USER': 'root',         # 用户名
        'PASSWORD': '123456',   # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 端口
    }
}
```