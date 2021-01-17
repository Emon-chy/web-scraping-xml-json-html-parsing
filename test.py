import re
fname=input("enter file name:")
handle=open(fname)
sum=0
for line in handle:
    line=line.rstrip()

    numstr=re.findall('[0-9]+',line)
    if len(numstr)<1:
        continue
    for i in numstr:
        numint=int(i)
        sum=sum+numint
print(sum)


    #print(num)
