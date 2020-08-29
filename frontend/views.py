from django.shortcuts import render

# Create your views here.
def TODOAppView(request):
    return render(request,'index.html')
