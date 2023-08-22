from matplotlib import pyplot as plt
from json import dumps

with open("avar1_cnt.txt", 'r') as f:
	ar1 = [float(x) for x in f.readline().strip().split()][:100000]

with open("avar2_cnt.txt", 'r') as f:
	ar2 = [float(x) for x in f.readline().strip().split()][:100000]

with open("tom_cnt.txt", 'r') as f:
	ar3 = [float(x) for x in f.readline().strip().split()][:100000]

##with open("tkt_cnt.txt", 'r') as f:
##	ar4 = [float(x) for x in f.readline().strip().split()][:100000]

with open("chir1_cnt.txt", 'r') as f:
	ar5 = [float(x) for x in f.readline().strip().split()][:100000]

with open("chir2_cnt.txt", 'r') as f:
	ar6 = [float(x) for x in f.readline().strip().split()][:100000]

with open("anna_cnt.txt", 'r') as f:
	ar7 = [float(x) for x in f.readline().strip().split()][:100000]
	
##plt.plot(list(range(len(ar1))), ar1, label="avar 1 (36 155 tokens)")
##plt.plot(list(range(len(ar2))), ar2, label="avar 2 (49 141 tokens)")
##plt.plot(list(range(len(ar3))), ar3, label="tom sawyer (76 664 tokens)")
##plt.plot(list(range(len(ar4))), ar4, label="tokita (13 337 tokens)")
##plt.plot(list(range(len(ar5))), ar5, label="chir 1 (210 274 tokens)")
##plt.plot(list(range(len(ar6))), ar6, label="chir 2 (212 291 tokens)")
##plt.plot(list(range(len(ar7))), ar7, label="anna karenina (269 580 tokens)")

plt.plot(list(range(len(ar1))), ar1, label="avar 1 (26 363 tokens)")
plt.plot(list(range(len(ar2))), ar2, label="avar 2 (26 306 tokens)")
plt.plot(list(range(len(ar3))), ar3, label="tom sawyer (26 371 tokens)")
#plt.plot(list(range(len(ar4))), ar4, label="tokita (13 337 tokens)")
plt.plot(list(range(len(ar5))), ar5, label="chir 1 (26 370 tokens)")
plt.plot(list(range(len(ar6))), ar6, label="chir 2 (26 395 tokens)")
plt.plot(list(range(len(ar7))), ar7, label="anna karenina (26 353 tokens)")
plt.ylabel('Different types of tokens')
plt.xlabel('Total no. of tokens')

plt.legend()
plt.show()
