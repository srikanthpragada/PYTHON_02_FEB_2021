def common_chars(s1, s2):
    return "".join(set(s1) & set(s2))


print(common_chars('Abcd', 'Xdyc'))
