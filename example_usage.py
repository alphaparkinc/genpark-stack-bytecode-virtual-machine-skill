from client import StackVM

def main():
    print("=== Testing Stack Bytecode Virtual Machine ===")
    vm = StackVM()
    bytecode = [
        ("PUSH", 5),
        ("STORE", "x"),
        ("LOAD", "x"),
        ("PUSH", 10),
        ("ADD",),
        ("HALT",)
    ]
    res = vm.run(bytecode)
    print("Execution output:", res)
    assert res == 15
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
