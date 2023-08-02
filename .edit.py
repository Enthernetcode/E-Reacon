h = open("port_scanner.py","r")
k = h.read()
h.close()
lines = []
for l in k:
 if l[0] =! "p":
   continue
 else:
  lines.append(l)
p = open("see.py", "w")
for line in lines:
 p.write(line)
