file = input("enter the text:")
fh = open(file)
for line in fh:
    fh=line.lower()
    print(fh)
