from rest_framework import routers

from SGBproject import views as sgb_views

router = routers.SimpleRouter()

router.register(r'SGB', sgb_views.SGBView, basename="south_german_bank_rendered")
