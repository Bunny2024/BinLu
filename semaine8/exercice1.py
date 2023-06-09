class Article:

    def __init__(self , reference , nom , prixHT , quantiteEnStock) :
        ## instance attributes
        print ("I am the constructor of the Article's class")
        self.__reference = reference   
        self.__nom = nom
        self.__prixHT = prixHT
        self.__quantiteEnStock = quantiteEnStock 

    @property
    def reference(self):
        return self.__reference

    @reference.setter
    def reference( self , ref ):
        self.__reference = ref 

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom( self , n ):
        self.__nom = n 
    
    @property
    def prixHT(self):
        return self.__prixHT

    @nom.setter
    def prixHT( self , p ):
        self.__prixHT = p 

    @property
    def quantiteEnStock(self):
        return self.__quantiteEnStock

    @nom.setter
    def quantiteEnStock( self , q ):
        self.__quantiteEnStock = q 
    
    def appovisionner(self, nb_article_ajoutes):
        self.quantiteEnStock =self.quantiteEnStock + nb_article_ajoutes
        print(f"La quantite devient : {self.quantiteEnStock}.")

    def vendre(self, qtv):
        if (qtv > self.quantiteEnStock) :
            print("Ventre non-reussite ( la quantite est insufusante).")
        else:
            self.quantiteEnStock  == qtv


