s = ""
n = 5
while n > 0:
  n -=1
  if (n%2) == 0:
    continue
    
  a = ["A","B","C"]
  while a:
    s += str(n) + a.pop(0)
    if len(a) < 2:
      break
    