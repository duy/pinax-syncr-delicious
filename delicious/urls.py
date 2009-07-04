from django.conf.urls.defaults import *

urlpatterns = patterns('',    
    url(r'^add_account/$', 'syncr_pinax.delicious.views.add_delicious_account', name="add_delicious_account"),
    url(r'^import_all/$', 'syncr_pinax.delicious.views.import_all', name="import_all"),
    url(r'^$', 'syncr_pinax.delicious.views.recently_imported', name="recently_imported"),
    url(r'^syncr_delicious/$', 'syncr_pinax.delicious.views.syncr_delicious', name="syncr_delicious"),
)
