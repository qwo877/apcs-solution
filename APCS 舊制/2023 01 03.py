def scan_f(codes, idx):

  s = ''
  while idx < len(codes):

    if codes[idx]=='f' and codes[idx+1]=='(':
      idx += 2
      max_v, idx = scan_f(codes, idx)
      s += str(max_v)

    elif codes[idx]==')':

      # decode s
      arr = []
      for x in s.split(','):
        mul = 1
        for a in x.split('*'):
          psum = 0
          for b in a.split('+'):
            psum += int(b)

          mul *= psum

        arr.append(mul)

      idx += 1
       
      return max(arr)-min(arr), idx

    else:
      s += codes[idx]
      idx += 1


codes = input() #sys.stdin.readlines()[0]

s1 = ''
idx = 0
while idx < len(codes):

  if codes[idx]=='f' and codes[idx+1]=='(':
    idx +=2
    v, idx = scan_f(codes, idx)
    s1 += str(v)
  else:
    s1 += codes[idx]
    idx += 1

# +- before *

mul = 1
for a in s1.split('*'):
  psum = 0
  for b in a.split('+'):
    psum += int(b)

  mul *= psum

print(mul)