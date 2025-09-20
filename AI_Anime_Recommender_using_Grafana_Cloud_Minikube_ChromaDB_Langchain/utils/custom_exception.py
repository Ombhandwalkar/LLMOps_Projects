import sys

class CustomException(Exception):
    def __init__(self, message:str, error_details:Exception=None):
        self.error_message= self.get_detailed_error_message(message, error_details)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_details):
        _, _, exc_tb= sys.exc_info()
        file_