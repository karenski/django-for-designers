from django.shortcuts import render, get_object_or_404, redirect
from bookmarks.models import Bookmark, Tag
from bookmarks.forms import BookmarkForm
import urllib
 
def index(request):
    if request.method == 'POST':
    	form = BookmarkForm(request.POST)
    	if form.is_valid():
    		new_bookmark = form.save()
    		raw_tags = form.cleaned_data['tags'].split(',')
    		if raw_tags:
    			for raw_tag in raw_tags:
    				raw_tag = raw_tag.strip().replace(' ','_').lower()
    				tag_slug = urllib.quote(raw_tag)
    				tag, created = Tag.objects.get_or_create(slug=tag_slug)
    				tag.save()
    				tag.bookmarks.add(new_bookmark)

    		return redirect(index)
    bookmarks = Bookmark.objects.all().order_by('-timestamp')[:10]
    current_user = request.user
    form = BookmarkForm(initial={'author':current_user})
    context = {
        'bookmarks': bookmarks,
        'form': form,
    }
    return render(request, 'index.html', context)


def tag(request, tag_name):
    tag = get_object_or_404(Tag, slug=tag_name)
    bookmarks = tag.bookmarks.all()
    context = {
        'tag': tag,
        'bookmarks': bookmarks,
    }
    return render(request, 'tag.html', context)
