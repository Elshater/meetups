from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    meetups=[
        {'title':'first Meetup',},
        {'title':'second Meetup',},
        {'title':'third Meetup',},
        ]
    return render(request,'meetups/index.html',{
        'show_meetups':True,
        'meetups': meetups
    })