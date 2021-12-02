######################################
# IMPORT
######################################
from PYTHON.System.color import Color


# class 'Warning' is used for display the warn
class Warning:

    def __init__(self, warning_type, index):
        self.warning_type = warning_type
        self.index = index
        self.Warning = {
            "salut": []
        }

        print(Color(txt=self.Warning.get(self.warning_type)[self.index]).yellow())