from threading import Thread
import threading
def print_numbers():
    for n in range(1,26):
        print(f'Child {n}')


print("In Main!")
t = Thread(target =print_numbers)
t.start()

print(f"No. of threads : {threading.active_count()}")

for n in range(1, 26):
    print(f'Main {n}')