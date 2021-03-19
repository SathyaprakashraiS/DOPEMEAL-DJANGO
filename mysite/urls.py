
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from main.views import fooddetailview
#from main.views import paleodetailview
#from main.views import vegetariandetailview
#from main.views import vegandetailview
from main.views import pybot
from main.views import schemeselection
from main.views import comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('basic/',include("main.urls")),
    path('fo/',include("main.urls")),
    path('result/',include("main.urls")),
    path('comment/',include("main.urls")),
    #path('food',fooddetailview),
    #path('paleo',paleodetailview),
    #path('vegetarian',vegetariandetailview),
    #path('vegan',vegandetailview),
    path('pybot/',pybot, name='pybot'),
    path('scheme',schemeselection),
    #path('page1/',include("main.urls")),  
    path('callcalcal/',include("main.urls")),
    path('call/calcalculated/',include("main.urls")),
    path('testdropdown/',include("main.urls")),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)