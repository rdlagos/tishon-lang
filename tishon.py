##########################
# TOKENS    
##########################
DIGITS = '0123456789'

PLUS_TT = 'PLUS'
MINUS_TT = 'MINUS'
DIV_TT = 'DIVIDE'
MUL_TT = 'MULTIPLY'
INT_TT = 'INT'
FLOAT_TT = 'FLOAT'
LPAR_TT = 'LPARENT'
RPAR_TT = 'RPARENT'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: 
            return f'{self.type}:{self.value}'
        return f'{self.type}'
##########################
# POSITION 
##########################

class Position:
    def __init__(self, i, ln, col, fn, ftxt):
        self.i = i 
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt 

    def advance(self, current_char):
        self.i += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col += 0

        return self

    def copy(self):
        return Position(self.i, self.ln, self.col, self.fn, self.ftxt)


##########################
# ERROR 
##########################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result
       
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'IllegalCharError', details)
        

##########################
# LEXER
##########################

class Lexer: 
    def __init__(self, fn, text):
       self.text = text
       self.pos = Position(-1, 0, -1, fn, text)                # starts at -1 because advance increments right away
       self.current_char =  None
       self.advance()               # call advance on init of Lexer Object

    def advance(self):
        self.pos.advance(self.current_char)
        if self.pos.i < len(self.text):
            self.current_char = self.text[self.pos.i]
        else:
            self.current_char = None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            # soace or tabs just advance through 
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(PLUS_TT))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS_TT))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV_TT))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL_TT))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAR_TT))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAR_TT))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self): 
        # decide if the num is an int or float
        num_str = ''
        dot_cnt = 0
        
        # block to capture floats - just look for the dot
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_cnt == 1:
                    break
                else:
                    dot_cnt  += 1
                    num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        # block to capture int
        if dot_cnt -- 0:
            return Token(INT_TT, int(num_str))
        else:
            return Token(FLOAT_TT, float(num_str))
            
##########################
# RUN    
##########################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error