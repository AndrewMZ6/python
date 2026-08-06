import threading
from time import sleep


def long_blocking_task():
	print(f'executing long blocking task in the thread "{threading.current_thread().name}"')
	sleep(3)
	print(f'long blocking task is over')

t1 = threading.Thread(target=long_blocking_task)
t1.start()
t2 = threading.Thread(target=long_blocking_task)
t2.start()

print(f'doing stuff in the thread "{threading.current_thread().name}"')
print(f'currently active threads = {threading.active_count()}')

for i in range(5):
	print(f'range {i}')
	sleep(0.2)

t1.join()
t2.join()
print('End propcess')


# executing long blocking task in the thread "Thread-1 (long_blocking_task)"
# executing long blocking task in the thread "Thread-2 (long_blocking_task)"
# doing stuff in the thread "MainThread"
# currently active threads = 3
# range 0
# range 1
# range 2
# range 3
# range 4
# long blocking task is over
# long blocking task is over
# End propcess