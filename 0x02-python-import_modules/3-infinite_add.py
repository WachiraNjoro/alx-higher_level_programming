#!/usr/bin/python3
if __name__ == "__main__":
    import sys
output = 0
for n in range(1, len(sys.argv)):
    output += int(sys.argv[n])
    print("{}".format(output))
