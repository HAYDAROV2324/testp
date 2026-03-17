from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


def login_view(request):
    """Login sahifasi"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Xush kelibsiz, {username}!')
                return redirect('quiz:home')
            else:
                messages.error(request, 'Foydalanuvchi nomi yoki parol noto\'g\'ri')
        else:
            messages.error(request, 'Formada xatolik bor. Iltimos, tekshirib ko\'ring.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authentication/login.html', {'form': form})


class RegisterView(CreateView):
    """Ro'yxatdan o'tish sahifasi"""
    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('auth:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ro\'yxatdan muvaffaqiyatli o\'tdingiz! Endi tizimga kirishingiz mumkin.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ro\'yxatdan o\'tishda xatolik yuz berdi. Iltimos, ma\'lumotlarni tekshirib ko\'ring.')
        return super().form_invalid(form)


def logout_view(request):
    """Tizimdan chiqish"""
    logout(request)
    messages.info(request, 'Tizimdan muvaffaqiyatli chiqdingiz.')
    return redirect('quiz:home')


@login_required
def profile_view(request):
    """Profil sahifasi"""
    return render(request, 'authentication/profile.html', {'user': request.user})
