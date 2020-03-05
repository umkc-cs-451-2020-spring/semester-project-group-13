from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "scheduling_app/home.html")

def database(request):
    return render(request, "scheduling_app/database.html", {'title': 'Database'})

def generate(request):
    return render(request, "scheduling_app/generate.html", {'title': 'Generate'})