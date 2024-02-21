
def solution(sticker):
    answer = 0
    if len(sticker) <= 3: return max(sticker)
    arr1 = [sticker[0],sticker[0]]
    arr2 = [sticker[1],max(sticker[1],sticker[2])]
    for i in range(2,len(sticker)-1):
        arr1.append(max(arr1[i-1],arr1[i-2]+sticker[i]))
    for i in range(2,len(sticker)-1):
        arr2.append(max(arr2[i-1],arr2[i-2]+sticker[i+1]))
    return max(arr1[-1],arr2[-1])