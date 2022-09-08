correcta = 0

password_vault = str(input("Ingrese una contraseña alfanumérica: "))

while (correcta != 1):
    password = str(input("Ingrese la contraseña: "))
    if (password == password_vault):
        print("Contraseña correcta. Puede ingresar al sistema.")
        correcta = 1
    else:
        print("Contraseña incorrecta. Vuelva a ingresar la contraseña.")