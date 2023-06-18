from django.contrib.auth.views import LoginView


class CustomBackendLoginView(LoginView):
    extra_context = {'site_type': 'Identity Access Management',
                     'helper_text': '(Bitte geben Sie die Anmeldedaten des Personals ein)'
                     }

    # Add any additional customizations here

    pass
