import random,string

print("Bienvenido a un generador de contraseñas.")
print("Elige la opción de seguridad de su contraseña")
print("1) Facil (Uso de letras mayusculas y minúsculas)")
print("2) Media (Uso de letras mayusculas y minúsculas y números.)")
print("3) Dificil (Uso de letras mayusculas y minúsculas,números y símbolos.)")
opcion=int(input("Seleccione su opción >"))
password_length = int(input("¿Cuantos caracteres desea que tenga su contraseña?: "))
charseasy='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
charsmedium='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
charshard='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
passwordeasy= random.choice(charseasy)
passwordmedium= random.choice(charsmedium)
passwordhard= random.choice(charshard)
for x in range(password_length):
    if opcion==1:
        passwordez=''
        passwordez = random.choice(charseasy)
        print(passwordez)
    elif opcion==2:
        passwormed=''
        passwordmed = random.choice(charsmedium)
        print(passwordmed)
    elif opcion==3:
        passwordhrd=''
        passwordhrd = random.choice(charshard)
        print(passwordhrd)
     

