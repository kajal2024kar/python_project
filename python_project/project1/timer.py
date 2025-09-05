import time
import os
while True:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(1)
    os.system("cls")