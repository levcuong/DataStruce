def fib(n):
  if (n == 1 or n == 2):
    return 1
  else:
    result = fib(n-1) + fib(n-2)
  return result

print(fib(100))