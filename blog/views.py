from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Feedback
from registeration.models import Profile
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

posts = Post.objects.all()
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  
    context_object_name = 'contexts'

    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'    
    context_object_name = "context" 


    def get_context_data(self, **kwargs):
        context = super(UserPostListView,self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))    
        context['count'] = Post.objects.filter(author=user).count()
        context['roles'] = Post.objects.filter(author=user)
        context['name'] = user 
        return context



class PostDetailView(DetailView):
    model = Post

    def get_context_data(self,
     *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context    

class PostCreateView(LoginRequiredMixin ,CreateView, UserPassesTestMixin):
    model = Post        
    fields = ['title','content','tags', 'blogimage']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False      


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False      



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post    
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        

    


def about(request):
    return render(request,'blog/about.html',{'title':'about'})


class UserFilterView(ListView):
    model = Post
    template_name = 'blog/filter.html'    
    context_object_name = 'contexts'

    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))    
        return Post.objects.filter(author=user)    


def filter(request):
    tag = request.GET['tag']
    results = Post.objects.filter(tags=tag)
    return render(request,'blog/filter.html',{'contexts':results})

def search(request):
    
    val = request.GET['searchone']
    alphabet = val[0]
    if User.objects.filter(username = val):
        note = "user found"
        results = User.objects.filter(username = val)
    else:
        note = "no matches found. take a look at other users"
        results = User.objects.filter(username__startswith = alphabet)
 
    return render(request,'blog/search.html',{'contexts':results,'note':note})

    
def Realcomment(request):    
    postid = request.POST['currentpostid']
    currentuserid = request.user
    currentcomment = request.POST['box']
    femina = Feedback.objects.create(comment= currentcomment, commentater= currentuserid, reciever= postid)
    femina.save()
    results = Feedback.objects.filter(reciever = postid)
    count = Feedback.objects.filter(commentater = currentuserid).count()
    return redirect('/post/'+postid)
    
def Realcommentsection(request):
    currentuserid = request.user
    postid = request.GET['currentpostids']
    results = Feedback.objects.filter(reciever = postid).order_by('-date_posted')
    count = Feedback.objects.filter(reciever = postid).count()
    return render(request, 'blog/commentsection.html', {'contexts':results, 'num':postid, 'count':count})

def Likeview(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog-detail',args=[str(pk)]))
    