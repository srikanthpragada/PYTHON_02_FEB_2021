st = "Programming is fun for many and for some it is not that fun"

words = {}
for word in st.split():
    if word in words:
        words[word] = words[word] + 1   # Increment count for existing word
    else:
        words[word] = 1   # First time word is encountered

print(words)

