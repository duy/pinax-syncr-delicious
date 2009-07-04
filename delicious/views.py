from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from django.utils.translation import ugettext_lazy as _

from delicious.delicious.forms import DeliciousAccountForm, TagForm
from delicious.delicious import DeliciousSyncr

@login_required
def syncr_delicious(request):
    # if already delicious account
    has_delicious_account = False
    if request.user.delicious_account.all():
        has_delicious_account = True
#    if request.method == "POST":
#        tag_form = TagForm(request.POST)
#        if tag_form.is_valid():
#            pass
#            # actions depending on options
#            d = DeliciousSyncr(delicious_account.username, delicious_account.password)
#            
#    else:
#        tag_form = TagForm()
    return render_to_response("delicious/delicious_options.html", {
        "has_delicious_account": has_delicious_account,
#        'tag_form': tag_form,
        
    }, context_instance=RequestContext(request))

@login_required
def add_delicious_account(request):
    # if already delicious account...
    
    if request.method == "POST":
        delicious_account_form = DeliciousAccountForm(request.user, request.POST)
        if delicious_account_form.is_valid():
            delicious_account = delicious_account_form.save(commit=False)
            delicious_account.user = request.user
            delicious_account.save()
            
            d = DeliciousSyncr(delicious_account.username, delicious_account.password)
            d.syncAll(request.user)
#            return HttpResponseRedirect(reverse("syncr_pinax.delicious.views.recently_imported"))
            return HttpResponseRedirect(reverse("bookmarks.views.your_bookmarks"))
    else:
        delicious_account_form = DeliciousAccountForm()
    
    return render_to_response("delicious/add_delicious_account.html", {
        "delicious_account_form": delicious_account_form,
    }, context_instance=RequestContext(request))

@login_required
def import_all(request):
    # if already delicious account...
    d = DeliciousSyncr(request.user.delicious_account.get().username,request.user.delicious_account.get().password)
    print "inicio sincronizacion"
    d.syncAll(request.user)
    print "fin sincronizacion"
#            return HttpResponseRedirect(reverse("syncr_pinax.delicious.views.recently_imported")
    return HttpResponseRedirect(reverse("bookmarks.views.your_bookmarks"))

@login_required
def recently_imported(request):
    bookmark_instances = BookmarkInstance.objects.filter(user=request.user).order_by("-saved")
    return render_to_response("bookmarks/your_bookmarks.html", {
        "bookmark_instances": bookmark_instances,
    }, context_instance=RequestContext(request))
    
