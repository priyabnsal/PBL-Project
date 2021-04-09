from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "sent from view"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is hompage")

def about(request):
    return HttpResponse("this is about")
def services(request):
    return HttpResponse("this is services")
def contact(request):
    return HttpResponse("this is contact")
