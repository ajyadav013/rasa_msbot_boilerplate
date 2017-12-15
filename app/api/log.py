import logging


class Logger(object):
    def getLoggingLevel(self, level):
        # logging level works with int values which are specified above. this
        # function converts user level to actual value of logging.
        loggingLevel = {
            'logging.CRITICAL': 50,
            'logging.ERROR': 40,
            'logging.WARNING': 30,
            'logging.INFO': 20,
            'logging.DEBUG': 10
        }
        return int(loggingLevel[level])

    def loggingObject(
            self,
            file_path,
            logging_level='logging.DEBUG',
            logging_format="""%(asctime)s %(levelname)s %
            (lineno)d %(process)d %(message)s"""):
        try:
            level = self.getLoggingLevel(logging_level)
            log_formatter = logging.Formatter(logging_format)
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(log_formatter)
            logger = logging.getLogger(__name__)
            logger.setLevel(level)
            logger.addHandler(file_handler)
            return logger
        except Exception as e:
            return e
