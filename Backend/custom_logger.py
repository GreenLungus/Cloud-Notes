import logging

class CustomLogger:
    def __init__(self, logger_name:str="Custom_Logger"):
        # create logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
         # create console handler and set level to debug
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        # create formatter
        self.formatter = logging.Formatter(f"#### {logger_name}(%(asctime)s) %(levelname)s --> [ %(message)s ]-END-LOG ", "%d-%m-%Y %H:%M:%S")
        # add formatter to ch
        self.console_handler.setFormatter(self.formatter)
        # add ch to logger
        self.logger.addHandler(self.console_handler)


# Only for testing purpose
if __name__ == "__main__":
    Logger = CustomLogger()

    # "application" code
    Logger.logger.debug("debug message")
    Logger.logger.info("info message")
    Logger.logger.error("error message")
    Logger.logger.critical("critical message")