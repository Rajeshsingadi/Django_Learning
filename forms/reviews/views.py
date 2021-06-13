from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

"""
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })
"""


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


"""
def review(request):
    # if request.method == "POST":
    #     entered_username = request.POST['username']
    #     if entered_username == "" and len(entered_username) >= 100:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True})
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    # return render(request, "reviews/review.html", {    "has_error": False})
    if request.method == "POST":
        # existing_data = Review.objects.get(pk=1) #optional these two lines
        # form = ReviewForm(request.POST, instance=existing_data)
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # review = Review(user_name=form.cleaned_data['user_name'],
            #                 review_text=form.cleaned_data['review_text'],
            #                 rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })
"""


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thankyou.html")
class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This is Working!"
        return context


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=4)
    #     return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

# class SingleReviewView(DetailView):
#     template_name = "reviews/single_review.html"
#     model = Review

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
