from django.contrib import admin
from multilingual_model.admin import TranslationInline
from modules.models import Module, ModuleTranslation


class ModuleTranslationInline (TranslationInline):
    model = ModuleTranslation

class ModuleAdmin (admin.ModelAdmin):
    inlines = [ModuleTranslationInline]

admin.site.register (Module, ModuleAdmin)

