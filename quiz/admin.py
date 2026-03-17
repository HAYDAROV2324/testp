from django.contrib import admin
from .models import Subject, Topic, Question


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'slug', 'created_at', 'updated_at')
    list_filter = ('subject', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'subject__name')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('subject')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text_short', 'topic', 'correct_answer', 'created_at', 'updated_at')
    list_filter = ('topic__subject', 'topic', 'correct_answer', 'created_at', 'updated_at')
    search_fields = ('question_text', 'topic__name', 'topic__subject__name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('topic', 'question_text', 'correct_answer')
        }),
        ('Variantlar', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d')
        }),
        ('Vaqt belgilari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def question_text_short(self, obj):
        return obj.question_text[:50] + '...' if len(obj.question_text) > 50 else obj.question_text
    question_text_short.short_description = 'Savol matni'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('topic__subject')
