from django.contrib import admin
from users import models
# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Menu)