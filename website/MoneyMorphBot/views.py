from django.http import HttpResponse
from django.shortcuts import render
from . import engine


def is_real_number(s):
    # Supprime les espaces en début et en fin de chaîne
    s = s.strip()

    # Si la chaîne est vide, retourne False
    if not s:
        return False

    # Remplace le point décimal par une chaîne vide
    s = s.replace(".", "")

    # Vérifie si le reste de la chaîne est numérique
    return s.isnumeric()


# Display the landing page
def index(request):
    if request.method == "GET":
        context = {
            "title": "MoneyMorphBot, your friendly currency converting bot",
        }
        return render(request, "MoneyMorphBot/index.html", context)
    else:
        if request.method == "POST":
            amount = request.POST.get("amount")
            from_currency = request.POST.get("from")
            to_currency = request.POST.get("to")
            if (amount != "") & (from_currency != "") & (to_currency != "") & (
                    from_currency != to_currency) & is_real_number(amount):
                # Some other verifications could have been done but this is enough for this project
                result = engine.convert(amount, from_currency, to_currency)
                context = {
                    "title": "MoneyMorphBot, your friendly currency converting bot",
                    "amount": amount,
                    "from_currency": from_currency,
                    "to_currency": to_currency,
                    "result": result,
                }
                return render(request, "MoneyMorphBot/index.html", context)
            else:
                return HttpResponse("Error: Invalid input")
        else:
            return HttpResponse("Error: Invalid request method")


def about(request):
    context = {
        "title": "About MoneyMorphBot",
    }
    return render(request, "MoneyMorphBot/about.html", context)


def contact(request):
    context = {
        "title": "Contact MoneyMorphBot",
    }
    return render(request, "MoneyMorphBot/contact.html", context)


def terms(request):
    context = {
        "title": "Terms and Conditions",
    }
    return render(request, "MoneyMorphBot/terms.html", context)
