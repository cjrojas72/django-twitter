from django.shortcuts import render,  reverse, HttpResponseRedirect
from tweet.models import Tweet
from tweet.forms import AddTweetForm


def AddTweet(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data['body'],
                author=request.user
            )
            return HttpResponseRedirect(reverse('home'))

    form = AddTweetForm()

    return render(request, 'tweet.html', {"form": form})


def TweetView(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweetview.html', {'tweet': tweet})
