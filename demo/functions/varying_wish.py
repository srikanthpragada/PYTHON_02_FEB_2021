def wish(*names, message='Hi'):
    for name in names:
        print(message, name)


wish('Van', 'Bob', 'Mike')
wish('Joe','Jack', message = "Good Bye")


