from django.shortcuts import render
from .models import Service, Lead, Portfolio,Blog
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def pricing(request):
    services = Service.objects.prefetch_related('plans')
    return render(request, 'pricing.html', {'services': services})

def services_page(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
def portfolio_list(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def portfolio_detail(request, slug):
    project = Portfolio.objects.get(slug=slug)
    return render(request, 'portfolio_detail.html', {'project': project})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})


def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')
        phone = request.POST.get('phone')


        # Save lead
        Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            message=message
        )

        # Send email notification
        subject = f"New Lead: {name}"
        body = f"""
New lead received:

Name: {name}
Email: {email}
Phone: {phone}
Service: {service}

Message:
{message}
        """

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # your inbox
            fail_silently=False,
        )

        success = True

    return render(request, 'contact.html', {'success': success})