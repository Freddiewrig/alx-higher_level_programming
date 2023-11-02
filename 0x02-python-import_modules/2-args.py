#!/usr/bin/python3
import sys
if __name__ == "__main":
    argc = len(sys.argv) - 1
    # Subtract 1 to exclude the script name
    args = sys.argv[1:]
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} {'argument' if argc == 1 else 'arguments'}:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
