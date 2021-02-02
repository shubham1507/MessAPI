from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('deliverylt', 'foodserved', 'mess_center_name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('birth_date', 'preference')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    vendor = VendorSerializer(required=True)

    customer = CustomerSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'address_line_1', 'address_line_2',
                  'first_name', 'last_name', 'email', 'phone', 'image',
                  'password', 'is_seller', 'vendor', 'customer')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        if validated_data.get('is_seller') == True:
            print(validated_data)
            profile_data = validated_data.pop('vendor')
            password = validated_data.pop('password')
            image = validated_data.pop('image')
            email = validated_data.pop('email')
            username = validated_data.pop('username')
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')
            is_seller = validated_data.pop('is_seller')
            address_line_1 = validated_data.pop('address_line_1')
            address_line_2 = validated_data.pop('address_line_2')
            phone = validated_data.pop('phone')
            user = User(email=email,
                        username=username,
                        image=image,
                        first_name=first_name,
                        last_name=last_name,
                        is_seller=is_seller,
                        address_line_1=address_line_1,
                        address_line_2=address_line_2,
                        phone=phone)
            user.set_password(password)
            user.is_active = False
            user.save()
            Vendor.objects.create(user=user, **profile_data)
            return user

        else:

            profile_data = validated_data.pop('customer')
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            username = validated_data.pop('username')
            is_seller = validated_data.pop('is_seller')
            address_line_1 = validated_data.pop('address_line_1')
            address_line_2 = validated_data.pop('address_line_2')
            phone = validated_data.pop('phone')
            user = User(email=email,
                        username=username,
                        address_line_1=address_line_1,
                        address_line_2=address_line_2,
                        phone=phone,
                        is_seller=is_seller)
            user.set_password(password)

            # for customer login approval from admin post info check
            user.is_active = False
            user.save()
            Customer.objects.create(user=user, **profile_data)
            return user

    def update(self, instance, validated_data):

        if validated_data.get('is_seller') == True:

            profile_data = validated_data.pop('vendor')
            # profile = instance.profile
            vendor = instance.vendor

            instance.email = validated_data.get('email', instance.email)
            instance.save()
            vendor.deliverylt = profile_data.get('deliverylt',
                                                 vendor.deliverylt)
            vendor.foodserved = profile_data.get('foodserved',
                                                 vendor.foodserved)
            vendor.mess_center_name = profile_data.get('mess_center_name',
                                                       vendor.mess_center_name)
            address_line_1 = profile_data.get('address_line_1',
                                              vendor.address_line_1)
            address_line_2 = profile_data.get('address_line_2',
                                              vendor.address_line_2)
            phone = profile_data.get('phone', vendor.phone)
            image = profile_data.get('image',vendor.image)    
            vendor.save()

            return instance

        else:

            profile_data = validated_data.pop('customer')

            customer = instance.customer

            instance.email = validated_data.get('email', instance.email)

            instance.save()

            customer.birth_date = profile_data.get('birth_date',
                                                   customer.birth_date)

            customer.preference = profile_data.get('preference',
                                                   customer.preference)
            instance.address1 = validated_data.get('address1', instance.address_line_1)

            instance.address2 = validated_data.get('address2', instance.address_line_2)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.image = validated_data.get('image',instance.image)
            instance.save()
            customer.save()

            return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()
        print("validate password")
        return instance

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
class VendorListSeializer(serializers.ModelSerializer):

    model = User
    vendor = VendorSerializer(required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'image',
            'vendor',
        )

        extra_kwargs = {'password': {'write_only': True}}
