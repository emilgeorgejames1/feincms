from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from feincms.models import Page


def handler(request, path=None):
    if path is None:
        path = request.path

    page = Page.objects.page_for_path_or_404(path)

    if page.redirect_to:
        return HttpResponseRedirect(page.redirect_to)

    return render_to_response(page.template.path, {
        'feincms_page': page,
        }, context_instance=RequestContext(request))

