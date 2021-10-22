class ERROR:
    def __init__(self, error_type, error_detail, error_suggestion=None):
        self.type = error_type
        self.detail = error_detail
        self.info = error_suggestion

    def __str__(self):
        if self.info is None:
            return "\033[91m" + f"[{self.type}]: {self.detail}" + "\033[0m"
        else:
            return "\033[91m" + f"[{self.type}]: {self.detail} == {self.info}" + "\033[0m"
