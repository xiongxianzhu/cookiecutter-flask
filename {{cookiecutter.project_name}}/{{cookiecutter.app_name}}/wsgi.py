# coding: utf-8

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.config import ProdConfig

CONFIG = ProdConfig

app = create_app(CONFIG)