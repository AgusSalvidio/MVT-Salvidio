from django.shortcuts import render
from .models import FamilyMember

def home(request):

    context = {'family_members': FamilyMember.objects.all()}

    return render(request,'home.html',context)


def family_member_registration(request,name,surname,born_date,email,phone_number):

    family_member = FamilyMember(name,surname,born_date,email,phone_number)
    family_member.save()
    context = { 'family_member': family_member}

    return render(request,'family_member_registration.html',context)


