import os
import sys
import pefile


print sys.argv[1]
print "========================================================="
path=os.path.join(os.path.dirname(os.path.abspath(__file__))+ "/plugins")
sys.path.append(path)
pe =  pefile.PE(sys.argv[1])
for file in os.listdir(path):
    if file.split(".").count("py"):
        file2= file.split(".")[0]
        test = __import__(file2)
        test.start(sys.argv[1],pe)
        print "========================================================="