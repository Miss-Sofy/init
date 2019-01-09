from django.contrib import admin
from .models import User,Document,Hobby,Sport,Social_Media_accounts_name,Question,Mentor,Course,Event,Scholarship,Trainings_classe,Success_storie,Extra

# Register your models here.

admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Scholarship)
admin.site.register(Trainings_classe)
admin.site.register(Success_storie)
admin.site.register(Extra)
admin.site.register(Document)
admin.site.register(Question)
admin.site.register(Hobby)
admin.site.register(Sport)
admin.site.register(Social_Media_accounts_name)


