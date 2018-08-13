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

class UpdateShoppinglist(graphene.Mutation):
    class Arguments:
        list_id= graphene.Int(required=True)
        new_name = graphene.String(required=True)
        new_description = graphene.String(required=True)
    shoppinglist = graphene.Field(ShoppinglistType)   

    def mutate(self, info,new_name, new_description,list_id):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Please log in and get a token')
        existing_shoppinglist=Shoppinglist.objects.get(id=list_id)
        if not existing_shoppinglist :
            raise GraphQLError('There is no shoppinglist with id: ' + str(list_id))
        existing_shoppinglist.name=new_name
        existing_shoppinglist.description=new_description
        existing_shoppinglist.save()
        print(existing_shoppinglist.description)
        return UpdateShoppinglist(shoppinglist=existing_shoppinglist)

            


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
    shoppinglist = graphene.List(ShoppinglistType, id= graphene.Int())

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

    def resolve_shoppinglist(self, info, **kwargs):
        user= info.context.user
        if user.is_anonymous:
            raise GraphQLError('User not logged in!! Pleaselog in and get a token')
        exact_shoppinglist= Shoppinglist.objects.filter(id=kwargs['id'])
        
        # if exact_shoppinglist:
        #     raise GraphQLError('No shoppinglist with id: '+ str(kwargs['id'])
        return (Shoppinglist.objects.filter(id=kwargs['id']))

class Mutation(graphene.ObjectType):
    create_shoppinglist = CreateShoppinglist.Field()
    create_item= CreateItem.Field()
    Update_shoppinglist = UpdateShoppinglist.Field()