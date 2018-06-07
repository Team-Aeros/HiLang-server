from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Token)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(ExerciseType)
admin.site.register(Exercise)
admin.site.register(WordListQuestion)
admin.site.register(SentenceStructureQuestion)
admin.site.register(SentenceStructureOption)
