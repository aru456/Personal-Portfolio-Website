from django.contrib import admin
from .models import education,students
from .models import home
from .models import experience

from .models import achievements
from .models import contact

admin.site.register(education)
admin.site.register(home)
admin.site.register(experience)

admin.site.register(achievements)
admin.site.register(contact)
admin.site.register(students)
