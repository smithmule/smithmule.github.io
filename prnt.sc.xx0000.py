#prnt.sc/aa0000 v0.4 by smithmule and github copilot
import random
import time
import webbrowser

# create a string of two random letters in a variable called letters
letters = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 2))
numbers = 1

for i in range(0, 20):
    url = 'http://prnt.sc/'+letters+'%04d' % numbers
    print(url)
    #open url in the same tab
    webbrowser.open(url, new=0)
    numbers += 1
    time.sleep(1)
    if numbers > 9999:
        letters = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 2))
        nums = 1