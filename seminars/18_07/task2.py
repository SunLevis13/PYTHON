path = r'folder\task2.txt'
with open (path,'r') as my_file:
    data = my_file.read()

data = data.split()
print(data)
data = data[:-2]
print(data)
data = [int(data[0][:-3]), int((data[1]+data[2])[:-1]), int(data[3] + data[4])]
print(data)

d = data[1]**2 - 4*data[0]*data[2]
print(d)

x_1 = (-data[1] + d**0.5)/(2*data[0])
x_2 = (-data[1] - d**0.5)/(2*data[0])

print(x_1, x_2)
