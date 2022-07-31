# challenge number 1
def sum_to(n):
  sum = 0
  for x in range(1, n, +1):
    sum += x
  return sum

# challenge number 2
def largest(nums):
  return max(nums)

print(largest([8, 6, 7, 500, 3, 0, 9]))

# challenge number 3
def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences("hiiiiiiiiiiiiiiiiii", "i"))

# challenge number 4

def product(*args):
  product = 1
  for x in args:
    product *= x
  return product

print(product(4, 0.5, 5, 6.7))