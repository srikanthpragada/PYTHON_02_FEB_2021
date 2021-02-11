# Keyword-only arguments

def wish(*,  message='Hi', name="Guest",):
    print(message, name)


#wish("Scott","Hello")
wish(message = "Hello", name = "Steve")
