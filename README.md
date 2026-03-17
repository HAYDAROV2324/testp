# Test Platformasi - Interaktiv Test Tizimi

adinparol
admin
admin123



Django (Backend) va HTML/Tailwind CSS (Frontend) yordamida yaratilgan interaktiv test platformasi.

## Xususiyatlari

- **Fanlar tizimi**: Fanlarni yaratish va boshqarish
- **Mavzular**: Har bir fanga tegishli mavzular
- **Testlar**: 4 variantli savollar bilan test tizimi
- **Natijalar**: Test natijalarini foiz ko'rinishida ko'rish
- **Admin panel**: Django Admin orqali oson boshqaruv
- **Responsive design**: Mobil qurilmalarga mos UI

## Texnologiyalar

- **Backend**: Django 6.0+
- **Database**: SQLite (o'zgartirish mumkin)
- **Frontend**: Django Templates, Tailwind CSS (CDN)
- **JavaScript**: Interaktiv test jarayoni uchun

## O'rnatish

1. Virtual muhitni yarating:
```bash
python -m venv venv
```

2. Virtual muhitni faollashtiring:
```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Kerakli paketlarni o'rnatish:
```bash
pip install django psycopg2-binary python-decouple
```

4. Migratsiyalarni bajaring:
```bash
python manage.py migrate
```

5. Superuser yarating:
```bash
python manage.py createsuperuser
```

6. Serverni ishga tushiring:
```bash
python manage.py runserver
```

## Ma'lumotlar Modeli

### Subject (Fan)
- `name`: Fan nomi
- `slug`: URL uchun slug

### Topic (Mavzu)
- `subject`: Fanga bog'langan (ForeignKey)
- `name`: Mavzu nomi
- `slug`: URL uchun slug

### Question (Savol)
- `topic`: Mavzuga bog'langan (ForeignKey)
- `question_text`: Savol matni
- `option_a`, `option_b`, `option_c`, `option_d`: 4 ta variant
- `correct_answer`: To'g'ri javob (a, b, c, d)

## Funksionallik

### Foydalanuvchi qismi
1. **Bosh sahifa**: Barcha fanlar ro'yxati
2. **Mavzular**: Tanlangan fanga tegishli mavzular
3. **Test jarayoni**: Interaktiv test yechish
4. **Natijalar**: Test natijalari va batafsil ko'rish

### Admin qismi
- Fanlarni qo'shish va tahrirlash
- Mavzularni boshqarish
- Savollarni qo'shish va tahrirlash
- Barcha ma'lumotlarni ko'rish

## URL Strukturasi

- `/` - Bosh sahifa (fanlar ro'yxati)
- `/subject/<slug>/` - Fanga tegishli mavzular
- `/quiz/<slug>/start/` - Testni boshlash
- `/quiz/question/` - Savol ko'rsatish
- `/quiz/submit/` - Javob yuborish (AJAX)
- `/quiz/result/` - Test natijalari
- `/admin/` - Admin panel

## Namunaviy ma'lumotlar

Namunaviy ma'lumotlarni yaratish uchun:
```bash
python manage.py create_sample_data
```

Bu quyidagilarni yaratadi:
- 3 ta fan (Matematika, Fizika, Informatika)
- 6 ta mavzu
- 15+ ta savol

## Sozlamalar

### Database o'zgartirish

`settings.py` faylida database konfiguratsiyasini o'zgartiring:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testplatform_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static files

Production uchun static files ni sozlash:

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Rivojlantirish

### Yangi funksiyalar qo'shish

1. **Foydalanuvchi tizimi**: Ro'yxatdan o'tish, login
2. **Test vaqti**: Har bir test uchun vaqt cheklovi
3. **Statistika**: Foydalanuvchi statistikasi
4. **Kategoriyalar**: Bo'limlar va kategoriyalar
5. **Media fayllar**: Savollarga rasm/qo'shiqcha qo'shish

### Xavfsizlik

- CSRF himoyasi yoqilgan
- Admin panel xavfsizligi
- SQL injectiondan himoya (Django ORM)

## Mualliflik huquqi

© 2026 Test Platformasi. Barcha huquqlar himoyalangan.
