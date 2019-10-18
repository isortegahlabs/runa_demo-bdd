"""Hooks file."""
from behave.tag_matcher import ActiveTagMatcher
from ipdb import post_mortem
from json import load
from os import makedirs
from os.path import isdir
from logging import getLogger, config
from runa_demo.helpers import constants
from selenium import webdriver


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    context.browser.implicitly_wait(10)


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def before_tag(context, tag):
    pass


def after_step(context, step):
    if context.config.userdata.get('debug') and step.status == "failed":
        post_mortem(step.exc_traceback)


def after_tag(context, tag):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass


def setup_logger(logger_name):
    if not isdir(constants.LOG_FILE_DIR):
        makedirs(constants.LOG_FILE_DIR)

    with open(constants.LOGGER_CONFIG, 'rt') as f:
        options = load(f)

    config.dictConfig(options)
    return getLogger(logger_name)
