file=open(input("Enter a file name: "))
lines=file.readlines()

file.close()
list1=[]
count=0
for line in lines:
    if count>0:
        list1.append(line)
    else:
        header=line
    count=1
#print(list1)
spt=int(input("Enter the number of rows you want in one file:"))
i,j=0,1
del line
del lines
g=open("output"+str(j)+".csv","w+")
g.write(header)
for item in list1:
    if i==spt:
        g.close()
        i,j=(0,j+1)
        g=open("output"+str(j)+".csv","w+")
        g.write(header)
    else:
        i+=1
        g.write(str(item)+"\n")
input("Press enter key to exit....!!!!")
