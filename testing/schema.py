from django.conf import settings
from graphene_django import DjangoObjectType
import graphene

from testing import models

class UserType(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL

class ClientType(DjangoObjectType):
    class Meta:
        model = models.Profile

schema = graphene.Schema(query=Query)
