import graphene

import shoppinglists.schema


class Query(shoppinglists.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    shoppinglists.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)