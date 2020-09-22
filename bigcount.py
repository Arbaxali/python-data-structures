counts=dict()
fh = input(' ')
line=open(fh)
words = line.read().split()

print(words)
print('counting.....')
for word in words:
    counts[word]=counts.get(word,0)+1
print("counts",counts)

bw=None
bc=None
for word,count in counts.items() :
    if bw is None or count > bc:
        bw=word
        bc=count
for i in counts:
    value=list()
    value=counts.values()
    largest=None
    cmp(value,)

print(bw,bc)
print("largest:",largest)
