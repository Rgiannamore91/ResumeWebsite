from django.shortcuts import render

def base(request):
    return render(request, 'build/base.html')

def index(request):
    firstName = "Ryan"
    lastName = "Giannamore"
    context = {
        "first": firstName,
        "last": lastName,
    }
    return render(request, 'build/index.html', context)

