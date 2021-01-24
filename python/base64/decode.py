import base64
import sys
print(sys.argv)
with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "wb") as o:
        line = f.readline()
        while line:
            buf = base64.b64decode(line.encode('utf-8'))
            print(buf)
            o.write(buf)
            line = f.readline()