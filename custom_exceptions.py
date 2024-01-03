class CustomErrorMessage(Exception):
    def __init__(self):
        message = "My custom error message"
        super().__init__(message)        