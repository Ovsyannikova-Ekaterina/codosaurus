from django.contrib import admin
from .models import Parent, Child, Teacher, Course, Topic, Lesson, Application

# Кастомизация отображения в админ-панели
class ChildInline(admin.TabularInline):
    model = Child
    extra = 1

class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline]
    list_display = ('name', 'description', 'time', 'price', 'level')
    search_fields = ('name', 'level')

class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline, ApplicationInline]
    list_display = ('name', 'email', 'phone', 'relation')
    search_fields = ('name', 'email')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email')
    search_fields = ('name', 'email')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'time_start', 'time_end', 'topic', 'teacher')
    list_filter = ('date', 'teacher')
    search_fields = ('topic__name',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description')
    search_fields = ('name', 'course__name')

# Регистрация моделей и их админ-классов
admin.site.register(Parent, ParentAdmin)
admin.site.register(Child)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Application)
