from django.contrib import admin
from pyflora_app.models import *
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Stats
    extra = 0

class PotAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Pot, PotAdmin)
admin.site.register(Plant)
admin.site.register(Stats)