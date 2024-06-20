# myname = "eMobilis"

# for i in myname:
#    if i == "e":
#        print(i)

jina = ['banana', 'mangoes', 'apples']

for i in range(5):
    print(i, jina[i])

try:
    # code that might raise exception
    result = 1 / 0
except ZeroDivisionError as e:
    # code to handle exception
    print(f"An exception occurred {e}")
finally:
    # code that runs no matter what
    print("This will always be printed")
