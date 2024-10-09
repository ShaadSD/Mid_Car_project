from django.shortcuts import render,redirect
from car.models import Car,Buy
from brand.models import Brand
from car import forms
from django.views import View
from django.views.generic import ListView,DetailView

def home(request,brand_slug=None):
    data= Car.objects.all()
    if brand_slug is not None:
        brand=Brand.objects.get(slug=brand_slug)
        data=Car.objects.filter(brand=brand)
   
    brands=Brand.objects.all()
    return render(request,'home.html',{'data': data,'brand': brands})
    
# def view_details(request, id):
#     data = Car.objects.get(pk=id)
#     return render(request, 'view_details.html', {'data': data})



class DetailCarView(DetailView):
    model=Car
    pk_url_kwarg='id'
    template_name='view_details.html'
    
    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.car=car
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        car=self.object 
        comments=car.comments.all()
        comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context



# def buy_car(request,id):
#     car=Car.objects.get(pk=id)

#     if car.quantity>0:
#         car.quantity-=1
#         buy=Buy(user=request.user,car=car)
#         buy.save()
#         car.save()
#         return redirect('profile')
#     else:
#         return redirect('view_details',id=id)

class Buy_car(View):
    def post(self, request, id):
        car=Car.objects.get(Car,pk=id)
        if car.quantity>0:
            car.quantity-=1
            car.save()
            Buy.objects.create(user=request.user,car=car)
            return redirect('profile')
        else:
            return redirect('view_details',id=id)




# def profile(request):
#     buy=Buy.objects.filter(user=request.user)
#     return render(request,'profile.html',{'buy':buy})

class ProfileView(ListView):
    model=Buy
    template_name='profile.html'
    context_object_name='buy'

    def get_queryset(self):
        return Buy.objects.filter(user=self.request.user)