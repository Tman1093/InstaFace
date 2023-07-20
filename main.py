from User import User
import funzioni 
from Post import Post
entry=False


User_def_1 =("Giulio", "Rossi", "GiuRos", "123Abc12@", "Firenze", 33)
User.all_user["GiuRos"]= "123Abc12@"



username=" "
password=" "

funzioni.welcome_message() #stampa un messaggio di benvenuto "Benvenuto su InstaFace!" 

#creo il primo account
print("Creiamo un account!")
print("Account1:")
dic_user1 = funzioni.sign_in()   
User1= User(username=dic_user["username"],name=dic_user["name"],surname=dic_user["surname"],age=dic_user["age"],city=dic_user["city"],password=dic_user["password"])    
print("Account1 registrato con successo!\n") 

second_account = input("Vuoi creare un altro account?").lower()
if second_account=="si" or second_account=="sì":
  dic_user2 = funzioni.sign_in()
  User2= User(username=dic_user2["username"],name=dic_user2["name"],surname=dic_user2["surname"],age=dic_user2["age"],city=dic_user2["city"],password=dic_user2["password"])
  print("Account2 registrato con successo!\n")

  third_account = input("Vuoi creare un altro account?").lower()
  if third_account=="si" or third_account=="sì":
    dic_user3 = funzioni.sign_in()
    User3= User(username=dic_user3["username"],name=dic_user3["name"],surname=dic_user3["surname"],age=dic_user3["age"],city=dic_user3["city"],password=dic_user3["password"])
  print("Account3 registrato con successo!\n") 

#Fase di login
while entry is False:
  print("Log in\n") 
  username=input("Inserisci il tuo username: \n")    
  password=input("Inserisci una password: \n")    
  result_log_in= funzioni.check_log_in(username,password)      
  if result_log_in:    
    print("Login avvenuto con successo!")  
    entry= True 
  else:
    print("utente o password errati") 
if username in dic_user1:
    Current_User=User1
elif username in dic_user2:
    Current_User=User2
elif username in dic_user3:
    Current_User=User3
elif username== "GioRos":
    Current_User=User3 = User_def_1

#INIZIO CORE DEL PROGRAMMA
id_choice = False     
while id_choice is False:
  menu_choice = input("""Scegli un'azione dal menu\nMenu: \n\     
              1- Visualizza le notifiche\n\     
               2- Condividi un nuovo post\n\     
               3- Modifica un vecchio post\n\      
               4- Visita un altro profilo\n\     
               5- Manda una richiesta di amicizia\n\    
               6- Accetta una richiesta di amicizia\n\    
               6- Apri una chat\n\     
               7- Fai un upgrade a premium\n\     
               8- Gestisci la tua privacy\n\    
               Digita logout per uscire da InstaFace\n\     
               """)     
  
  #MOSTRA NOTIFICHE
  if menu_choice=="1":     
    User.show_notice(Current_User)     

  #AGGIUNGI POST
  if menu_choice=="2": 
    text_post = input("Scrivi un post: ")
    while True:
        pubblication_choice = input("""Premi 1 se vuoi pubblicare il post,\n
        2 per riscrivere il post,\n
        premi 3 per ritornare al menù principale: """)
        if pubblication_choice == "1":
            post1 = Post(text_post, Current_User)
            post1.add_post()
            print("Il post è stato pubblicato con successo!")
            break
        elif pubblication_choice == "2":
            text_post = input("Riscrivi il post: ")
        else:
            print("ciao")
            break   
  #elif menu_choice=="3":     
       #edit_post     
   #    pass     
  #elif menu_choice=="4":      
      #view_dashboard     
   #   pass     
  #elif menu_choice=="5":     
      #visit_friend()      
    #  pass     
  #elif menu_choice=="6":      
      #add_friends     
  #    pass     
  #elif menu_choice=="7":     
      #premium_upgrade      
    #  pass     
  
  #IMPOSTA PRIVACY
  elif menu_choice=="8":    
      User1.getter__profile_privacy()    
      level_privacy=input("Scegli 0 per profilo privato, 1 per profilo pubblico, 2 per lasciare il profilo inalterato: ")    
      if level_privacy=="1":    
          User1.setter__profile_privacy("Public")    
          print("Livello privacy modificato con successo")    
      if level_privacy=="0":    
          User1.setter__profile_privacy("Private")    
          print("Livello privacy modificato con successo")    
  elif menu_choice=="logout":     
                print("A presto!")     
                break     