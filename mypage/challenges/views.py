#from django.template.loader import render_to_string
from django.http.response import Http404
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here.


# def index(months):
#     return HttpResponse("This Works! Hoorayyyy!!")
# def index2(months):
#     return HttpResponse("This is Feb!")
"""
def monthly_challanges_num(request, months):
    return HttpResponse(months)
"""

"""
def monthly_challenges(request, months):
    challenge_text = None
    if months == "january":
        challenge_text = "This is lord siva time"

    elif months == "febuary":
        challenge_text = "This is Feb time"

    elif months == "march":
        challenge_text = "This is march month"

    else:
        return HttpResponseNotFound("This month is not found!")

    return HttpResponse(challenge_text)
"""


monthly_challenges_dict = {
    "january": "this is jan",
    "febuary": "this is feb",
    "march": "this is mar",
    "april": "this is apr",
    "may": "this is may",
    "june": "this is jun",
    "july": None
}

"""
def monthly_challanges_num(request, months):
    list_months = list(monthly_challenges_dict.keys())
    if months > len(list_months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = list_months[months-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)
"""


def monthly_challanges_num(request, months):
    list_months = list(monthly_challenges_dict.keys())
    if months > len(list_months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = list_months[months-1]
    redirect_path = reverse("month_challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


"""
def monthly_challenges(request, months):
    try:
        list_months = monthly_challenges_dict[months]
        return HttpResponse(list_months)
    except:
        return HttpResponseNotFound("<h1>This is not found u fooooool</h1>")
    
"""

"""
def index(request):
    list_items = ""
    months = monthly_challenges_dict.keys()
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a> </li > "
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
"""

"""
def monthly_challenges(request, months):
    try:
        list_months = monthly_challenges_dict[months]
        response_data = f"<h1>{list_months}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not found u fooooool</h1>")
"""

"""
def monthly_challenges(request, months):
    # try:
    list_months = monthly_challenges_dict[months]
    response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)
    # except:
    return HttpResponseNotFound("<h1>This is not found u fooooool</h1>")
"""

"""
def monthly_challenges(request, months):
    try:
        list_months = monthly_challenges_dict[months]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This is not found u fooooool</h1>")
"""

# dynamically adding html content


def monthly_challenges(request, months):
    try:
        list_months = monthly_challenges_dict[months]
        return render(request, "challenges/challenge.html", {
            "text": list_months,
            "text2": months.capitalize()
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404()#keep debug false insettings.py to execute


def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
