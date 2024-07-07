#11. Read and Write into a File
f=open("bca4.txt","r")
print(f.read())
f.close()

f=open("bca4.txt","w")
f.write("we all are Best")
f.close()

f=open("bca4.txt","r")
print(f.read())
f.close()