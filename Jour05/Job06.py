import copy


def dames(n, coordonnées=None, plateau=None, dames_count=0):
    if coordonnées is None:
        coordonnées = [0, 0]

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
                    array_clone=copy.copy(array)
                    array_two = array_create(n, i, j, array_clone, array_two)
                    return array_two
                else:
                    return array_two
        else:
            return array

    def verif_dame(plateau, coordonnées, n):
        def verif_ligne(plateau, coordonnées, n):
            def ligne_gauche(plateau, coordonées):
                if coordonées[1] != -1:
                    if plateau[coordonées[0]][coordonées[1]] == "o":
                        coordonées[1] -= 1
                        return ligne_gauche(plateau, coordonées)
                    else:
                        return 1
                else:
                    return 0

            def ligne_droite(plateau, coordonées, n):
                if coordonées[1] != n:
                    if plateau[coordonées[0]][coordonées[1]] == "o":
                        coordonées[1] += 1
                        return ligne_droite(plateau, coordonées, n)
                    else:
                        return 1
                else:
                    return 0

            if ligne_gauche(plateau, coordonnées) == 0 and ligne_droite(plateau, coordonnées, n) == 0:
                return 0
            else:
                return 1

        def verif_colonne(plateau, coordonnées, n):
            def colonne_haut(plateau, coordonées):
                if coordonées[0] != -1:
                    if plateau[coordonées[0]][coordonées[1]] == "o":
                        coordonées[0] -= 1
                        return colonne_haut(plateau, coordonées)
                    else:
                        return 1
                else:
                    return 0

            def colonne_bas(plateau, coordonées, n):
                if coordonées[0] != n:
                    if plateau[coordonées[0]][coordonées[1]] == "o":
                        coordonées[0] += 1
                        return colonne_bas(plateau, coordonées, n)
                    else:
                        return 1
                else:
                    return 0

            if colonne_haut(plateau, coordonnées) == 0 and colonne_bas(plateau, coordonnées, n) == 0:
                return 0
            else:
                return 1

        def verif_diagonales(plateau, coor_diag, n):
            def haut(plateau, coor_haut_d, n):
                coor = copy.copy(coor_haut_d)

                def gauche(plateau, coor):
                    if coor[0] != -1 and coor[1] != -1:
                        if plateau[coor[0]][coor[1]] == "o":
                            coor[0] -= 1
                            coor[1] -= 1
                            return gauche(plateau, coor)
                        else:
                            return 1
                    else:
                        return 0

                def droite(plateau, coor_gauche_h_d, n):
                    if (coor_gauche_h_d[0] != -1) and (coor_gauche_h_d[1] != n):
                        if plateau[coor_gauche_h_d[0]][coor_gauche_h_d[1]] == "o":
                            coor_gauche_h_d[0] -= 1
                            coor_gauche_h_d[1] += 1
                            return droite(plateau, coor_gauche_h_d, n)
                        else:
                            return 1
                    else:
                        return 0

                if gauche(plateau, coor) == 0 and droite(plateau, coor_haut_d, n) == 0:
                    return 0
                else:
                    return 1

            def bas(plateau, coor_bas_d, n):
                def gauche(plateau, coor_gauche_d_b, n):
                    if coor_gauche_d_b[0] != n and coor_gauche_d_b[1] != -1:
                        if plateau[coor_gauche_d_b[0]][coor_gauche_d_b[1]] == "o":
                            coor_gauche_d_b[0] += 1
                            coor_gauche_d_b[1] -= 1
                            return gauche(plateau, coor_gauche_d_b, n)
                        else:
                            return 1
                    else:
                        return 0

                def droite(plateau, coor_droite_d_b, n):
                    if (coor_droite_d_b[0] != n) and (coor_droite_d_b[1] != n):
                        if plateau[coor_droite_d_b[0]][coor_droite_d_b[1]] == "o":
                            coor_droite_d_b[0] += 1
                            coor_droite_d_b[1] += 1
                            return droite(plateau, coor_droite_d_b, n)
                        else:
                            return 1
                    else:
                        return 0

                coor = copy.copy(coor_bas_d)
                if gauche(plateau, coor, n) == 0 and droite(plateau, coor_bas_d, n) == 0:
                    return 0
                else:
                    return 1

            coor_diag_bas = copy.copy(coor_diag)
            if haut(plateau, coor_diag, n) == 0 and bas(plateau, coor_diag_bas, n) == 0:
                return 0
            else:
                return 1

        coordonnées_ligne = copy.copy(coordonnées)
        coordonnées_colonne = copy.copy(coordonnées)
        coordonnées_diagonales = copy.copy(coordonnées)
        if verif_ligne(plateau, coordonnées_ligne, n) == 0 \
                and verif_colonne(plateau, coordonnées_colonne, n) == 0 \
                and verif_diagonales(plateau, coordonnées_diagonales, n) == 0:
            return 0
        else:
            return 1
    if plateau == None:
        plateau = array_create(n)
    #if n>2:
    if verif_dame(plateau, coordonnées, n) == 0:
        plateau[coordonnées[0]][coordonnées[1]] = "x"
        dames_count+=1
    elif (coordonnées[0] == n - 1) and (coordonnées[1] == n - 1):
        if dames_count==n:
            return plateau
        else:
            return "Le nombre entré ne permet pas d'avoir un nombre egal de dimension et de dames"



    elif coordonnées[1] == n - 1:
        coordonnées[0] += 1
        coordonnées[1] = 0
    else:
        coordonnées[1]+=1
    plateau=dames(n,coordonnées,plateau,dames_count)
    return plateau



print(dames(8))
