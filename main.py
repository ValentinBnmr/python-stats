serie_user_input = "1"
serie = []

class Stats:
    def __init__(self,s,effectif=0):
        self.s = s
        self.effectif = effectif
        self.Affichage()
      
    
    def Moyenne(self):
        x = 0
        for i in range(len(self.s)):
            x += self.s[i]
        moyenne =  round(x/len(self.s),2)
        return moyenne
    
    def Etendue(self):
        maxi = self.s[0]
        min = self.s[0]
        for i in self.s:
            if i >= maxi:
                # print("i =" + str(i)) "Comprendre le boucle *"
                maxi = i
            if i <= min:
                # print("i =" + str(i)) "*"
                min = i
        etendue = maxi - min 
        return etendue
    
    def Mediane(self):
        serie_mediane = []
        for i in self.s:
            serie_mediane.append(i)
        serie_mediane.sort()
        position_mediane = int(len(serie_mediane)/2)
        mediane = serie_mediane[position_mediane]
        return mediane
    
    def Variance(self):
        moy = self.Moyenne()
        variance = 0
        for i in self.s:
            variance += (i - moy)**2
        return variance
    
    def Affichage(self):
        moyenne = self.Moyenne()
        etendue = self.Etendue()
        mediane = self.Mediane()
        variance = self.Variance()
        choice_user = ""

        while choice_user == "" or not(choice_user == '1' or choice_user == '2' or choice_user == "3" or choice_user == "4" or choice_user == "ALL" or choice_user == "all"):
            choice_user = input("Choississez quel caractère statistique vous voulez : \n Moyenne : TAPER 1 \n Étendue : TAPER 2 \n Médiane = TAPER 3 \n Variance = TAPE 4 \n Pour tous les caractères : TAPER ALL \n : ")
        print(f"La serie S = {self.s}")
        if choice_user == "1":
            print(f"La moyenne est de : {moyenne}")
        elif choice_user == "2":
            print(f"L'étendue est de : {etendue}")
        elif choice_user == "3":
            print(f"La médiane est de : {mediane}")
        elif choice_user == "4":
            print(f"La variance est de : {variance}")
        else: 
            print(f"La moyenne est de : {moyenne}")
            print(f"L'étendue est de : {etendue}")
            print(f"La médiane est de : {mediane}")
            print(f"La variance est de : {variance}")

            
    


        


while serie_user_input != "":
    serie_user_input = input("Rentrez votre série statistique (ENTRER pour quitter) : ")
    if(serie_user_input != ""):
        serie_user_input_int = int(serie_user_input)
        serie.append(serie_user_input_int)


Stats(serie)


