from datetime import datetime 

class User: 
 
    #Creo una variabile di classe dizionario che associa allo username la relativa password
    all_user={}
 
    #Costruttore della classe
    def __init__(self, name, surname, username, password, city, age, profile_privacy="public"): #profile_privacy, homepage, dashboard_content, inbox, sign_in_date): 
        self.name=name  
        self.surname=surname  
        self.age=age  
        self.city=city  
        self.username=username  
        self.password=password  
        self.__profile_privacy= profile_privacy
        self.friend_list =[]
        self.friend_list_request =[]
    #Questi attributi gli ho commentati perchè non ho capito come li volevate usare, sorry:)
        #self.homepage = homepage[]
        #self.inbox= inbox 
 
    #creo un metodo di classe per modificare l' attributo di classe: all_user
    @classmethod #metodo di classe 
    def sign_in(cls,name,surname,username,password,city,age):
        #aggiunge l'utente al "database"
        cls.all_user.append([username,password,name,surname,city,age])
 
    #creo un setter per assegnare l'attributo
    def setter__profile_privacy(self,privacy_level):
        self.__profile_privacy=privacy_level
 
 
    #creo un getter per "controllare" lla privacy delk'user   
    def getter__profile_privacy(self):
        print(f"Il tuo livello di privacy è {self.__profile_privacy}")
        return self.__profile_privacy

    #mostra le notifiche dell'utente
    def show_notice(self):
        print("Notifiche: \n",self.notice)

    #aggiunge notifiche al pannello notifiche
    def add_notice(self, new_notice):
        self.notice=  self.notice.append(new_notice)

    #mostra le richieste di amicizia
    def show_friend_request_list(self):
        print(self.friend_request_list)
    
    #accetta le richieste di amicizia
    def accept_request(self, User1):
        if User1.username in self.friend_request_list:
            self.friend_list.append(User1.username)
            self.friend_request_list.remove(User1.username)
            self.add_notice(f"{User1} è stato aggiunto agli amici")

   # def add_message(self, new_message, friend_username):
    #self.inbox=  self.inbox. 