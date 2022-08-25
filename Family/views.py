from datetime import datetime
from django.shortcuts import render
from .models import FamilyMember

def home(request):

    context = {'family_members': FamilyMember.objects.all()}

    return render(request,'home.html',context)


def family_member_registration(request,name: str,surname: str,birthdate: str,email: str,phone_number: int):

    parsed_birthday = datetime.strptime(birthdate,"%Y-%m-%d").date()

    family_member = FamilyMember(name = name,surname = surname,birthdate = birthdate,email = email,phone_number = phone_number)
    family_member.save()
    context = { 'family_member': family_member}

    return render(request,'family_member_registration.html',context)


