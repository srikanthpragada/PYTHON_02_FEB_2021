def wish(name, message='Hello'):
    print(f"{message} {name}")


# Positional parameters
wish('Van', 'Hi')
wish('Bob')

# keyword arguments
wish(message='Hello', name='Steve')
wish(name='Scott')
