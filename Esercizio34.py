numeri=[1,2,3,4,5,6,7,8,9, 10]
num=[[x*y for x in range (1,11)]for y in range(1,10)]
for k in range(1,10):
    tabelline=[k* num for num in numeri]
    print(tabelline)
print(num[3][5])