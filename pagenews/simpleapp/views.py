from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import P
from .filters import PFilter

class PList(ListView):
    model = P
    ordering = 'title_p'
    template_name = "flatpages/p.html"
    context_object_name = 'p'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, p=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PDetail(DetailView):
    model = P
    template_name = 'flatpages/p_id.html'
    context_object_name = 'p_id'

    def get_context_data(self, p_id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None
        return context

