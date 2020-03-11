file = open("testfile.txt","r")
st_check = input("What are we recycling today?")
data = st_check.lower()
for x in file:
    i = 0
    if data in x:
        print(x)
    else:
        i +=1
        continue
file.close()