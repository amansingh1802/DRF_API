from django.urls.conf import include, path
from .views import PlanView, SubView, UserView
# from .views import (SuccessView,
#                     GenerateHashKeyView
#                     )
urlpatterns = [path('signup', UserView.as_view()),
               path('plan', PlanView.as_view()),
               path('subscribe', SubView.as_view()),
               # path('generateHashKey', GenerateHashKeyView.as_view(),
               #      name="generate-hash"),
               # path('success', SuccessView.as_view(), name="success"),
               ]
