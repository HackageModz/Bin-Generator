import random, string
import requests
import os
from colorama import Fore





from time import sleep
import sys

line_1 = "[?] Amount of bin code"
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
    
num = input(f':')

f = open("bin-codes.txt", "a+", encoding='utf-8')

print("")

for n in range(int(num)):
    y = ''.join(random.choice(string.digits) for _ in range(5))
    f.write('4')
    f.write(y)
    f.write("\n")

f.close()
