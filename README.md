# Favorite Places 

Вебзастосунок на **Django** для ведення особистого каталогу улюблених місць (парки, заклади, локації для відпочинку) із можливістю перегляду детальної інформації, завантаження власних зображень, оцінювання та інтерактивного вибору випадкового місця.

---

## Функціонал

* **Перегляд каталогу:** список усіх доданих місць із картками, рейтингом у вигляді зірочок та коротким описом.
* **Детальна сторінка:** повна інформація про локацію, категорію, дату додавання та фотографію.
* **Редагування:** додавання нових місць через форму та можливість редагування вже існуючих карток.
* **Випадковий вибір:** вибір місця для відвідування на основі рейтингу (чим вищий рейтинг, тим вищий шанс випадання).
* **Медіафайли:** підтримка завантаження зображень.

---

## Технології

* **Python 3.10+**
* **Django 5.x**
* **SQLite3** 
* **Pillow** 
* **HTML5 / CSS3 / Django Templates**

---

## Інструкція із запуску проєкту

### 1. Клонування репозиторію

```bash
git clone [https://github.com/YOUR_USERNAME/favorite-places.git](https://github.com/YOUR_USERNAME/favorite-places.git)
cd favorite-places

```

### 2. Створення та активація віртуального середовища

* **Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1

```


* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



### 3. Встановлення залежностей

```bash
pip install -r requirements.txt

```

### 4. Застосування міграцій бази даних

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Заповнення бази даних початковими даними (Seed Data)

Для заповнення бази тестовими місцями виконайте скрипт:

```bash
python seed_data.py

```

### 6. Створення облікового запису адміністратора (опціонально)

```bash
python manage.py createsuperuser

```

### 7. Запуск локального сервера

```bash
python manage.py runserver

```

Після запуску перейдіть у браузері за адресою: http://127.0.0.1:8000/

---

## Структура проєкту

```text
favorite-places/
├── media/               
├── myplaces/           
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── places/              
│   ├── migrations/
│   ├── templates/     
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── seed_data.py         
├── requirements.txt   
└── README.md

```
