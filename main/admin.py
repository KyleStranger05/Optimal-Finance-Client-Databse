from django.contrib import admin
from .models import IndividualClass, CompanyClass

# Register your models here.
class IndividualAdmin(admin.ModelAdmin):
    pass

admin.site.register(IndividualClass, IndividualAdmin)

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(CompanyClass, CompanyAdmin)