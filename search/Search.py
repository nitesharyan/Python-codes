file=open(input("Enter a file name: "))
lines=file.readlines()
file.close()
i,j,k=0,0,0

pid=input("Enter Papaer Id for search:")
header=lines[0].strip().split(",")
for line in lines:
    if pid in line:
        for j in range(0,len(header)):
            k=line.find(",",k)
            if line[i:k]!="":
                print(header[j]+"="+line[i:k])
            i=k+1
            k=k+1
        c=input("Press enter to exit....")
        exit()
print("No such Paper ID Exists")