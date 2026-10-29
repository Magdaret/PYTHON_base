'''
#Задача №1 easy "Two Sum"
nums = [2,11,7,15]
target = 11
result = []
a = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Nice!")
            result.append(nums[i])
            result.append(nums[j])
            print(result)
            break
'''
