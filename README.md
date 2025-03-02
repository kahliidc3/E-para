# E-Para - Online Pharmacy E-Commerce Platform

E-Para is a modern e-commerce platform specifically designed for online pharmacy and healthcare products. Built with Django, it provides a secure and user-friendly interface for purchasing pharmaceutical and healthcare items.

## 🌟 Key Features

### User Management
- Secure email-based authentication
- Google social login integration
- Custom user profiles with medical history
- Address management for delivery

### Product Catalog
- Categorized healthcare products
- Prescription medicine section
- Over-the-counter medications
- Health and wellness products
- Product search and filtering
- Detailed product information

### Shopping Experience
- Intuitive shopping cart
- Real-time stock updates
- Prescription upload capability
- Multiple payment options
- Order tracking system

### Security & Compliance
- SSL/TLS encryption
- HIPAA compliance measures
- Secure payment processing
- Data privacy protection

## 🛠️ Technical Stack

### Backend
- Django 5.1
- Python 3.x
- SQLite3 (Development)
- django-allauth for authentication

### Frontend
- Tailwind CSS
- Crispy Forms
- Responsive design
- Mobile-first approach

### Development Tools
- Git version control
- VS Code
- Python virtual environment


## 🗂️ Project Structure

```
E-Para/
├── accounts/          # User authentication & profiles
├── cart/             # Shopping cart functionality
├── core/             # Core application features
├── orders/           # Order processing & tracking
├── products/         # Product catalog management
├── static/           # Static assets (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/        # HTML templates
├── media/           # User-uploaded content
├── requirements.txt  # Project dependencies
└── manage.py        # Django management script
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```python
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


