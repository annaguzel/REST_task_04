from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class RegisterSerializer(serializers.ModelSerializer):
	password=serializers.CharField(write_only=True)
	class Meta:
		model=User
		fields=["username","password","last_name","first_name"]
	def create (self, validated_data) :
		user = User(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
		user.set_password(validated_data['password'])
		user.save()


		return validated_data
	#def create(self,validated_data):
		#username = validated_data.get("username")
		#password= validated_data.get("password")
		#lastname= validated_data.get("last_name")
		#firstname= validated_data.get("first_name")

		#user=User(username=username)
		#user.set_password(password)
		#user.save()
		#return validated_data
