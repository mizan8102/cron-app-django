import logging

logger = logging.getLogger(__name__)
logger=logging.getLogger('django')


def my_function():
    logger.info('call my function ')
    # logger.error('An error occurred.')
    print("hdl")


def print_hello():
    print("hello world")
    logger.info('call hello world function .')
    # logger.error('An error occurred.')
