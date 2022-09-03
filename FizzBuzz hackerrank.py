import hashlib



def probar(n):
    prueba=True
    number=n
    tres=""
    cinco=""
    if (n%3)==0:
        tres="Fizz"
        number=""
        prueba=False
    if (n%5)==0:
        cinco="Buzz"
        number=""
        prueba=False
    if prueba:
        print(n)
    else:
        print(tres+cinco)

def fizzBuzz(n):
    # Write your code here
    for i in range (n):
        probar(i+1)
        
        
numerito=int(input("ingrese numero entero"))

fizzBuzz(numerito)
