op=open("text.txt","r")
se=input("Enter the word: ")
if se== "Hello"in op.read():
    print("found hello")
elif se== "konichiwa" in op.read():
    print("found konichiwa")
elif se=="bonjour"in op.read():
    print("found bonjour")
else:
    print("not found")
