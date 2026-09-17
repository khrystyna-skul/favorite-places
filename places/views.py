import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place


def index(request):
    places = Place.objects.all()
    random_place = None

    if 'random' in request.GET and places.exists():
        places_list = list(places)
        weights = [p.rating for p in places_list]
        random_place = random.choices(places_list, weights=weights, k=1)[0]

    return render(request, 'places/index.html', {'random_place': random_place})


def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return render(request, 'places/place_detail.html', {'place': place})


def add_place(request):
    errors = {}
    data = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        place_type = request.POST.get('type', '').strip()
        location = request.POST.get('location', '').strip()
        rating_raw = request.POST.get('rating', '').strip()
        image = request.FILES.get('image')

        if not name:
            errors['name'] = 'Назва не може бути порожньою.'

        try:
            rating = int(rating_raw)
            if rating < 1 or rating > 5:
                errors['rating'] = 'Рейтинг має бути цілим числом від 1 до 5.'
        except (ValueError, TypeError):
            errors['rating'] = 'Введіть коректне ціле число від 1 до 5.'

        data = {
            'name': name,
            'description': description,
            'type': place_type,
            'location': location,
            'rating': rating_raw
        }

        if not errors:
            Place.objects.create(
                name=name,
                description=description,
                type=place_type or 'Розваги',
                location=location,
                rating=rating,
                image=image
            )
            return redirect('place_list')

    return render(request, 'places/add_place.html', {'errors': errors, 'data': data})

def edit_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    errors = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        place_type = request.POST.get('type', '').strip()
        location = request.POST.get('location', '').strip()
        rating_raw = request.POST.get('rating', '').strip()
        image = request.FILES.get('image')

        if not name:
            errors['name'] = 'Назва не може бути порожньою.'

        try:
            rating = int(rating_raw)
            if rating < 1 or rating > 5:
                errors['rating'] = 'Рейтинг має бути від 1 до 5.'
        except (ValueError, TypeError):
            errors['rating'] = 'Введіть ціле число від 1 до 5.'

        if not errors:
            place.name = name
            place.description = description
            place.type = place_type or 'Розваги'
            place.location = location
            place.rating = rating
            if image:
                place.image = image
            place.save()
            return redirect('place_detail', place_id=place.id)

    return render(request, 'places/edit_place.html', {'place': place, 'errors': errors})
