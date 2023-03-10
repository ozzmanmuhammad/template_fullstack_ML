from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from identifier import api
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/images', api.ImageList.as_view()),
    path('api/image/create/', api.CreateImage.as_view()),
    path('api/image/<int:image_id>', api.GetImageById.as_view()),
    path('api/image/delete/<int:id>', api.ImageDelete.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
