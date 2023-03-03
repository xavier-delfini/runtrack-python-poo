def dames(n):
    def array_create(n, i=n, j=n, array=[], array_two=[]):
        if n >= 3 or j != 0:
            if i != 0:
                i -= 1
                array.append("o")
                array = array_create(n, i, j, array, array_two)
                return array
            else:
                if j != 0:
                    array_two.append(array)
                    j -= 1

                    array_two = array_create(n, i, j, array, array_two)
                    return array_two
                else:
                    return array_two
        else:
            return array
    #def verif_dame(plateau,coordonnées):
        #def verif_ligne(plateau,coordonnées):
            def ligne_gauche():
            def ligne droite():
        #def verif_colonne(plateau,coordonnées):
            def colonne_haut():
            def colonne_bas():

        #def verif_diagonales(plateau,coordonnées):

    return array_create(n)


print(dames(5))
