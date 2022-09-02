from django.contrib import admin
from testing.models import Profile, Counterparty, Order, Detail


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    model = Counterparty


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    model = Detail
