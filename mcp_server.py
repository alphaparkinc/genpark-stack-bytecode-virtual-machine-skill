import sys
import json
from client import StackVM

def main():
    vm = StackVM()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "run":
            code = [tuple(inst) for inst in params.get("bytecode", [])]
            res = {"result": vm.run(code)}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
