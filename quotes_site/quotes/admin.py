from django.contrib import admin
# Зареєструйте тут свої моделі
from .models import Author, Quote

admin.site.register(Author)
admin.site.register(Quote)