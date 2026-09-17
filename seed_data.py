import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myplaces.settings')
django.setup()

from places.models import Place

PLACES_DATA = [
    {
        'name': 'Парк КПІ',
        'description': 'Затишний парк для прогулянок та відпочинку біля університету.',
        'type': 'Парки',
        'location': 'м. Київ, Берестейський проспект',
        'rating': 5,
        'image_name': 'парк кпі.jpg',
    },
    {
        'name': 'Парк Кіото',
        'description': 'Парк з алеєю сакур та традиційним японським садом.',
        'type': 'Парки',
        'location': 'м. Київ, вул. Кіото',
        'rating': 4,
        'image_name': 'парк кіото.jfif',
    },
    {
        'name': 'Парк Наталка',
        'description': 'Сучасний парк на Оболонській набережній з чудовим видом на Дніпро.',
        'type': 'Парки',
        'location': 'м. Київ, Оболонська набережна',
        'rating': 5,
        'image_name': 'парк наталка.jpg',
    },
    {
        'name': 'Парк Шевченка',
        'description': 'Центральний міський парк, популярне місце для зустрічей.',
        'type': 'Парки',
        'location': 'м. Київ, вул. Терещенківська',
        'rating': 5,
        'image_name': 'парк шевченка.jfif',
    },
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'places', 'images')


def seed():
    for item in PLACES_DATA:
        img_path = os.path.join(IMAGES_DIR, item['image_name'])

        place, created = Place.objects.get_or_create(
            name=item['name'],
            defaults={
                'description': item['description'],
                'type': item['type'],
                'location': item['location'],
                'rating': item['rating'],
            }
        )

        if created and os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                place.image.save(item['image_name'], File(f), save=True)
            print(f"Додано: {place.name}")
        else:
            print(f"Пропущено або вже існує: {item['name']}")


if __name__ == '__main__':
    seed()