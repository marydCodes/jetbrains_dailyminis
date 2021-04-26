msg = input() # HlAdghmcXnt
key = int(input()) # 256

keyByte = (key).to_bytes(2, "little")
keyByteSum = keyByte[0] + keyByte[1]

decoded = []
for i in msg:
    temp = ord(i) + keyByteSum
    decoded.append(chr(temp))

print("".join(decoded))