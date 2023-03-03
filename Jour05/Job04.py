from Job03 import longeur


def number_Max(number_list):
    if longeur(number_list)>1:
        if number_list[0]>=number_list[1]:
            del number_list[1]
        else:
            del number_list[0]
        number_list=number_Max(number_list)
        return number_list
    else:
        return number_list[0]
def input_number(number_list=None):
    if number_list is None:
        number_list = []
    nombre = input("Veuillez entrer une liste de nombre")
    try:
        nombre=int(nombre)
        number_list.append(nombre)
        number_list=input_number(number_list)
        return number_list

    except ValueError:
        return number_list


number_list=input_number()
print(number_Max(number_list))

