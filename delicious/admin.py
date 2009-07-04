from django.contrib import admin
from syncr.delicious.models import Bookmark

class DeliciousAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(DeliciousAccount, DeliciousAccountAdmin)
