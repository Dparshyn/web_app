from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from publications.models import Publication, Comments


def get_publication(request, id):
    template = 'publication.html'

    try:
        publication = Publication.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Publication id {id} doesn't exists")

    comments = Comments.objects.filter(publication=publication)
    content = {
        'publication': publication,
        'comments': comments,
    }
    return render(request, template, content)

