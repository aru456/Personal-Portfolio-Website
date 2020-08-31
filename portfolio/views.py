from django.shortcuts import render
from .models import education,achievements,experience,home,contact,students

def index(request):
    things = home.objects.all()
    things2 = education.objects.all()
    things3 = experience.objects.all()
    things4 = contact.objects.all()
    things5 = achievements.objects.all()
    things6 = students.objects.all()




    return render( request, 'portfolio/index.html',{'homethings':things ,'educationthings':things2 ,'contactthings':things4,'achievementthings':things5,'experiencethings':things3, 'studentthings':things6    } )


