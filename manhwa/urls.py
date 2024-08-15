from django.urls import path
from .views import index,about,add_reviews,ongoing,complete,first,view_comments,commentCreateView,commentUpdateView,commentDeleteView,favorites,favoriteCreateView,favoriteUpdateView,favoriteDeleteView


urlpatterns = [
    path('', first ,name='first'),
    path('dashboard',index, name='home'),
    path('complete/',complete, name='complete'),
    path('ongoing/',ongoing, name='ongoing'),
    path('about/<int:pk>/', about, name='about'),
    path('reviews/add/',add_reviews, name="add"),
    path('comments/',view_comments, name="chat"),
    path('favorites/',favorites, name="favorites"),
    path('comments/create/',commentCreateView.as_view(),name ="create-comments"),
    path('comments/<int:pk>/update/',commentUpdateView.as_view(),name ="update-comments"),
    path('comments/<int:pk>/delete/',commentDeleteView.as_view(),name ="delete-comments"),
    path('favorite/create/',favoriteCreateView.as_view(),name ="create-favorite"),
    path('favorite/<int:pk>/update/',favoriteUpdateView.as_view(),name ="update-favorite"),
    path('favorite/<int:pk>/delete/',favoriteDeleteView.as_view(),name ="delete-favorite"),
]

