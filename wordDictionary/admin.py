from django.contrib import admin
from django.contrib.admin.models import LogEntry
from wordDictionary.models import Word, Feature, Dimension, Language


# Register your models here.
admin.site.register(Word)
admin.site.register(Feature)
admin.site.register(Dimension)
admin.site.register(Language)
admin.site.register(LogEntry)