# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


## 创建虚拟环境并安装依赖库

```
$ pipenv --three
```
创建完虚拟环境后会在项目根目录下生成一个Pipfile文件， 将里面的Pypi源路径替换为国内阿里云的Pypi源：
```
sed -i 's/https:\/\/pypi.python.org/http:\/\/mirrors.aliyun.com\/pypi/g' Pipfile
```

p.s. 如果使用了官方pypi源`https://pypi.python.org/simple`, 则在执行`pipenv install`命令会生成`Pipfile.lock`。如果使用非官方pypi源， 则安装库时用`pipenv install --skip-lock`, 且不会生成`Pipfile.lock`文件。

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