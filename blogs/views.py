from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

from .models import Post, Comment
from shared.models import *
from django.contrib import auth
from django.shortcuts import render,render_to_response
from django.template import RequestContext

from .forms import RegisterForm
from .forms import LoginForm


# Create your views here.
def index(request):
    latest_post_list = sorted(Post.objects.all(), key=lambda p: p.score)
    # latest_post_list = Post.objects.all()
    context = {
        'latest_post_list': latest_post_list,
    }

    return render(request, 'blogs/index.html', context=context)


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-create_time')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blogs/results.html'

class PostView(generic.DetailView):
    model = Post
    template_name = 'blogs/post.html'

class CommentView(generic.ListView):
    template_name = 'blogs/comment.html'
    context_object_name = 'comment_list'

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk', "-1")
        return super(generic.ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return the comments of the certain post ordered by score."""
        return sorted(Comment.objects.filter(parent=self.pk), key=lambda c: c.score)

class LoginView(generic.DetailView):
    model = Post
    template_name = 'blogs/login.html'

class RegisterView(generic.DetailView):
    model = Post
    template_name = 'blogs/register.html'



def vote(request, content_id):
    if (request.method == 'POST'):
        user_id = request.POST.get('user_id', None)
        value = request.POST.get('value', 1)
        return HttpResponse(str(Vote.vote(content_id, user_id, value)))



def login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        # name = request.POST.get['username']
        # password = request.POST.get['password']


        print("fdsfdsfdsfdsfdsfsdfads")

        if login_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']


            user = auth.authenticate(username = username,password = password)
            print(user)
            print("fdsfdsfdsfdsfdsfsdfads")
            if user is not None:
                auth.login(req,user)
                return render_to_response('index.html', RequestContext(req))
            #else:
               # return render_to_response('login.html', RequestContext(req, {'password_is_wrong': True}))
                return render(request,'blogs/login.html', {'error': 'username or password error!'})

    return render(request, 'blogs/login.html', locals())


def register(request):
    if (request.method == 'POST'):
        register_form = RegisterForm(request.POST)
        # message = "Please check the information"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']

            same_name_user = User.objects.filter(username=username)
            if same_name_user:
                message = 'Username already exists!'
                return render(request, 'blogs/register.html', {'form': RegisterForm(), 'message': message})
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                message = 'Email already exists!'
                return render(request, 'blogs/register.html', {'form': RegisterForm(), 'message': message})

            new_user = User.objects.create()
            new_user.username = username
            new_user.email = email
            new_user.password = password
            new_user.save()

            message = 'Registered Successfully!'

            # return redirect('/login/')
            return render_to_response("blogs/login.html", {'message': message})
        else:
            message = 'Invalid input!'
            return render_to_response("blogs/login.html", {'message': message})


    register_form = RegisterForm()
    return render(request, 'blogs/register.html', {'form': register_form, 'message': ''})




def post(request):
    return render(request, 'blogs/post.html', locals())

def comment(request):
    return render(request, 'blogs/comment.html', locals())



