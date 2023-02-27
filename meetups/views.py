from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    meetups=[
        {
            'title':'first Meetup', 
            'location':'New York',
            'slug':'a-first-meetup'
        },
        {
            'title':'second Meetup',
            'location':'Paris',
            'slug':'a-second-meetup'
        },
        {
            'title':'third Meetup',
            'location':'London',
            'slug':'a-third-meetup'
        },
    ]
    return render(request,'meetups/index.html',{
        'show_meetups':True,
        'meetups': meetups
    })