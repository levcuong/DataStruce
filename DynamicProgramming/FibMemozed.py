def fib(n, memo):  
  if memo[n] != None:
    return memo[n]
  if n == 1 or n == 2:
    result = 1
  else:
    result = fib(n-1, memo) + fib(n-2, memo)
  memo[n] = result
  return result

memo  = [None] * 1001

print(fib(995, memo))
