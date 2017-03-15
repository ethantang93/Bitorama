from django.shortcuts import render, redirect
from models import Activity, Transaction, Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    transactions = Transaction.objects.all()
    context = {
        'reviews': reviews,
        'transactions': transactions
    }
    return context

def get(request):
    pass

def create(request):
    if request.method == 'POST':
        Activity.objects.new_activity(request.POST)
        return redirect('/item')
    return redirect('/')

def delete(request, id):
    pass

def getUser(request, id):
    activity = Activity.objects.get_user(id)
    context = {
        'activity': activity
    }
    return context

def getItem(request, id):
    result = Activity.objects.itemid(id)

def getUserReviews(request, id):
    pass

def getItemReviews(request, id):
    pass

def getUserTransactions(request, id):
    pass

def getItemTransactions(request, id):
    pass

