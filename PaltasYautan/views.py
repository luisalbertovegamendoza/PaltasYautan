from django.views.generic import TemplateView
from productos.models import Producto


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productos'] = Producto.objects.filter(
            disponible=True
        )

        return context




