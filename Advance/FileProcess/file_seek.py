import os

f = open('example.txt', 'rb')
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(1, os.SEEK_SET)
print(f.tell())
print(f.read())
f.seek(0, os.SEEK_END)
print(f.tell())
print(f.read())
f.seek(-5, os.SEEK_CUR)
print(f.tell())
print(f.read())