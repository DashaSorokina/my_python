with open('temp.txt','r') as file:
    degrees = file.read()
a = degrees.split()
print(a)
temp=[]
for i in a:
    temp.append(float(i))

c=0
for i in temp:
        if temp.count(i)==1:
            c=c+1
    
def average(temp):
    return round(sum(temp)/len(temp),2)

print("Максимальная:",max(temp),"Минимальная:",min(temp),"Средняя:",average(temp),"Уникальность:",c)

