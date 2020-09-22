count=dict()
fh = input(' ')
line=open(fh)
words = line.read().split()

print(words)
print('counting.....')
for word in words:
    count[word]=count.get(word,0)+1
print("count",count)
