import prestamo
edad = int(input("ingresa tu edad: "))
anios_antiguedad =int(input("ingrese su antiguedad de empleo: "))
salario_mensual = int(input("ingrese su salario mensual: "))

if edad >= 25 and edad <= 60:
    if salario_mensual >= 30000:
        if anios_antiguedad>= 2:
            print("Prestamo aprovado!")
        else:
            print("antiguedad insuficiente.")
    else:
        print("salario fuera del rango.")
else:
    print("edad fuera del rango.")
