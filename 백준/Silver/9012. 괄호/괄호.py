import sys
brace = sys.stdin.readlines()[1:]
for b in brace:
  b = b.rstrip()
  while '()' in b:
    b = b.replace('()','')

  if b:
    print("NO")
  else:
    print("YES")