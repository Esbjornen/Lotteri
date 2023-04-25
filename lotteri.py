import random 

class Lotteri:
    def _init__(self):
        self.list_vinster = [
        "1200 Vbucks" ,
        "Sebbes Flensost",
        "Elliotts Punghår",
        "Maxs Vcard",
        "Pansarvagn",
        "Nocco Juicy Melba",
        "Lana Rhoades Onlyfans i en månad",
        "Youtube premium4life",
        "Manal",
        "Banan",
        "Iphone 5+",
        "BajsAPA",
        "Gitarr",
        "Funäsdalen",
        "Kiwi",
        "Melon",
        "citron",
        "Cykel"
        "Örjan Lax",
        "500 kr",
        ]

    def get_vinst(self):
        slumptal = random.randint(0,20)
        return self.list_vinster[3]
    
