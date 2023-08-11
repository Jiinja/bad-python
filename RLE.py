import re
(n, l, o) = ('', 0, ' '*79)
for c in "".join(open('PC-POW.txt', 'r').read().split()):
  if c == '\\' or c == '-': (o, l, p) = (' '*79, 0, print(o)) if c == '\\' else (o, 0, 0)
  else: n += c.replace('#', '"').replace('^', ':')
  if n and not c.isdigit():
    (v, s, n) = (re.findall(r'(\d+)(.+)', n)[0] if re.search(r'\d', n) else ('1', n)) + ('',)
    (o, l) = (o[0:l] + s * int(v) + o[l+int(v):79], l + int(v)) if s != ']' else (o, l + int(v))
