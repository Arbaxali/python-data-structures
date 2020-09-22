count=dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for lines in handle:
    if lines.startswith("From ") :
        words=lines.split()
        count[words[1]]=count.get(words[1],0)+1
print(count)
i = None
j = None

for k, v in count.items():
    if j is None or j < v:
        j = v
        i = k
print(i, j)


       
