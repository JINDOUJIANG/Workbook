
# global vars
primary_list = []
secondary_list = []
file_list = []

# How to read a file
with open("data/primary.txt", "r") as file: 
  for data in file:
    # print(data)
    primary_list.append(data.split())
    

# How to read a file
with open("data/secondary.txt", "r") as file: 
  for data in file:
    # print(data)
    secondary_list.append(data.split())
    

# loop through angles
for angles in primary_list:

  # loop through the direction
  for direction in secondary_list:  

    # compare direction to angle
    if float(direction[0]) >= float(angles[0]):

      # insert columns
      angles.insert(1, direction[1])
      angles.insert(2, direction[2])

      # append to file list
      file_list.append(angles)
      break

    
# How to write a file
with open('data/results.txt', 'w') as file:
    for data in file_list:      
      file.write(' '.join(data) + "\n")
