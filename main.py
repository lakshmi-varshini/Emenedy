import os

# def printFile(c, fileName):
#   a_file = open("./" + c + "/" + fileName + ".txt")
#   lines = a_file.readlines()

#   for line in lines:
#     print(line)

#printFile("hair care", "hair remedies")
print("Welcome to Emenedy, your home remedy hub!")
name = input("Name: ")
password = input("Password: ")

# with open("hair remedies.txt", "w+") as file:
#    for line in file:
#      print(line)


# a_file = open("./" + c + "/" + fileName + ".txt")

# lines = a_file.readlines()
# for line in lines:
#     print(line)

print("\nHi,", name)
categories = input("What types of remedies do you want to see? Options: sore throat & cough, skin care, hair care, headaches, body pain\n")
categories = categories.split(", ")
print()

# prints what files are there in directory
for c in categories:
  try:
    for file in os.listdir(c):
      # printFile(c, file)
      # print(file)
      a_file = open("./" + c + "/" + file)
      lines = a_file.readlines()
      for line in lines:
        print(line)
    print()
  except(FileNotFoundError):
    print(c, "is not a valid entry.\n")
  

# for i in categories:
#  print(i)