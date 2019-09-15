from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index),

    path('addperson/',addPerson),
    path('getperson/',getPerson),
    path('updateperson/',updatePerson),
    path('deleteperson/',deletePerson),
    path('addPB/',addPB),
    path('getPB/',getPB),
    path('updatePB/',updatePB),
    path('deletePB/',deletePB),

    path('mtmadd/',manytomanyadd),
    path('mtmget/',manytomanyget),
    path('mtmupdate/',manytomanyupdate),
    path('mtmdelete/',manytomanydelete),

    path('polymerization/',polymerization),

    path('ftest/',Ftest),
    path('qtest/',Qtest)
]