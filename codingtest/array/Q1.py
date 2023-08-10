'''
입력: nums = [2, 7, 11, 15], target = 9 l 출력: [0, 1]
'''
import sys



def bruteforcing(nums,target):
    length=len(nums)
    for i in range(length):
        for j in range(i):
            number=nums[i]+nums[j]
            if number==target:
                return [i,j]
            
def twopointer(nums,target):
     i=0
     j=len(nums)-1
     nums.sort()
     while i<j:
        number=nums[i]+nums[j]
        if number==target:
            return [i,j]
        elif number<target:
            i+=1
        elif number>target:
            j-=1
        else:
            return None


            
if __name__=="__main__":
    nums=list(map(int,input().split()))
    target=int(input())
    print(twopointer(nums,target))
    print(bruteforcing(nums,target))