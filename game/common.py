import requests
import re
from lxml import etree
import datetime
import time
import sys
from utils import configureRead
import logging
import logging.config
import codecs
import yaml
logging.config.dictConfig(yaml.load(codecs.open("conf/logger.yml", 'r', 'utf-8').read()))



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'}
UTC_FORMAT = '%Y-%m-%d %H:%M:%S'
date_format = '%Y-%m-%d'
