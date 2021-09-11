#prnt.sc/aa0000 v0.2 by smithmule
import webbrowser  
import time

lets = "aa"
nums = 1

while True:
    #url = 'http://prnt.sc/'+lets+str(nums)
    url = 'http://prnt.sc/'+lets+'%04d' % nums
    print(url)
    webbrowser.open(url, new=2, autoraise=True)
    time.sleep(1)
    nums += 1
    if nums > 9999:
        nums = 1111
        lets = ab
