#  while condicion = True flase:
    
contraseña="ucagirls"
entrada=""
intentos=0
 
 while entrada! = contraseña and intentos < 3:
     entrada=input("ingrese su contraseña:")
     if entrada != contraseña: 
         print("incorrecta-siga participando:")
         intentos +=1 
    if entrada == contraseña: 
        print("correcto!!!")
        else:
            print("no hay mas intentos.")
     