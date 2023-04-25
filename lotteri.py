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
        ]

    def get_vinst(self):
        slumtal = random.randint(0,16)
        return self.list_vinster[slumtal]
    
