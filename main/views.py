from django.shortcuts import render
from rest_framework import generics

from models import Company, User, Event, Call, CompanyTypes, Material
from serializers import  CompanySerializer, UserSerializer, EventSerializer, CallSerializer, \
						CompanyTypesSerializer, MaterialSerializer 


class CompanyListView(generics.ListCreateAPIView):

	serializer_class = CompanySerializer

	def get_queryset(self):
		objs = Company.objects.filter()
		return objs



class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = CompanySerializer
	model = Company 



class UserListView(generics.ListCreateAPIView):

	serializer_class = UserSerializer

	def get_queryset(self):
		objs = User.objects.filter()
		return objs



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = UserSerializer
	model = User 


class EventListView(generics.ListCreateAPIView):

	serializer_class = EventSerializer

	def get_queryset(self):
		objs = Event.objects.filter()
		return objs



class EventDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = EventSerializer
	model = Event



class CallListView(generics.ListCreateAPIView):

	serializer_class = CallSerializer

	def get_queryset(self):
		objs = Call.objects.filter()
		return objs



class CallDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = CallSerializer
	model = Call


class CompanyTypesListView(generics.ListCreateAPIView):

	serializer_class = CompanyTypesSerializer

	def get_queryset(self):
		objs = CompanyTypes.objects.filter()
		return objs



class CompanyTypesDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = CompanyTypesSerializer
	model = CompanyTypes


class MaterialListView(generics.ListCreateAPIView):

	serializer_class = MaterialSerializer

	def get_queryset(self):
		objs = Material.objects.filter()
		return objs



class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = MaterialSerializer
	model = Material



def main(request):
	return render(request, 'main.html')


def logout(request):
	pass


def login(request):
	return render(request, 'login.html')