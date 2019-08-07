from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json


def index(request):
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('index/riverhackathon-firebase-adminsdk-skacy-05a1506cdc.json')
    # Initialize the app with a service account, granting admin privileges

    if not len(firebase_admin._apps):
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://riverhackathon.firebaseio.com/'
        })

    ref = db.reference("/Report")
    snap = ref.get()

    data = []

    for key, val in snap.items():
        for x in val:
            data.append(val[x])

    print(data)
    context = {
        "data": data
    }

    return render(request, "index/index.html", context)
