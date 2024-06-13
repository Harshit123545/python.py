#! python
def lexicographic_perms(a: str):
  pool = list(a)
  n = len(pool) # The number of distinct objects
  last = n - 1
  
  if n <= 1:
    return a # return the same string if n is less than 1
  yield ''.join(i for i in pool) # output the first permutation as itself
  while last:
  j = last - 1

  # Find the largest j such that pool[j] can be increased
  while pool[j] >= pool[j + 1]:
      j = j - 1
      
  if j < 0:
  break
  # Increase pool[j] by the smallest feasible amount
# in this case pool[i] is the smallest element greater than
# pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
i = last
while pool[j] >= pool[i]:
    i = i - 1

pool[j], pool[i] = pool[i], pool[j]
# Reverse pool[j+1] ... pool[n]
# Find the lexicographically least way to extend the new
# pool[0]...pool[j] to a complete pattern
k = j + 1
l = last
while k < l:
    pool[k], pool[l] = pool[l], pool[k]
    k = k + 1
    l = l - 1
  
print(''.join(c for c in pool))