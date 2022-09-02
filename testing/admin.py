from django.contrib import admin
from testing.models import Profile, Сounterparty, Order, Detail


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Сounterparty)
class СounterpartyAdmin(admin.ModelAdmin):
    model = Сounterparty


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    model = Detail
