from django.db import models
from django.utils.text import slugify


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Fan nomi")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics', verbose_name="Fan")
    name = models.CharField(max_length=100, verbose_name="Mavzu nomi")
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
        ordering = ['name']
        unique_together = ['subject', 'slug']

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions', verbose_name="Mavzu")
    question_text = models.TextField(verbose_name="Savol matni")
    option_a = models.CharField(max_length=255, verbose_name="A variant")
    option_b = models.CharField(max_length=255, verbose_name="B variant")
    option_c = models.CharField(max_length=255, verbose_name="C variant")
    option_d = models.CharField(max_length=255, verbose_name="D variant")
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('a', 'A variant'),
            ('b', 'B variant'),
            ('c', 'C variant'),
            ('d', 'D variant'),
        ],
        verbose_name="To'g'ri javob"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"
        ordering = ['id']

    def __str__(self):
        return f"{self.topic.name} - {self.question_text[:50]}..."

    def get_options(self):
        return {
            'a': self.option_a,
            'b': self.option_b,
            'c': self.option_c,
            'd': self.option_d,
        }

    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()
