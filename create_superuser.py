import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imayass.settings')
django.setup()

from accounts.models import CustomUser

def create_superuser():
    if not CustomUser.objects.filter(email='admin@imayass.com').exists():
        CustomUser.objects.create_superuser(
            username='admin',
            email='admin@imayass.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print('Superuser created successfully!')
    else:
        print('Superuser already exists.')

if __name__ == '__main__':
    create_superuser()
