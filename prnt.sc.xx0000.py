#prnt.sc/aa0000 v0.1 by smithmule
import webbrowser  
import time

lets = "aa"
nums = 1323

while True:
    #print("http://prnt.sc/"+lets+str(nums))
    url = 'http://prnt.sc/'+lets+str(nums)
    print(url)
    webbrowser.open(url, new=2, autoraise=True)
    time.sleep(1)
    nums += 1
    if nums > 9999:
        nums = 1111
        lets = ab