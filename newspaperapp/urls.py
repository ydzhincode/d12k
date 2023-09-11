from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete, PostCategory, \
    subscribe_to_category, CategoryList

app_name = 'newspaperapp'
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='details'),
    path('search', PostSearch.as_view()),
    path('add', PostCreate.as_view()),
    path('<int:pk>/edit', PostEdit.as_view()),
    path('<int:pk>/delete', PostDelete.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', PostCategory.as_view()),
    path('subscribe/<int:pk>/', subscribe_to_category, name='subscribe')
]
