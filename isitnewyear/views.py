from django.shortcuts import render
import datetime

now = datetime.datetime.now()
isIt = "No"

if now.day == 1 and now.month == 1:
    isIt = "Yes"


# Create your views here.
def newYear(request):
    return render(request, "newyear/index.html", {
        "check": isIt
    })