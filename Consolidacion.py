
name_list = ["Harry Houdini", "Newton", "David Blaine", "Hawking"
             , "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Creando lista de magos
magos_list = [name_list[0],name_list[2],name_list[5]]

# Creando lista de Cientificos
scientist_list = [name_list[1],name_list[3],name_list[6]]

#  Creando lista de others
others = [name_list[7],name_list[8],name_list[4]]


#  creando funcion Hacer Grandioso()

def hacer_grandioso():
    for mago in magos_list:
        print(f" El Gran {mago}") 

def imprimir_nombres():
    for name in range(len(name_list)):
        print(name_list[name])


hacer_grandioso()
imprimir_nombres()
print(name_list)   
print(magos_list)
print(scientist_list)
print(others)


    

    


