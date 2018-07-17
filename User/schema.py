from User.models import User

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        FirstName = graphene.String(required=True)
        LastName = graphene.String(required=True)
        UserName = graphene.String(required=True)
        Password = graphene.String(required=True)
        Email = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        print(kwargs)
        user = User(**kwargs)
        # user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()