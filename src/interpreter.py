class Interpreter:
    def __init__(self, ast):
        self.ast = ast

        self.environment = {}
=======
>>>>>>> c07e21a (Обновена първа фаза + тест)

    def run(self):
        output = []
        for node in self.ast:
            if node[0] == "PRINT":
                value = self.evaluate(node[1])
                output.append(f"Извеждане: {value}")
            elif node[0] == "RETURN":
                value = self.evaluate(node[1])
                output.append(f"Върната стойност: {value}")
                break  # Прекъсване при върната стойност (като return в програма)
        return output

    def evaluate(self, value):
        # Число
        if value.isdigit():
            return int(value)
        # Стринг (в кавички)
        elif value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        # Други стойности (планирано – променливи)
        else:
            return value

# ======= Пример за тестване ==========
if __name__ == "__main__":
    from parser import simple_tokenize, Parser

    code = '''
дейба
    чурки "Здравей, свят!"
    майнатаму 42
майкаму
'''
    tokens = simple_tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    result = interpreter.run()

    for step in result:
        print(step)
=======
                output.append(node[1])
            elif node[0] == "RETURN":
                output.append(f"Връща стойност: {node[1]}")
        return output
>>>>>>> c07e21a (Обновена първа фаза + тест)
