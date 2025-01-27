import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from .models import HoneypotAdminLog

# Set up a logger for honeypot activity
logger = logging.getLogger('honeypot')

def admin_honeypot(request):
    return render(request, 'django-security-tools/index.html')


def honeypot_login(request):
    if request.method == 'POST':
        ip = get_client_ip(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        timestamp = now()

        # Log the information
        logger.warning(f"HONEYPOT TRIGGERED: IP={ip}, Username={username}, Password={password}, Time={now()}")

        login_attempt = HoneypotAdminLog.objects.create(ip=ip, username=username, password=password, timestamp=timestamp)

        # Send a generic response (e.g., invalid credentials message)
        return render(request, 'django-security-tools/index.html')

    # Render the fake login page
    return render(request, 'django-security-tools/index.html')  # Use a decoy login template

def get_client_ip(request):
    """Get the client's IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
