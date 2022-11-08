#from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from .models import Review, Song

from .form import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
import datetime

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}

    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, id=pk)

    return render(request, 'review_detail.html', {'review': review})

def song_list(request):
    song_list = Song.objects.order_by('-title')[:20]
    context = {'song_list':song_list}

    return render(request, 'song_list.html', context)

def song_detail(request, pk):
    song = get_object_or_404(Song, id = pk)
    form = ReviewForm()

    return render(request, 'song_detail.html', {'song':song})

def add_review(request, pk):
    song = get_object_or_404(Song, id = pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data('rating')
        comment = form.cleaned_data('comment')
        user_name = form.cleaned_data('user_name')
        review = Review()
        review.song = song
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        return HttpResponseRedirect(reverse('song_detail', args = (song.id,)))
    return render(request, 'song_detail.html', {'song': song, 'form': form})

def logout_view(request):
    logout(request)

    return redirect('/')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')















