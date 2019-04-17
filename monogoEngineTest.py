from mongoengine import *
DBName = "tumblelog"
connect(DBName)

class User(Document):
    email = StringField(max_length=100)
    first_name = StringField(max_length=50)
    second_name = StringField(max_length=50)

# define embedded document
class Comment(EmbeddedDocument):
    content = StringField()
    name =  StringField(max_length=50)

class Post(Document):
    title = StringField(max_length = 100)
    ## if the reference is delete, delete the post auto
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    ##store the tags as a Strings directly within the post
    tags = ListField(StringField(max_length=30))
    ##store comments
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {"allow_inheritance":True}

class TextPost(Post):
    content = StringField(max_length=200)

class ImagePost(Post):
    image_link = StringField(max_length=100)

class Linkpost(Post):
    link_post = StringField(max_length=100)

ross = User(email = "ross@google.com", first_name='ross', second_name = 'pick')

