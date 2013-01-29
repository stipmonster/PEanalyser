import os
import sys

print "/Users/Erik/sources/tor/Tor Browser/App/tor.exe"
print "========================================================="
path=os.path.join(os.path.dirname(os.path.abspath(__file__))+ "/plugins")
sys.path.append(path)
for file in os.listdir(path):
    if file.split(".").count("py"):
        file2= file.split(".")[0]
        test = __import__(file2)
        test.start("/Users/Erik/sources/tor/Tor Browser/App/tor.exe")
        print "========================================================="