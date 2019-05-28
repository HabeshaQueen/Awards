from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


# Create your views here.
#first page - signup page
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

#landing page - home page
def home_index(request):

    index_path = Project.objects.all()
    # forms=CommentForm()
    # comments = Comments.objects.all()
    # my_profile = Profile.objects.all()
    return render(request,'home.html',locals())

#profile page
@login_required
def profile_path(request):

    images = Project.objects.all()
    my_profile = Profile.objects.all()

    return render(request,'profile.html', locals())



def single(request,single_id):
    try:
        index_path = Project.objects.filter(id = single_id)
    except DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('single')
    else:
        form =  VoteForm()

    return render(request,"single.html", locals())




def update(request):
    all_profile = Profile.objects.all()
    profile = Profile.objects.get(user_id = request.user)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form  = ProfileForm()

    return render(request,'new_profile.html', locals())

def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())


@login_required(login_url='/accounts/login/')
def all(request, pk):
   profile = Profile.objects.get(pk=pk)
   projects = Project.objects.all().filter(posted_by_id=pk)
   content = {
       "profile": profile,
       'projects': projects,
   }
   return render(request, 'profile.html', content)

def post_new(request):

    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

    return render(request,'post_new.html',locals())

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('homePage')

    else:
        form = UploadForm()
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_review(request,pk):
   project = get_object_or_404(Project, pk=pk)
   current_user = request.user
   if request.method == 'POST':
       form = ReviewForm(request.POST)
       if form.is_valid():
           design = form.cleaned_data['design']
           usability = form.cleaned_data['usability']
           content = form.cleaned_data['content']
           review = form.save(commit=False)
           review.project = project
           review.juror = current_user
           review.design = design
           review.usability = usability
           review.content = content
           review.save()
           return redirect('homePage')
   else:
       form = ReviewForm()
       return render(request,'review.html',{"user":current_user,"form":form})