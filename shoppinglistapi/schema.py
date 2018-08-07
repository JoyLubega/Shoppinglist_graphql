import graphene
import graphql_jwt

import shoppinglists.schema
import User.schema


class Query(User.schema.Query,shoppinglists.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    shoppinglists.schema.Mutation,
    User.schema.Mutation,
    graphene.ObjectType
):
    login_user = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)