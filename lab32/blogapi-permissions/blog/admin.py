from django.contrib import admin
from .models import Article
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    list_display=["title","date_created","updated","published"]


admin.site.register(Article,AdminArticle)