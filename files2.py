inp = input("enter file name:")
fh = open(inp)
count=0
for i in fh:

    if not i.startswith("X-DSPAM-Confidence:") :
        continue
    print(i)
    t=i.find('0')
    num=float(i[t:])
    count=count+1
    num=num+num
avg=num/count
print(avg)
