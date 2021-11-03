from django.contrib import admin
from .models import Kijiji, News, Business, Police, Hospital,Profile

# Register your models here.
admin.site.register(Kijiji)
admin.site.register(News)
admin.site.register(Business)
admin.site.register(Police)
admin.site.register(Hospital)
admin.site.register(Profile)

