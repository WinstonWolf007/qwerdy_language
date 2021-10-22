#############################
# CONSTANT
#############################
DIGITS = "0123456789"

#############################
# ERROR
#############################

class Error:
    def __init__(self, pos_start, pos_end, error_name, error_detail):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.error_detail = error_detail

    def as_string(self):
        result = f'{self.error_name}: {self.error_detail}'
        result += f"\nFile '{self.pos_start.find}', line {self.pos_start.line + 1}"
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Characters', details)


#############################
# POSITION
#############################

class Position:
    def __init__(self, index, line, colone, find, find_txt):
        self.index = index
        self.line = line
        self.colone = colone
        self.find = find
        self.find_txt = find_txt

    def advance(self, current_char):
        self.index += 1
        self.colone += 1

        if current_char == '\n':
            self.line += 1
            self.colone = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.colone, self.find, self.find_txt)



#############################
# TYPE
#############################
TT_INT = "INT"
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_LOW = "LOW"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_RPARENT = "PARENT_RIHT"
TT_LPARENT = "PARENT_LEFT"

##############################
# TOKEN
##############################
class Token:
    def __init__(self, var_type, var_value=None):
        self.var_type = var_type
        self.var_value = var_value

    def __repr__(self):
        if self.var_value: return f'{self.var_type}:{self.var_value}'
        return f'{self.var_type}'

##############################
# LEXER
##############################

class Lexer:
    def __init__(self, find, text):
        self.find = find
        self.text = text
        self.pos = Position(-1, 0, -1, find, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def makeToken(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_LOW))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPARENT))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPARENT))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + ".":
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

#############################
# RUN
#############################

def run(find, text):
    lexer = Lexer(find, text)
    tokens, error = lexer.makeToken()
    return tokens, error