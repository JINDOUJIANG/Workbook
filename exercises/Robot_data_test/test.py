import numpy as np

list_assem = []
list_time_a = []
with open("../datasets/assem.txt", "r") as file: 
  for data in file:
    data_assem = data.split() 
    a = data_assem[0]
    b = data_assem[1]
    c = data_assem[2]
    d = data_assem[3]
    e = data_assem[4]
    f = data_assem[5]
    g = data_assem[6]
    list_assem.append(data_assem)
with open("../datasets/time_a.txt", "r") as file:
  for line in file:
    data_time_a = line.split() 
    i = data_time_a[0]
    j = data_time_a[1]
    k = data_time_a[2]
    list_time_a.append(data_time_a)

list_combine = []
for index in range(len(list_assem)):
  if a <= i: 
    print(a + j + k + b + c + d + e + f + g)
  else: 
    print(a,j+,k+,b,c,d,e,f,g)
