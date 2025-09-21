import sys

# This defines a new exception type that extends the Python's built in "Exception"
class CustomException(Exception):
     # This will initiate - human readable error message and original exception
    def __init__(self, message:str, error_details:Exception=None):
        self.error_message= self.get_detailed_error_message(message, error_details)
        super().__init__(self.error_message)

    @staticmethod # Will get most recent custom exception.
    def get_detailed_error_message(message, error_details):
        _, _, exc_tb= sys.exc_info()
        file_name= exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number= exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_details} | File: {file_name} | Line: {line_number}"
    def __str__(self):
        return self.error_message