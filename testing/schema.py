from django.conf import settings
from graphene_django import DjangoObjectType

from testing import models

import graphene
from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProfileType(DjangoObjectType):
    class Meta:
        model = models.Profile


class CounterpartyType(DjangoObjectType):
    class Meta:
        model = models.Counterparty


class OrderType(DjangoObjectType):
    class Meta:
        model = models.Order


class DetailType(DjangoObjectType):
    class Meta:
        model = models.Detail


class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)
    all_counterparties = graphene.List(CounterpartyType)

    def resolve_all_orders(root, info):
        return (
            models.Order.objects.all()
        )

    def resolve_all_counterparties(root, info):
        return (
            models.Counterparty.objects
            .select("organization_name")
            .all()
        )
    pass


schema = graphene.Schema(query=Query)
