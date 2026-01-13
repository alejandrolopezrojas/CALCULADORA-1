a = input("Digite el valor de a: ")
b = input("Digite el valor de b: ")

if a.isalpha() or b.isalpha():
    print("A Y B NO PUEDEN SER O CONTENER STR")
    if a.isalpha():
        a = input("digite un nuevo valor para ""a"" que no sea un str= ")
    if b.isalpha():
        b = input("digite un nuevo valor para ""b"" que no sea un str= ")
if a.isspace() or b.isspace() or a == "" or b == "":
    print("A Y B NO PUEDEN SER O CONTENER VACIOS")
    if a.isspace() or a == "":
        a = input("digite un nuevo valor para ""a"" que no sea un vacio= ")
    if b.isspace() or b == "":
        b = input("digite un nuevo valor para ""b"" que no sea un vacio= ")

a = float(a)
b = float(b)

e_0 = "No se puede realizar esta operación si b = 0"

op = int(
    input(
        "1 = +\n"
        "2 = -\n"
        "3 = *\n"
        "4 = /\n"
        "5 = **\n"
        "6 = %\n"
        "7 = //\n"
        "Ingrese la operación que desea realizar: "
    )
)

if op < 1 or op > 7:
    print("ESTE NÚMERO NO CORRESPONDE A NINGUNA OPERACIÓN DEL SISTEMA")
    op = int(input("Ingrese una opción dentro del rango existente: "))

# SUMA
if op == 1:
    print(f"El resultado de {a} + {b} es =", a + b)

# RESTA
elif op == 2:
    print(f"El resultado de {a} - {b} es =", a - b)

# MULTIPLICACIÓN
elif op == 3:
    print(f"El resultado de {a} * {b} es =", a * b)

# DIVISIÓN
elif op == 4 and b != 0:
    print(f"El resultado de {a} / {b} es =", a / b)

# POTENCIA
elif op == 5:
    print(f"El resultado de {a} ** {b} es =", a ** b)

# MÓDULO
elif op == 6 and b != 0:
    print(f"El resultado de {a} % {b} es =", a % b)

# DIVISIÓN ENTERA
elif op == 7 and b != 0:
    print(f"El resultado de {a} // {b} es =", a // b)

else:
    if (op == 4 or op == 6 or op == 7) and b == 0:
        print(e_0)
        b = float(input("Digite un valor diferente de 0 para b: "))

        if op == 4:
            print(f"El resultado de {a} / {b} es =", a / b)
        elif op == 6:
            print(f"El resultado de {a} % {b} es =", a % b)
        elif op == 7:
            print(f"El resultado de {a} // {b} es =", a // b)
    else:
        print("Ups, ha ocurrido un error inesperado")





























