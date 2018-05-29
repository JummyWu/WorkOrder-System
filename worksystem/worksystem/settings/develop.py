# coding:utf-8
__author__ = 'jummy'

from .base import * # NOQA
from decouple import config


DEBUG = config('DEBUG', default=True, cast=bool)
