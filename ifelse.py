mark = int(input("Enter a Marks: "))
if mark >= 80 and mark <= 100:
   print("You have an A")
elif mark >= 60 and mark <= 79:
   print("You have a B")
elif mark >= 40 and mark <= 59:
   print("You have a C")
elif mark >= 0 and mark <= 49:
   print("You have a D")
else:
   print("Wrong inputs, check your marks")

