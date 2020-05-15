def fourSum( nums, target):
    result = []
    dict = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            tracker = target -( nums[i] + nums[j])
            for k in range(j + 1, len(nums)):
                if tracker - nums[k] in dict.values():
                    result.append([nums[i], nums[j], tracker - nums[k], nums[k]])
                else:
                    dict[tracker - nums[k]] = nums[k]
    return result