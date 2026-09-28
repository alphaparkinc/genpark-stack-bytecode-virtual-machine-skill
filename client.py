"""Stack-Based Bytecode Virtual Machine Engine
100% Python Standard Library.
"""

class StackVM:
    """Stack virtual machine execution engine."""
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.ip = 0

    def run(self, bytecode):
        self.stack = []
        self.ip = 0
        while self.ip < len(bytecode):
            inst = bytecode[self.ip]
            op = inst[0]

            if op == "LOAD_CONST":
                self.stack.append(inst[1])
            elif op == "STORE_VAR":
                self.variables[inst[1]] = self.stack.pop()
            elif op == "LOAD_VAR":
                self.stack.append(self.variables[inst[1]])
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif op == "MUL":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
            elif op == "DIV":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a / b)
            elif op == "JUMP_IF_ZERO":
                val = self.stack.pop()
                if val == 0:
                    self.ip = inst[1]
                    continue
            elif op == "HALT":
                break
            self.ip += 1

        return {
            "result": self.stack[-1] if self.stack else None,
            "variables": self.variables,
            "stack_depth": len(self.stack)
        }
