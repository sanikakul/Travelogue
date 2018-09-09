from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request):
        """
        Docstrings
        """
        return render(request, 'login/index.html')