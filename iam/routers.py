from rest_framework import routers

from users import views as user_views

router = routers.SimpleRouter()

router.register(r'user', user_views.UserView, basename="users")
router.register(r'authentication', user_views.AuthView, basename="authentication")
