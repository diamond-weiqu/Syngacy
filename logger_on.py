import logging
from logging import handlers

logger = logging.getLogger('log')
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('[%(levelname)s][%(asctime)s]: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='./logs/bot.log', when='D',
                                                               encoding='utf-8')
time_rotating_file_handler.setLevel(logging.INFO)
time_rotating_file_handler.setFormatter(formatter)
logger.addHandler(time_rotating_file_handler)
logger.addHandler(stream_handler)
