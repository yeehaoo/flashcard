import random
import sys

def populate(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data.strip().split('\n')

def main():
    data = populate(sys.argv[1])
    random.shuffle(data)
    for i in range(len(data)):
        print(str(i+1) + "/" + str(len(data)) + ": " + data[i])
        input()

if len(sys.argv) == 1:
    print("command line argument FILE_PATH missing", file=sys.stderr)
else:
    main()
