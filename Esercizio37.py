import random
lanciMarco=[random.randint(1,6) for num in range(10)]
lanciAlice=[random.randint(1,6) for num in range(10)]
f=open("./lanci.txt","w")
for k in range(10):
    f.write(str(lanciMarco[k])+","+str(lanciAlice[k])+"\n")
f.close()