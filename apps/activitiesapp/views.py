import json

from django.forms.models import model_to_dict
from django.http import JsonResponse

from models import Review, Transaction


def index(request):
    reviews = Review.objects.all().as_dict()
    transactions = Transaction.objects.all().as_dict()
    context = {
        'reviews': reviews,
        'transactions': transactions
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
        return redirect('/')

def deleteReview(request, id):
    review = Review.objects.get(pk=id)
    if review.owner_id == request.session.user:
        review.delete()
        return redirect('/dashboard')
    else:
        return redirect('/item')

def getUser(request, id):
    transactions = Transaction.objects.by_user(id)
    reviews = Review.objects.by_user(id)
    context = {
        'transactions': transactions,
        'reviews': reviews
    }
    return context

def getItem(request, id):
    transactions = Transaction.objects.by_item(id)
    reviews = Review.objects.by_item(id)
    context = {
        'transactions': transactions,
        'reviews': reviews
    }
    return context

def getUserReviews(request, id):
    reviews = Review.objects.by_user(id)
    context = {
        'reviews': reviews
    }
    return context

def getItemReviews(request, id):
    reviews = Review.objects.by_item(id)
    context = {
        'reviews': reviews
    }
    return context

def getUserTransactions(request, id):
    transactions = Transaction.objects.by_user(id)
    context = {
        'transactions': transactions,
    }
    return context

def getItemTransactions(request, id):
    transactions = Transaction.objects.by_item(id)
    context = {
        'transactions': transactions,
    }
    return context
