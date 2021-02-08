s = "Hello"

codes = [ord(c) for c in s]
codes = [ord(c) for c in s if c.islower()]

print(codes)
