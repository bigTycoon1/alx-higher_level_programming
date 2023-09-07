#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    results = len(sys.argv) - 1

    if results == 0:
        print("{} arguments.".format(results))
    elif results == 1:
        print("{} argument:".format(results))
    else:
        print("{} arguments:".format(results))

    if results >= 1:
        results = 0
        for arg in sys.argv:
            if results != 0:
                print("{}: {}".format(results, arg))
            results = results + 1
