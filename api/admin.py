from django.contrib import admin
from api.authn.models import User
from api.doctors.models import Doctor
from api.patients.models import Patient
from api.mappings.models import Mapping

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_joined', 'is_staff', 'is_active')
admin.site.register(User,UserAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'created_at')
admin.site.register(Doctor,DoctorAdmin)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'disease', 'created_by', 'created_at')
    def created_by(self, obj):
        return obj.user.name
    created_by.short_description = 'Created By'
admin.site.register(Patient,PatientAdmin)
class MappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_at')
admin.site.register(Mapping,MappingAdmin)