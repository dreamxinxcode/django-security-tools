from django.shortcuts import render

def admin_honeypot(request):
    return render(request, 'django-security-tools/index.html')

def admin_custom(request):
    pass

def admin_form_view(request):
    if request.method == 'POST':
        pass