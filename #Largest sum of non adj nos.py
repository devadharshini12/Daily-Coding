#Largest sum of non adj nos
def maxRes(arr,i):
    if(i==0):
        return arr[i]
    if(i==1):
        return max(arr[i-1], arr[i])
    else:
        return max(maxRes (arr,i-1), arr[i]+maxRes (arr,i-2))