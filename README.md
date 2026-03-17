<<<<<<< HEAD
# 📚 Test Platformasi

Interaktiv test platformasi - foydalanuvchilarga turli fanlar bo'yicha testlar topshirish imkonini beruvchi zamonaviy veb-ilova.

## ✨ Xususiyatlar

### 🔐 **Foydalanuvchi Tizimi**
- Ro'yxatdan o'tish va tizimga kirish
- Shaxsiy profil sahifasi
- Xavfsiz autentifikatsiya

### 📝 **Test Tizimi**
- Ko'p fanlar bo'yicha testlar (Matematika, Fizika, Kimyo, Biologiya, Informatika, Tarix, Geografiya, Adabiyot)
- Tasodifiy savol tartibi
- To'g'ri/noto'g'ri javob analizi
- Batafsil natijalar

### ⏰ **Timer Funksiyasi**
- Har bir test uchun vaqt chegarasi
- Real-time taymer
- Vaqt tugaganda avtomatik yakunlash

### 🤖 **AI Tahlili**
- Google Gemini API orqali avtomatik tahlil
- Shaxsiy maslahatlar va tavsiyalar
- Test natijalari bo'yicha AI xulosasi

### 📊 **Natijalar**
- Foizli ko'rsatkichlar
- Progress circle vizualizatsiya
- Batafsil javob tahlili
- Tavsiyalar bo'limi

## 🛠️ Texnologiyalar

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **AI**: Google Gemini API
- **Authentication**: Django内置认证系统
- **Deployment**: Gunicorn + Nginx (production)

## 📋 Talablar

- Python 3.8+
- Django 4.2+
- Google Gemini API kaliti

## 🚀 O'rnatish

### 1️⃣ **Repozitoriyani klonlash**
```bash
git clone <repository-url>
cd testplatform
```

### 2️⃣ **Virtual muhit yaratish**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3️⃣ **Packagelarni o'rnatish**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Muhit o'zgaruvchilari**
`.env` faylini yarating:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5️⃣ **Migratsiyalar**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Superuser yaratish**
```bash
python manage.py createsuperuser
```

### 7️⃣ **Serverni ishga tushirish**
```bash
python manage.py runserver
```

## 📁 Loyiha Tuzilishi

```
testplatform/
├── authentication/          # Autentifikatsiya
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── quiz/                    # Asosiy test tizimi
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── testplatform/           # Django sozlamalari
│   ├── settings.py
│   └── urls.py
├── static/                 # CSS, JS, rasmlar
├── templates/              # Asosiy shablonlar
├── manage.py
├── requirements.txt
└── README.md
```

## 🎯 Foydalanish

### **Admin uchun:**
1. `/admin` ga kiring
2. Fanlar, mavzular va savollarni qo'shing
3. Test vaqtini sozlang

### **Foydalanuvchi uchun:**
1. Ro'yxatdan o'ting
2. Fan va mavzuni tanlang
3. Testni boshlang
4. Taymer tugishini kuting
5. Natijalarni ko'ring

## 🔧 Sozlamalar

### **Gemini API:**
1. [Google AI Studio](https://aistudio.google.com/) ga kiring
2. API kalitini oling
3. `.env` fayliga qo'shing

### **Test Vaqti:**
- Admin panelda mavzuning `duration_minutes` maydonini o'zgartiring
- Default: 15 daqiqa

## 🌐 Online Deployment

### **Heroku:**
```bash
# Heroku CLI o'rnatish
heroku create
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

### **PythonAnywhere:**
1. Account yaratish
2. Web app qo'shish
3. Code yuklash
4. WSGI konfiguratsiyasi

### **VPS (DigitalOcean/Vultr):**
```bash
# Gunicorn o'rnatish
pip install gunicorn

# Nginx konfiguratsiyasi
sudo nginx -t
sudo systemctl restart nginx
```

## 📸 Ekran Rasmlari

### Bosh Sahifa
![Bosh sahifa](screenshots/home.png)

### Test Jarayoni
![Test](screenshots/quiz.png)

### Natijalar
![Natijalar](screenshots/results.png)

## 🤝 Hamkorlik

1. Repozitoriyani fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. O'zgarishlarni commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Branchga push qiling (`git push origin feature/AmazingFeature`)
5. Pull request yarating

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi - [LICENSE](LICENSE) faylini ko'ring.

## 👻 Mualliflar

- **[Ismingiz]** - *Initial work* - [YourUsername]

## 🙏 Minnatdorchilik

- [Django](https://www.djangoproject.com/) - Web framework
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
- [Google Gemini](https://ai.google.dev/) - AI API
- [Font Awesome](https://fontawesome.com/) - Ikonlar

## 📞 Aloqa

Agar savollaringiz bo'lsa:
- Email: your.email@example.com
- Telegram: @your_username

---

⭐ Agar loyiha foydali bo'lsa, repozitoriyaga yulduz qo'ying!
=======
# testp
online test platformasi maktab o'quvchilari uchun
>>>>>>> dece92bc0f3675b23277a4a731f4809bbedfdb3c
