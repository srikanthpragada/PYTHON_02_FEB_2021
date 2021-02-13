names = ["  Abc Xyz", "      Xyz A", "Abc    ", "    Bdf   Pqr"]

for s in sorted(names):
    print(s)

for s in sorted(names, key=lambda st: st.replace(" ", '')):
    print(s)

for s in sorted(map(lambda st: st.replace(" ", ''), names)):
    print(s)
