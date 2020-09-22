text = "X-DSPAM-Confidence:    0.8475";
x=text.find('0')
pos=text[23:29]
pos=float(pos)
print(pos)
