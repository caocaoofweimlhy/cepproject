from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Request, Favor, Tag
from .forms import RequestForm, FavorForm, TagForm, RequestFormUpdate
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
import json

def home(request):
    return render(request, 'ttrade/index.html')

def dashboard(request):
    return render(request, 'ttrade/dashboard.html')

def accept_request(request):
    duration = request.GET.get('targetDuration')
    me = request.user
    targetUser = User.objects.get(username = request.GET.get('targetUser'))
    meProfile = UserProfile.objects.get(user = me)
    targetProfile = UserProfile.objects.get(user = targetUser)
    targetContent = request.GET.get('targetContent')
    theRequest = Request.objects.get(id = int(targetContent))
    targetProfile.timepoint = targetProfile.timepoint+int(duration)
    meProfile.timepoint = meProfile.timepoint-int(duration)
    theRequest.acceptor = meProfile
    theRequest.accepted = True
    theRequest.save()
    meProfile.save()
    targetProfile.save()
    return HttpResponse()
    
class RequestList(ListView):
    model = Request
    queryset = Request.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequestList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        tag = self.kwargs['tag']
        if tag == '':
            self.queryset = Request.objects.all()
            return self.queryset
        else:
            self.queryset = Request.objects.all().filter(tag__title__iexact=tag)
            return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(RequestList, self).get_context_data(**kwargs)
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class FavorList(ListView):
    model = Favor
    queryset = Favor.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FavorList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        self.queryset = Favor.objects.all().filter(user=curruser)
        return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(FavorList, self).get_context_data(**kwargs)
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class RequestCreate(CreateView):
    model = Request
    form_class = RequestForm
    
    def get_context_data(self, **kwargs):
        context = super(FavorList, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class FavorCreate(CreateView):
    model = Favor
    form_class = FavorForm
    
    def form_valid(self, form):
        curruser = UserProfile.objects.get(user=self.request.user)
        form.instance.user = curruser
        form.save()
        return super(FavorCreate, self).form_valid(form)

class RequestUpdate(UpdateView):
    model = Request
    form_class = RequestFormUpdate
    
class FavorUpdate(UpdateView):
    model = Favor
    form_class = FavorForm

class RequestDetail(DetailView):
    model = Request

class FavorDetail(DetailView):
    model = Favor
    
class RequestDelete(DeleteView):
    model = Request
    success_url = reverse_lazy('dashboard')
    
class FavorDelete(DeleteView):
    model = Favor
    success_url = reverse_lazy('dashboard')

class MyViewR(TemplateView):
    tag_form_class = TagForm
    request_form_class = RequestForm
    template_name = "ttrade/request_hybrid.html"
    
    def get(self, request, *args, **kwargs):
        kwargs.setdefault("createtag_form", self.tag_form_class())
        kwargs.setdefault("createrequest_form", self.request_form_class())
        return super(MyViewR, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        
        if "btn_createtag" in request.POST['form']: 
            form = self.tag_form_class(**form_args)
            if not form.is_valid():
                response_dict = {}
                response_dict['status'] = 0
                response_dict['message'] = form.errors.as_ul()
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
            else:
                curruser = UserProfile.objects.get(user=self.request.user)
                form.instance.user = curruser
                form.save()
                data = Tag.objects.all()
                response_dict = {'status': 1}
                response_dict['message'] = list(data.values('id','title'))
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
        elif "btn_createrequest" in request.POST['form']:
            form = self.request_form_class(**form_args)
            if not form.is_valid():
                response_dict = {}
                response_dict['status'] = 0
                response_dict['message'] = form.errors.as_ul()
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
            else:
                curruser = UserProfile.objects.get(user=self.request.user)
                form.instance.user = curruser
                form.save()
                response = {'status': 1, 'message':'Request is created!'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder))
        
        return super(MyViewR, self).get(request)

class UserDetail(DetailView):
    model = UserProfile

class AcceptedList(ListView):
    model = Request
    queryset = Request.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AcceptedList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        self.queryset = Request.objects.all().filter(acceptor=curruser)
        return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(AcceptedList, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class PostedList(ListView):
    model = Request
    queryset = Request.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostedList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        self.queryset = Request.objects.all().filter(user=curruser)
        return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(PostedList, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class FavorListAll(ListView):
    model = Favor
    queryset = Favor.objects.all()