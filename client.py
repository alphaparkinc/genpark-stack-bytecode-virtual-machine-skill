class StackVM:
    """
    Stack-Based Bytecode Virtual Machine.
    Executes instruction sequences with operand stack and local variable storage.
    """
    def __init__(self):
        self.stack = []
        self.locals = {}

    def run(self, bytecode):
        ip = 0
        while ip < len(bytecode):
            inst = bytecode[ip]
            op = inst[0]
            if op == "PUSH":
                self.stack.append(inst[1])
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == "MUL":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
            elif op == "STORE":
                self.locals[inst[1]] = self.stack.pop()
            elif op == "LOAD":
                self.stack.append(self.locals[inst[1]])
            elif op == "HALT":
                break
            ip += 1
        return self.stack[-1] if self.stack else None
