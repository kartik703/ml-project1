import logging
import sys
def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script {file_name}, line {exc_tb.tb_lineno}: {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(error)
        self.error_message = error_message_detail(error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(filename='example.log', level=logging.INFO)  # Configure logging
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException("Divide by zero error occurred", e)
