import logging

def logger():
    logger = logging.getLogger()
    fh = logging.FileHandler('loger')
    ch = logging.StreamHandler()
    fm = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(fm)
    logger.addHandler(fh)
    logger.addHandler(ch)
    ch.setFormatter(fm)
    return logger
logger = logger()
logger.debug('log debug message')
logger.info('log info message')
logger.warning('log warning message')
logger.error('log error message')
logger.critical('log critical message')