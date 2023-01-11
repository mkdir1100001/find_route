from django.shortcuts import render

def home(request):
    context = {
        'project': 'project',
    }
    return render(request, 'home.html', context)
