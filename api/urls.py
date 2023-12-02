from django.urls import path
from .views import UserRegistrationView, UserLoginView
from .views import VideoUploadView, UserVideosView
from .views import AllNerfsView
from .views import GenerateNerfModelView, UserNerfModelsView
from .views import GenerateNerfObjectView, UserNerfObjectsView

urlpatterns = [

    # users
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    # videos
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('user-videos/', UserVideosView.as_view(), name='user-videos'),

    # nerfs
    path('all-nerfs/', AllNerfsView.as_view(), name='all-nerfs'),

    # models
    path('generate-nerf-model/', GenerateNerfModelView.as_view(), name='generate-nerf-model'),
    path('user-nerf-models/', UserNerfModelsView.as_view(), name='user-nerf-models'),

    # objects
    path('generate-nerf-object/', GenerateNerfObjectView.as_view(), name='generate-nerf-object'),
    path('user-nerf-objects/', UserNerfObjectsView.as_view(), name='user-nerf-objects'),
    
]