from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def upload(request):
    if request.method == 'POST':
        return render(request, 'results.html')
    
    return render(request, 'upload.html')

def identification_result(request):
    if request.method == 'POST':
        return render(request, 'results.html')
    return render(request, 'upload.html')