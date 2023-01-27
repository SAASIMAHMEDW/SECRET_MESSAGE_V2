#st = "oracle is game"
st = "oracle is game"
print(st)
words = st.split()
print(words)
choice = input("enter choice:").upper()
if choice=="Y":
    newst = []
    for word in words:
    #print(word)
        if len(word)>=3:
            r1 = "ksh"
            r2 = "gss"
            nword = r1 + word[1:] + word[0] + r2
      #  print (nword)
            newst.append(nword)
        else:
           #  word = word[::-1]
             newst.append(word[::-1])
             #print(word)         
    print(" ".join(newst))
else:
    newst=[]
    for word in words:
        if len(word)>=3:
            nword = word[3:-3]
            nword = nword[-1] + nword[:-1]
            newst.append(nword)
        else:
           newst.append(word[::-1])
    print(" ".join(newst))
           # print(nword)