from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    """
    Кастомная команда для создания супер пользователя
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='sanekzh01@gmail.com',
            first_name='Alexander',
            last_name='Rychagov',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('superkot123')
        user.save()
