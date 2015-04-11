from rest_framework import serializers

from models import Company, User, Event, Call, CompanyTypes, Material


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event


class CallSerializer(serializers.ModelSerializer):
	class Meta:
		model = Call


class CompanyTypesSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyTypes


class MaterialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Material