if __name__ == "__main__":
    string_text=input("Veuillez entrer une chaine de caractère")
def longeur(string_text,lenth_string=0):
    try:
        string_text[lenth_string]
        lenth_string+=1
        lenth_string=longeur(string_text,lenth_string)
        return lenth_string
    except IndexError:
        return lenth_string
if __name__ == "__main__":
    print(longeur(string_text))