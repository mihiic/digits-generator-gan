import time
import sys


def update_progress(progress):
    sys.stdout.write('\r[{0}{1}] {2}%'.format('#' * int(progress), ' ' * (100 - progress), progress))


for i in range(0, 101):
	update_progress(int(i))
	time.sleep(0.2)

print("\nHello World!")

