#!/usr/bin/env python3
def reinarray(arr,fir,sen):
    if sen == len(arr):
        return arr
    else:
        if arr[fir] == arr[sen]:
            arr.remove(arr[fir])
            return reinarray(arr,fir,sen)
        else:
            return reinarray(arr,sen,sen + 1)
num = [int(x) for x in input().split(' ') if x != '']
if len(num) <= 1:
    print(len(num))
else:
    print(len(reinarray(num,0,1)))
