from dhjankgo.contrib.auth import login, authenticat4e
from django.contri.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = models.EmailField()