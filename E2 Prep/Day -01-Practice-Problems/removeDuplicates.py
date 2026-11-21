def removeDuplicatesWithSet(nums):
  unique_nums = list(set(nums))
  return unique_nums


nums = [4, 2, 7, 2, 4, 9, 1]
print(removeDuplicatesWithSet(nums)) #does not preserve order
# Output : [1, 2, 4, 7, 9]

def removeDuplicatesWithDict(nums):
  unique_nums = list(dict.fromkeys(nums))
  return unique_nums
  
nums1 = [4, 2, 7, 2, 4, 9, 1]
print(removeDuplicatesWithDict(nums1)) #Preserves the order 

def removeDuplicatesWithSeen(nums):
  seen = set()
  unique_nums = []

  for num  in nums:
    if num not in seen:
      seen.add(num)
      unique_nums.append(num)
  return unique_nums;

nums2 = [4, 2, 7, 2, 4, 9, 1]
print(removeDuplicatesWithSeen(nums2))
