from threading import Thread
import time

value = 0

def testfunc(val):
    
    global value
    local_value = value
    local_value += 1
    value = local_value
    time.sleep(val+1)
    print(f'Thread {val} valmis!', flush=True)

threads = []
for i in range(3):
    thread = Thread(target=testfunc, args=(i,))
    thread.start()  # Käynnistä thread
    threads.append(thread)

for index, thread in enumerate(threads):
    print(f'Joining thread {index}')
    thread.join()   # Odota thredia

print(f'{value=}')