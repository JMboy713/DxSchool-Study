# # n=int(input())
# # dp=[0 for i in range(n+1)]

# # dp[1]=1
# # dp[2]=1

# # for i in range(3,len(dp)):
# #     dp[i]=dp[i-1]+dp[i-2]
# # print(dp)
         
# n=int(input())

# if n==1 or n==2:
#     print(1)
# else:
#     a=1
#     b=1
#     for i in range(3,n+1):
#         result=a+b
#         b=a
#         a=result
#     print(result)
    

import functools
@functools.lru_cache()



def pibonnacci(n:int)-> int:
    if n==1 or n==2:
        return 1
    return pibonnacci(n-1)+pibonnacci(n-2)
pibonnacci.__doc__="재귀를 이용한 피보나치 수열"




help(pibonnacci)
    