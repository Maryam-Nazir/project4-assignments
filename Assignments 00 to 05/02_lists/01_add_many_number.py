#Write a function that takes a list of numbers and returns the sum of those numbers.
def add_many_numbers(num):
   total = 0 
   for i in num:
      total += i
      return total
numbers:list = [1,2,3,4,5]
print(add_many_numbers(numbers))










