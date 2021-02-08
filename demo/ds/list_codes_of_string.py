s = "Hello"

codes = []
for c in s:
    code = ord(c)
    if code not in codes:
        codes.append(code)

print(codes)
