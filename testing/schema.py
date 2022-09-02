from typing import Counter
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


class СounterpartyType(DjangoObjectType):
    class Meta:
        model = models.Сounterparty


class OrderType(DjangoObjectType):
    class Meta:
        model = models.Order


class DetailType(DjangoObjectType):
    class Meta:
        model = models.Detail


class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)
    all_counterparties = graphene.List(СounterpartyType)

    def resolve_all_orders(root, info):
        return (
            models.Order.objects
            .select("order_code")
            .all()
        )

    def resolve_all_counterparties(root, info):
        return (
            models.Сounterparty.objects
            .select("organization_name")
            .all()
        )


schema = graphene.Schema(query=Query)
