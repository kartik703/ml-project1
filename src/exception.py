import sys
from src.logger import logging  # Make sure src.logger.logging exists

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script [{file_name}] line number [{exc_tb.tb_lineno}] error message: {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        # Some code that may raise an exception
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("An error occurred")
        raise CustomException("An error occurred", sys.exc_info())
