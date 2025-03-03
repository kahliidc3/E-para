# E-Para - Modern Pharmacy E-Commerce Platform

<p align="center">
  <img src="staticfiles/images/logo.png" alt="E-Para Logo" width="200"/>
</p>

## 🏥 About E-Para

E-Para is a sophisticated e-commerce platform built with Django, specifically designed for online pharmacies. It offers a secure, user-friendly interface for purchasing pharmaceutical and healthcare products.

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/kahliidc3/E-para.git
cd E-para

# Set up virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
copy .env.example .env

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🌟 Key Features

### 👤 User Management
- Secure email-based authentication
- Google OAuth integration
- Medical history profiles
- Address management

### 💊 Product Catalog
- Prescription medicines
- OTC medications
- Health & wellness products
- Advanced search & filtering

### 🛒 Shopping Experience
- Real-time cart updates
- Prescription uploads
- Multiple payment options
- Order tracking

### 🔒 Security
- SSL/TLS encryption
- HIPAA compliance
- Secure payments
- Data protection

## 🛠️ Tech Stack

- **Backend**: Django 5.1, Python 3.x
- **Database**: SQLite3 (Development)
- **Authentication**: django-allauth
- **Frontend**: Tailwind CSS, Crispy Forms
- **Tools**: Git, VS Code

## 📂 Project Structure

```
E-Para/
├── accounts/          # Authentication & profiles
├── cart/             # Shopping cart
├── core/             # Core features
├── orders/           # Order processing
├── products/         # Product management
├── static/           # Assets
├── templates/        # HTML templates
└── manage.py         # Django CLI
```

## ⚙️ Environment Setup

```python
# .env configuration
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


