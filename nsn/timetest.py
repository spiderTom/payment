import time


print time.time()
print time.localtime(time.time())
print time.strftime('%Y-%m-%d',time.localtime(time.time()))
print "11111111111111111111111111111111111111"
options = time.strftime('%Y/%m',time.localtime(time.time()))
print options

