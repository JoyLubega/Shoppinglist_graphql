import graphene
from graphql import GraphQLError

from graphene_django.types import DjangoObjectType

from shoppinglists.models import Shoppinglist, Item
from User.schema import UserType


class ShoppinglistType(DjangoObjectType):
    class Meta:
        model = Shoppinglist


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class CreateShoppinglist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        
    shoppinglist = graphene.Field(ShoppinglistType)
    created_by = graphene.Field(UserType)

    def mutate(self, info, name,description):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Please log in and get a token')

        shoppinglist = Shoppinglist(name=name,description=description,created_by=user)

        shoppinglist.save()

        return CreateShoppinglist(shoppinglist=shoppinglist)

class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        shoppinglist_id = graphene.Int(required=True)

        
    item = graphene.Field(ItemType)
    created_by = graphene.Field(UserType)

    def mutate(self, info, name,shoppinglist_id):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Please log in and get a token')

        item = Item(name=name,shoppinglist_id=shoppinglist_id,created_by=user)
        item.save()
        return CreateItem(item=item)

class Query(object):
    all_shoppinglists = graphene.List(ShoppinglistType)
    all_items = graphene.List(ItemType)

    def resolve_all_shoppinglists(self, info, **kwargs):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Pleaselog in and get a token')
        return Shoppinglist.objects.filter(created_by=user)

    def resolve_all_items(self, info, **kwargs):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Pleaselog in and get a token')
        # We can easily optimize query count in the resolve method
        return Item.objects.select_related('shoppinglist').filter(created_by=user)

class Mutation(graphene.ObjectType):
    create_shoppingliist = CreateShoppinglist.Field()
    create_item= CreateItem.Field()