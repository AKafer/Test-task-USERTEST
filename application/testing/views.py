from django.shortcuts import render


def testing(request):
    return render(request, 'index.html')