from tastypie.resources import ModelResource
from bookmarks.models import Bookmark

class BookmarkResource(ModelResource):
	class Meta:
		allowed_methods = ['get']
		queryset = Bookmark.objects.all()
		resource_name = 'bookmark'

