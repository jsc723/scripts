import base64
import sys
print(sys.argv)
with open(sys.argv[1], "rb") as f:
    with open(sys.argv[2], "w") as o:
        buf = f.read(8)
        print(buf)
        while buf:
            o.write(base64.b64encode(buf).decode('utf-8') + '\n')
            buf = f.read(8)
            print(buf)

        