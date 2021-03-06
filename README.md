# cookiecutter-flask

Cookiecutter可以让你快速从模板中建立工程，cookiecutter-flask则是Flask的模板，可以快速生成Flask大型项目模板。

## 用法

```
$ pip install cookiecutter
$ cookiecutter https://github.com/xiongxianzhu/cookiecutter-flask.git
```

你将会被要求填写一些基本的项目信息。

## 在开发环境运行项目

先将.env文件里的环境变量`FLASK_DEBUG`设置为`1`, `FLASK_ENV`设置为`development`。

```
$ sudo pip install pipenv
$ pipenv --three
$ pipenv install
$ pipenv shell
(env)$ flask run
```

就这样! 项目以端口`5000`运行。

## 在生产环境运行项目

先将.env文件里的环境变量`FLASK_DEBUG`设置为`0`, `FLASK_ENV`设置为`production`。

```
$ sudo pip install pipenv
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


## 关于cookiecutter

- Documentation: https://cookiecutter.readthedocs.io
- GitHub: https://github.com/audreyr/cookiecutter
- PyPI: https://pypi.python.org/pypi/cookiecutter

## 参考项目

- cookiecutter-flask: https://github.com/sloria/cookiecutter-flask
- cookiecutter-flask-restful: https://github.com/karec/cookiecutter-flask-restful

## 参考文章

- [使用Flask设计RESTful APIs](http://www.pythondoc.com/flask-restful/index.html)
