TT_VAR = {}
ERROR_CODE = False

class Data:

    def GET_var(self, value=None):
        if value  is not None:
            return TT_VAR[value]
        return TT_VAR

    def POST_var(self, key, value):
        TT_VAR[key] = value