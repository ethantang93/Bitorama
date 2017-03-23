import json

from django.forms.models import model_to_dict
from django.http import JsonResponse

from models import Review, Transaction


def index(request):
    reviews = Review.objects.all()
    jsonReviews = [model_to_dict(obj) for obj in reviews.get_queryset()]
    transactions = Transaction.objects.all()
    jsonTransactions = [model_to_dict(obj) for obj in transactions.get_queryset()]
    context = {
        'reviews': jsonReviews,
        'transactions': jsonTransactions
    }
    return JsonResponse(context)

def create(request):
    if request.method == 'POST':
        review = Review.objects.create(request.POST)
        review = review.as_dict()
        return JsonResponse({
            'success': True,
            'review': review
            })
    else:
        return JsonResponse({
            'success': False,
            'review': None
            })

def deleteReview(request, id):
    review = Review.objects.get(pk=id)
    if review.owner_id == request.session.user:
        review.delete()
        return JsonResponse({
            'success': True
        })
    else:
        return JsonResponse({
            'success': False
        })

def getUser(request, id):
    transactions = Transaction.objects.by_user(id)
    jsonTransactions = [model_to_dict(obj) for obj in transactions.get_queryset()]
    reviews = Review.objects.by_user(id)
    jsonReviews = [model_to_dict(obj) for obj in reviews.get_queryset()]
    context = {
        'transactions': jsonTransactions,
        'reviews': jsonReviews
    }
    return JsonResponse(context)

def getItem(request, id):
    transactions = Transaction.objects.by_item(id)
    jsonTransactions = [model_to_dict(obj) for obj in transactions.get_queryset()]
    reviews = Review.objects.by_item(id)
    jsonReviews = [model_to_dict(obj) for obj in reviews.get_queryset()]
    context = {
        'transactions': jsonTransactions,
        'reviews': jsonReviews
    }
    return JsonResponse(context)

def getUserReviews(request, id):
    reviews = Review.objects.by_user(id)
    jsonReviews = [model_to_dict(obj) for obj in reviews.get_queryset()]
    context = {
        'reviews': jsonReviews
    }
    return JsonResponse(context)

def getItemReviews(request, id):
    reviews = Review.objects.by_item(id)
    jsonReviews = [model_to_dict(obj) for obj in reviews.get_queryset()]
    context = {
        'reviews': jsonReviews
    }
    return JsonResponse(context)

def getUserTransactions(request, id):
    transactions = Transaction.objects.by_user(id)
    jsonTransactions = [model_to_dict(obj) for obj in transactions.get_queryset()]
    context = {
        'transactions': jsonTransactions,
    }
    return JsonResponse(context)

def getItemTransactions(request, id):
    transactions = Transaction.objects.by_item(id)
    jsonTransactions = [model_to_dict(obj) for obj in transactions.get_queryset()]
    context = {
        'transactions': jsonTransactions,
    }
    return JsonResponse(context)
