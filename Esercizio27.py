x=[2,4,15,5,6,13]
max=x[0]
min=x[0]
for num in x:
    if(num> max):
        max=num
    if(num< min):
        min=num
print(f"Maggiore: {max} Minimo: {min}")
    