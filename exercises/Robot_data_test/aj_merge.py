
# Dataset_1 header = Time, joint-angles
# Dataset_2 header = Time, Task, State


# if "7" < "70":
#   print("less than")
# else:
#   print("greater than")




assem_list = []
time_list = []

with open("../datasets/primary.txt", "r") as file: 
  for data in file:
    # print(data)
    angles_line = data.split() 
    assem_list.append(angles_line)
    

# with open('primary.txt', 'w') as file:
#     for assem in assem_list:      
#       result = ""
#       for i in range(5):
#       # for angles in assem:
#         result += assem[i] + "  "
        
#       file.write(str(result) + "\n")



with open("../datasets/time_a.txt", "r") as file: 
  for data in file:
    # print(data)
    time_line = data.split() 
    time_list.append(time_line)
    # pass


print_flag = False
for assem in reversed(assem_list):

  is_found = False

  for time in time_list:
    if float(assem[0]) <= float(time[0]):
      # print(assem[0] + " " + time[0])
      assem.insert(1, time[1])
      assem.insert(2, time[2])

      is_found = True
      break

  if is_found == False:
    assem_list.remove(assem)


with open('results.txt', 'w') as file:
    for assem in assem_list:      
      result = ""
      for angles in assem:
        result += angles + " "
        
      file.write(str(result) + "\n")
