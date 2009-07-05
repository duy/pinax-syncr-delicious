from django.conf.urls.defaults import *

urlpatterns = patterns('',    
    url(r'^add_account/$', 'delicious.views.add_delicious_account', name="add_delicious_account"),
    url(r'^import_all/$', 'delicious.views.import_all', name="import_all"),
    url(r'^$', 'delicious.views.recently_imported', name="recently_imported"),
    url(r'^syncr_delicious/$', 'delicious.views.syncr_delicious', name="syncr_delicious"),
)
