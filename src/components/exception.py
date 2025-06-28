import sys

def error_msg_detail(error,detail:sys):
    exc_type, exc_value, exc_tb = sys.exc_info()
    error_message = f"Error: {error}\nDetail: {detail}"
    return error_message

class CustomException(Exception):
    def __init__(self, error, detail:sys):
        super().__init__(error_msg_detail(error, detail))
        self.error = error
        self.detail = detail

    def __str__(self):
        return f"{self.error} - {self.detail}"