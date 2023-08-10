# # with open("./0714/log.txt","r") as logfile:
# #     log=logfile.readlines()
# #     count=0
# #     for i in log:
# #         a=i.split(' ')
# #         if a[8]=='200':
# #             count+=1
# # print(count)


with open("./0714/log.txt","r") as logfile:
    count=0
    ssum={}
    for i in logfile:
        a=i.split(' ')
        try:
            if int(a[-1])<0:
                 raise Exception("not a plus integer")
            ssum[a[0]]=ssum.get(a[0],0)+int(a[-1])
        except:
        	continue
for ip in ssum:
    print(ip," : ",ssum[ip])


# import re

# with open("./0714/log.txt","r") as logfile:
#     count=0
#     ssum={}
#     for i in logfile:
#         a=i.split(' ')
#         num=re.sub('/n','',a[-1])
#         try:
#             ssum[a[0]]=ssum.get(a[0],0)+int(num)
#         except:
#         	continue
# for ip in ssum:
#     print(ip," : ",ssum[ip])

# counter module 을 이용한 풀이.
from collections import Counter

