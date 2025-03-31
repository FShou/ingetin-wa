from django.views import View
from core.views import LoginRequiredMixinView


class ConnectionView(LoginRequiredMixinView,View):
    def get(self,request):
        pass

    def post(self,request):
        pass
