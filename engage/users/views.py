from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User, Follow, Notification
from posts.models import Post

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')

    is_following = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=user
        ).exists()

    return render(request, 'profile.html', {
        'profile_user': user,
        'posts': posts,
        'is_following': is_following
    })

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        bio = request.POST.get('bio')
        image = request.FILES.get('profile_picture')

        user.bio = bio

        if image:
            user.profile_picture = image

        user.save()
        return redirect('profile', username=user.username)

    return render(request, 'edit_profile.html', {'user': user})

@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)

    if request.user == target_user:
        return redirect('profile', username=username)

    follow = Follow.objects.filter(
        follower=request.user,
        following=target_user
    )

    if follow.exists():
        follow.delete()  # unfollow
    else:
        Follow.objects.create(
            follower=request.user,
            following=target_user
        )

    return redirect('profile', username=username)

@login_required
def search_users(request):
    query = request.GET.get('q')
    users = []

    if query:
        users = User.objects.filter(
            Q(username__icontains=query)
        )

    return render(request, 'search.html', {
        'query': query,
        'users': users
    })


@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)

    if request.user == target_user:
        return redirect('profile', username=username)

    follow = Follow.objects.filter(
        follower=request.user,
        following=target_user
    )

    if follow.exists():
        follow.delete()
    else:
        Follow.objects.create(
            follower=request.user,
            following=target_user
        )

        # 🔔 CREATE NOTIFICATION
        Notification.objects.create(
            sender=request.user,
            receiver=target_user,
            message="started following you"
        )

    return redirect('profile', username=username)

@login_required
def notifications_view(request):
    notifications = request.user.notifications.all().order_by('-created_at')

    return render(request, 'notifications.html', {
        'notifications': notifications
    })

@login_required
def notifications_view(request):
    notifications = request.user.notifications.all().order_by('-created_at')

    # ✅ mark all as read
    notifications.update(is_read=True)

    return render(request, 'notifications.html', {
        'notifications': notifications
    })

