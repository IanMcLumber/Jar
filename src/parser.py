import re
from typing import List, Tuple

# ===== Token клас =====
class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

# ===== Минимален лексер за тестване на parser =====
def simple_tokenize(code: str) -> List[Token]:
    token_specification = [
        ("KEYWORD", r"\b(дейба|майкаму|чурки|шейба|ебиго|майнатаму)\b"),
        ("NUMBER", r"\b\d+\b"),
        ("STRING", r"\".*?\""),
        ("IDENTIFIER", r"\b[а-яА-Я_][а-яА-Я0-9_]*\b"),
        ("OPERATOR", r"[+\-*/=<>!]+"),
        ("SKIP", r"[ \t\n]+"),
        ("MISMATCH", r".")
    ]
    tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specification)
    tokens = []
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Трагичен символ: {value}")
        else:
            tokens.append(Token(kind, value))
    return tokens

# ===== Парсър за ЖАР код =====
=======
from typing import List, Tuple
from lexer import Token

>>>>>>> c07e21a (Обновена първа фаза + тест)
class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0

    def current(self) -> Token:
        return self.tokens[self.position] if self.position < len(self.tokens) else Token("EOF", "")

    def consume(self) -> Token:
        token = self.current()
        self.position += 1
        return token

<<<<<<< HEAD
    def expect(self, type_: str) -> Token:
        token = self.consume()
        if token.type != type_:
            raise SyntaxError(f"Очаквах {type_}, но получих {token.type}")
        return token
=======
    def match(self, type_: str) -> bool:
        return self.current().type == type_
>>>>>>> c07e21a (Обновена първа фаза + тест)

    def parse(self) -> List[Tuple[str, str]]:
        ast = []
        if self.current().value == "дейба":
            self.consume()
            while self.current().value != "майкаму":
                if self.current().value == "чурки":
                    self.consume()
                    value = self.consume()
                    ast.append(("PRINT", value.value))
                elif self.current().value == "майнатаму":
                    self.consume()
                    value = self.consume()
                    ast.append(("RETURN", value.value))
                else:
                    raise SyntaxError(f"Непозната конструкция: {self.current().value}")
            self.consume()  # край
        else:
            raise SyntaxError("Програмата трябва да започва с 'дейба'")
        return ast
<<<<<<< HEAD

# ===== Тест пример =====
if __name__ == "__main__":
    code = '''
дейба
    чурки "Здравей, свят!"
    майнатаму 42
майкаму
'''
    tokens = simple_tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST резултат:")
    for node in ast:
        print("  →", node)
=======
>>>>>>> c07e21a (Обновена първа фаза + тест)
