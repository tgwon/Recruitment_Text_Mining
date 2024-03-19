from django.views.generic import View, ListView, DetailView, FormView, CreateView
from .models import *
from django.db.models import Q
from django.contrib import messages


# 공지사항 리스트 뷰
class RecruitList(ListView):
    model = Gonggo
    paginate_by = 10
    # paginate_orphans = 10
    template_name = 'recruit/recruit_list.html'  # DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'recruit_list'  # DEFAULT : <app_label>_list

    def get_queryset(self):
        recruit_list = Gonggo.objects.all()
        search_keyword = self.request.GET.get('q', '')

        if search_keyword:
            search_recruit_list = recruit_list.filter(
                    Q(title__icontains=search_keyword) |
                    Q(company_names__icontains=search_keyword) |
                    Q(main_category__icontains=search_keyword) |
                    Q(industry__icontains=search_keyword))
            return search_recruit_list
        else:
            return recruit_list
         

    def get_context_data(self, *args, **kwargs):
        context = super(RecruitList,self).get_context_data(*args,**kwargs)
        return context

class RecruitDetail(DetailView):
    model = Gonggo
    template_name = 'recruit/recruit_detail.html'
    context_object_name = 'recruit'