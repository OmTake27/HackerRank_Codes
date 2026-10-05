#print highest second last element in the array
n = int(input())
arr =list(set(map(int, input().split())))
arr.sort()
runner_up=arr[-2]
print(runner_up)
