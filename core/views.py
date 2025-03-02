from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from products.models import Product, Category

# Create your views here.

def home(request):
    featured_products = Product.objects.filter(available=True)[:6]
    skin_types = dict(Product.SKIN_TYPE_CHOICES)
    skin_concerns = dict(Product.CONCERN_CHOICES)
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'skin_types': skin_types,
        'skin_concerns': skin_concerns,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Send email
        email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=email_message,
                from_email=email,
                recipient_list=['support@e-para.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('core:contact')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
            
    return render(request, 'core/contact.html')

def privacy_policy(request):
    return render(request, 'core/privacy.html')

def terms_of_service(request):
    return render(request, 'core/terms.html')
