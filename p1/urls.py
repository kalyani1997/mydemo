from rest_framework.routers import SimpleRouter
from p1.views import *
simplert = SimpleRouter()

simplert.register('patients',PatientOps)
simplert.register('doctors',DoctorOps)
simplert.register('address',AddressOps)
simplert.register('hospital',HospitalOps)
urlpatterns = simplert.urls