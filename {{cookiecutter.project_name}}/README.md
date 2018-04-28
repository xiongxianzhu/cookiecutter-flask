# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## 项目架构

项目采用架构：
```
python3.6.5+flask+nginx(web服务器)+uwsgi(or gunicorn应用服务)+mongodb3.6(mysql5.7.21)+supervisor(进程管理)+fabric(rsync部署多主机)+celery+rabbitmq+redis
```

## 项目目录结构详解

```
$ tree -a {{cookiecutter.project_name}}
{{cookiecutter.project_name}}       # 项目目录
├── autoapp.py                      # 项目开发环境程序启动主入口
├── {{cookiecutter.app_name}}       # 应用目录
│   ├── api                         # 通用API
│   │   ├── __init__.py
│   │   ├── resources
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── views.py
│   ├── app.py                      # 程序初始化
│   ├── auth                        # 认证
│   │   ├── __init__.py
│   │   └── views.py
│   ├── celery_runner.py            # celery脚本
│   ├── commands.py                 # 项目启动前所执行的命令
│   ├── commons                     # 常用工具
│   │   ├── __init__.py
│   │   └── pagination.py
│   ├── config.py                   # 配置文件
│   ├── email.py                    # 邮件发送
│   ├── extensions.py               # 扩展库实例化
│   ├── forms                       # 表单
│   │   └── __init__.py
│   ├── __init__.py
│   ├── logs                        # 日志
│   ├── models                      # 模型
│   │   ├── __init__.py
│   │   └── user.py
│   ├── static                      # 静态文件
│   ├── templates                   # 模块
│   │   ├── 401.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── footer.html
│   │   ├── layout.html
│   │   └── nav.html
│   ├── themes                      # 主题
│   ├── translations                # 多语言翻译
│   ├── views                       # 视图
│   │   └── __init__.py
│   ├── webpack                     # 前端模块打包
│   │   └── manifest.json
│   └── wsgi.py                     # 生产环境启动项目的主入口
├── data                            # 数据
├── deploy                          # 部署
├── docs                            # 文档
├── .env                            # 虚拟环境中的环境变量
├── HISTORY.rst                     # 版本更新历史记录
├── migrations                      # 数据迁移
├── package.json
├── Pipfile                         # pipenv虚拟环境依赖相关文件
├── Pipfile.lock                    # pipenv虚拟环境依赖相关文件
├── README.md                       # 项目说明文档
├── requirements                    # 项目开发环境与生产环境的依赖库及其版本
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt                # 项目开发环境与生产环境的依赖库及其版本
├── setup.cfg
├── setup.py.bak
├── tests                           # 测试
└── uwsgi.ini                       # 项目生产环境程序启动的uwsgi脚本

```

## 安装依赖

### 安装sqlite3相关依赖库

如果数据库采用了sqlite3则需要安装sqlite3相关依赖库， 否则不用安装。

For Ubuntu:

```
sudo apt-get install libsqlite3-dev sqlite3 -y
```

For Centos:

```
yum install sqlite-devel sqlite3 -y
```

## 创建虚拟环境并安装依赖库

```
$ pipenv --three
```

## 为虚拟环境安装依赖库

```
pipenv install
npm install
npm start
```
创建完虚拟环境后会在项目根目录下生成一个Pipfile文件， 将里面的Pypi源路径替换为国内阿里云的Pypi源：
```
sed -i 's/https:\/\/pypi.python.org/http:\/\/mirrors.aliyun.com\/pypi/g' Pipfile
```

p.s. 如果使用了官方pypi源`https://pypi.python.org/simple`, 则在执行`pipenv install`命令会生成`Pipfile.lock`。如果使用非官方pypi源， 则安装库时用`pipenv install`, 且不会生成`Pipfile.lock`文件。

若项目根目录还有.env文件， 则在执行`pipenv --three`命令创建虚拟环境时也会将.env文件里的环境变量添加到虚拟环境当中。
检测虚拟环境变量是否生效， 可以用`echo $环境变量`查看， 如下：

```
$ pipenv shell
(env)$ echo $FLASK_APP
autoapp.py
(env)$ echo $FLASK_DEBUG
1
(env)$ exit
$ 
```

为了项目能生成`Pipfile.lock`文件， 我们默认使用官方的pypi源`https://pypi.python.org/simple`。

## 初始化数据库

一旦你安装了你的dbms，运行以下命令创建你的应用程序的数据库表并执行初始迁移。

```
rm -fr migrations
flask db init
flask db migrate
flask db upgrade
npm start
```

若项目根目录存在migrations目录， 则先rm删除migrations目录再执行`flask db init`

## 在开发环境运行项目

```
$ pipenv --three
$ pipenv install
$ pipenv shell
(env)$ flask run
```

就这样! 项目以端口`5000`运行。

## 在生产环境运行项目

先将.env文件里的环境变量`FLASK_DEBUG`设置为`0`。

```
$ pipenv --three
$ pipenv install
```


### 用gunicorn作为应用服务器运行

项目提供了一个简单的wsgi入口，例如使用gunicorn或uwsgi运行。

```
$ pipenv install gunicorn
$ pipenv shell
(env)$ gunicorn {{cookiecutter.app_name}}.wsgi:app
```

就这样! gunicorn以端口`8000`运行项目。

### 用uwsgi作为应用服务器运行

几乎和gunicorn一样：

```
$ pipenv install uwsgi
$ pipenv shell
(env)$ uwsgi --http 127.0.0.1:5000 --module {{cookiecutter.app_name}}.wsgi:app
```

就这样! uwsgi以端口`5000`运行项目。