import logging

logging.basicConfig(filename='test_logs.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)

disable_loggers = ['urllib3.connectionpool','faker.factory']

def pytest_configure():
    for logger_name in disable_loggers:
        logger_not = logging.getLogger(logger_name)
        logger_not.disabled = True
