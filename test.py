import os
import time
while 1:
    print('等待连接中', end='')
    for i in range(6):
        print('.', end='')
        time.sleep(0.5)
    os.system('cls')

