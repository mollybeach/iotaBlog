from django.contrib import admin
from .models import Post, employee, client, Users

# Register your models here.
admin.site.register(Post)
admin.site.register(employee)
admin.site.register(client)
admin.site.register(Users)