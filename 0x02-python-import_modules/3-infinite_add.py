#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    results = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            results = results + int(arg)
    print(results)
