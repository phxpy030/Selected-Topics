from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Type)
admin.site.register(Produce)
