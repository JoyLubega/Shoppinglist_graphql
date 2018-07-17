import graphene

from graphene_django.types import DjangoObjectType

from shoppinglists.models import Shoppinglist, Item


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

    def mutate(self, info, **kwargs):
        shoppinglist = Shoppinglist(**kwargs)
        shoppinglist.save()

        return CreateShoppinglist(shoppinglist=shoppinglist)

class Query(object):
    all_shoppinglists = graphene.List(ShoppinglistType)
    all_items = graphene.List(ItemType)

    def resolve_all_shoppinglists(self, info, **kwargs):
        return Shoppinglist.objects.all()

    def resolve_all_items(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Item.objects.select_related('shoppinglist').all()

class Mutation(graphene.ObjectType):
    create_shoppingliist = CreateShoppinglist.Field()