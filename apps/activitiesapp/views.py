from django.shortcuts import redirect
from models import Transaction, Review

def index(request):
    reviews = Review.objects.all()
    transactions = Transaction.objects.all()
    context = {
        'reviews': reviews,
        'transactions': transactions
    }
    return context

def create(request):
    if request.method == 'POST':
        Review.objects.create(request.POST)
        return redirect('/item')
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

