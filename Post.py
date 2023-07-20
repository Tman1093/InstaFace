from datetime import datetime
from User import User 
## classe POST
all_posts=[] #ROADMAP DIZIONARIO POST 
 
class Post:
    def __init__(self, text, user):
        self.text = text
        self.user = user
 
#metodo per pubblicare un post
    def add_post(self):
        global all_posts
        all_posts.append(self)