from django.shortcuts import render, get_object_or_404, redirect, reverse
from core.models import Deck
from core.models import Card
from .forms import DeckForm, CardForm

# Create your views here.

def list_deck(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'html/deck_page.html', {'decks': decks})

def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    return render(request, 'html/deck_detail.html', {'deck': deck})

def add_deck(request):
    if request.method == 'GET':
        form = DeckForm()
    else:
        form = DeckForm(data=request.POST)
        if form.is_valid():
            new_deck = form.save(commit=False)
            new_deck.user = request.user
            new_deck.save()
            return redirect(to='list-deck')
    return render(request, 'html/add_deck.html', {'form': form})

def add_card(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.deck = deck
            new_card.save()
            return redirect(to='deck-detail', pk=new_card.deck.pk)
    return render(request, 'html/add_card.html', {'form': form})
        

def delete_card(request, pk):
    
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        card.delete()
        return redirect(to='deck-detail', pk=card.deck.pk)
    return render(request, 'html/delete_card.html', {'card': card})

def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='list-deck')
    return render(request, 'html/delete_deck.html', {'deck': deck})

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "GET":
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(to='deck-detail', pk=card.deck.pk)
    return render(request, 'html/edit_card.html', {'card': card, 'form': form})


def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == "GET":
        form = DeckForm(instance=deck)
    else:
        form = DeckForm(data=request.POST, instance=deck)
        form.save()
        return redirect(to='list-deck')
    return render(request, 'html/edit_deck.html', {'deck': deck, 'form': form})