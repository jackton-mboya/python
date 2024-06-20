a = 3
b = 45.8
c = "emobilis"
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

str = "Welcome to coding"
str2 = "at emobilis Training academy"
print(str[0:4])
print(str[5])
print(str+str2)  # concatenatintion

# list datatype
majina = ["Jackton", "Mercy", "Purity", "John,Caleb"]
print(type(majina))
majina[0] = "Jackton"
print(f"My name is {majina[0]}")

matunda = ("Banana", "mangoes", "pineapples", "oranges")
print(f"i like eating {matunda[2]}")  # tupledatatype

magari = ("BMW", "mercedez", "ferrari", "bugatti")
print(f"i like driving {magari[3]}")  # set datatype

print(majina)
print(matunda)
print(magari)

mydict = {"Age": 25, "salary": 100000, "gender": "male", "name":"Jackton"}
print(f"The age of the employee is {mydict['Age']}")
print(f"The salary of the employee is {mydict['salary']}")
print(f"The gender of the employee is {mydict['gender']}")
print(f"The name of the employee is {mydict['name']}")