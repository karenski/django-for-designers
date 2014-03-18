from django.contrib import admin
from bookmarks.models import Bookmark, Tag

admin.site.register(Bookmark)
admin.site.register(Tag)
