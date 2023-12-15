from django.urls import path

from textsnippets.views.create_snippet import CreateSnippet
from textsnippets.views.list_snippets import ListSnippets
from textsnippets.views.snippet_details import SnippetDetails
from textsnippets.views.update_snippet import UpdateSnippet
from textsnippets.views.delete_snippet import DeleteSnippet
from textsnippets.views.list_tag import ListTags
from textsnippets.views.tag_details import TagDetails

urlpatterns = [
    # Create Items
    path('create/', CreateSnippet.as_view(), name='create_snippet_view'),

    # Items List
    path('list/tags/', ListTags.as_view(), name='list_tags_view'),
    path('list/snippets/', ListSnippets.as_view(), name='list_snippets_view'),

    # Item Details
    path('details/snippet/<str:snippet_id>/', SnippetDetails.as_view(), name='snippet_details_view'),
    path('details/tag/<str:tag_id>/', TagDetails.as_view(), name='tag_details_view'),

    # Update Items
    path('update/', UpdateSnippet.as_view(), name='update_snippet_view'),

    # Delete Items
    path('delete/', DeleteSnippet.as_view(), name='delete_snippet_view'),
]
