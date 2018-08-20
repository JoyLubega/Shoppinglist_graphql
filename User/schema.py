from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email,last_name,first_name):
        user = get_user_model()(
            username=username,
            email=email,
            last_name=last_name,
            first_name=first_name
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged!')
        return user

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()