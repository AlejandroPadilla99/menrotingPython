from .singleton_driver import SingletonDriver

driver = None

if not driver:
    driver = SingletonDriver().driver