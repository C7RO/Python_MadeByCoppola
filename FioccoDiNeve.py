f=open("./comandi.txt","w")
#snow.left(90)
for _ in range(6):
    f.write("forward:100\n")#snow.forward(100)
    f.write("left:40\n")#snow.left(40)
    f.write("forward:40\n")#snow.forward(40)
    f.write("back:40\n")#snow.back(40)
    
    f.write("right:80\n")#snow.right(80)
    f.write("forward:40\n")#snow.forward(40)
    f.write("back:40\n")#snow.back(40)

    f.write("left:40\n")#snow.left(40)
    f.write("forward:40\n")#snow.forward(40)
    f.write("back:40\n")#snow.back(40)
    

    f.write("right:60\n")#snow.right(60)
    f.write("goto:0,0\n")#snow.goto(0,0)

f.write("left:30\n")#snow.left(30)
f.write("forward:65\n")#snow.forward(65)
f.write("right:120\n")#snow.right(120)

for _ in range(6):
    f.write("forward:65\n")#snow.forward(65)
    f.write("right:60\n")#snow.right(60)

f.write("goto:0,0\n")#snow.goto(0,0)
f.close()