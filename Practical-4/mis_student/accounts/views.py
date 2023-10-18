from django.shortcuts import render, redirect
from .models import suser as users
from .models import Post, Comment
from django.contrib import messages
# Create your views here.

# def home(req):
#     return render(req, 'index.html')


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Retrieve the suser instance associated with the username from the session
            try:
                author = users.objects.get(uname=request.session['uname'])
                post = Post(author=author, content=content)
                post.save()
                messages.success(request, 'Post created successfully!')
                return redirect('home')
            except users.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Post content cannot be empty.')
    return render(request, 'create_post.html')


def like_post(request, post_id):
    try:
        post_id = int(post_id)
        post = Post.objects.get(pk=post_id)
        if request.session['uname'] in post.likes.all():
            cnt = post.likes.count()
            cnt = cnt - 1
            post.likes.remove(cnt)
        else:
            #post.likes.add(request.session['uname'])
            cnt = post.likes.count()
            cnt = cnt + 1
            post.likes.add(cnt+1)
        return redirect('home') 
    except (Post.DoesNotExist):
        messages.error(request, 'Invalid post or post not found.')
        return redirect('home')


def add_comment(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            try:
                post = Post.objects.get(pk=post_id)
                author = users.objects.get(uname=request.session['uname'])
                comment = Comment(user=author, post=post, text=text)
                comment.save()
                messages.success(request, 'Comment added successfully!')
            except (users.DoesNotExist, Post.DoesNotExist):
                messages.error(request, 'Invalid post or user.')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('home')




def register(req):

    if req.method == 'POST':
        fname = req.POST['first_name']
        lname = req.POST['last_name']
        uname = req.POST['user_name']  
        email = req.POST['email']
        password = req.POST['password1']

        f = 0
        user = users.objects.all()
        for u in user:
            if u.uname == uname:
                f=1
                messages.info(req,"Username is already taken.")
                break
            if u.email == email:
                f=1
                messages.info(req,"Username is already taken.")
                break
        
        if f == 0:
            users(fname=fname,lname=lname,uname=uname,email=email,password=password).save()
            messages.info(req,"hello, " + req.POST['user_name'])
            req.session['uname'] = uname
            return render(req,'index.html')
        else:
            return render(req, 'register.html')
    else:
        return render(req, 'register.html')
    
def login(req):
    if req.method == 'POST':
        try:
            userdetails = users.objects.get(uname = req.POST['uname'],email = req.POST['email'], password = req.POST['password'])
            req.session['uname'] = userdetails.uname
            return render(req, 'index.html')
        except users.DoesNotExist as e:
            messages.info(req, "Email/ password does not match..")
    return render(req, 'login.html')

def logout(req):
    try:
        del req.session['uname']
    except:
        return render(req,'index.html')
    return render(req, 'login.html')
    