from client import StackVM

def main():
    vm = StackVM()
    code = [
        ("LOAD_CONST", 7),
        ("LOAD_CONST", 3),
        ("ADD",),
        ("STORE_VAR", "x"),
        ("LOAD_VAR", "x"),
        ("LOAD_CONST", 4),
        ("MUL",),
        ("HALT",)
    ]
    res = vm.run(code)
    print("Stack Bytecode VM Verification:")
    print(f"Execution Result: {res['result']} (Expected: 40)")
    print(f"Final Variables: {res['variables']}")

if __name__ == "__main__":
    main()
