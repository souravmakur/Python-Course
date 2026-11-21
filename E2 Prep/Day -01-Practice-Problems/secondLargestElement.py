def secondLargest(list):
  largest = 0
  secondLargest = -1

  for nums in list:
    if nums > largest:
      secondLargest = largest
      largest = nums 
    elif nums > secondLargest and nums < largest:
      secondLargest = nums

  return secondLargest


list = [1,2,3,4,5,6,7,8]
print(secondLargest(list))