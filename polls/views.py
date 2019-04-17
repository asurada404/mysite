from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Artical, Comment
from django.views.generic import View
#Create your views here.

import json

# CONNECT MONGO
from mysite.settings import DBNAME
from pymongo import MongoClient
client = MongoClient()
db = client[DBNAME]
post = db.post.find_one()

def index(request):
    return HttpResponse('hello world')






def calculate(request):
    formula = request.GET['formula']
    try :
        res = eval(formula,{})
    except:
        res = "error"
    res_json = {"res":res}
    return HttpResponse(json.dumps(res_json),content_type="application/json")


