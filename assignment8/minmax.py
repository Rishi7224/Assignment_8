
def find_max_min(numbers):

  if len(numbers) == 0:
    return None, None

  max_num = numbers[0]
  min_num = numbers[0]

  for num in numbers:
    if num > max_num:
      max_num = num
    if num < min_num:
      min_num = num 
  if max_num is not None and min_num is not None:
   print("The maximum number is:", max_num)
   print("The minimum number is:", min_num)    
lst = [3, 1, 4, 2, 5]
find_max_min(lst)
     