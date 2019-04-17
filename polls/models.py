from django.db import models
from mongoengine import *
from mysite.settings import DBNAME
connect(DBNAME)



class User(Document):
    name = StringField(max_length=100)
    email = StringField(max_length=50)

class Comment(EmbeddedDocument):
    content = StringField(max_length=200)
    author = ReferenceField(User)

class Artical(Document):
    title = StringField(max_length=50)
    content = StringField(max_length=300)
    comment = ListField(EmbeddedDocumentField(Comment))
    tags = ListField(StringField(max_length=30))





