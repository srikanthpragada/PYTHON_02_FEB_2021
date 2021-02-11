# Positional-only arguments  3.8 feature

def wish(message='Hi', user="Guest", /):
    print(message, user)


wish("Hello", "Scott")
# wish(message = "Hello", name = "Steve")
