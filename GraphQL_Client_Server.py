from graphene import ObjectType, String, Schema

'''Very basic GraphQL Server '''

class Query(ObjectType):
	hello = String(name=String(default_value='not the world'))
	goodbye = String()
	def resolve_hello(root, info, name):
		return f'Hello {name}'
	def resolve_goodbye(root, info):
		return 'See ya'

# Create an instance of the 'Query' class

schema = Schema(query=Query)

'''Very basic GraphQL Client '''

query_with_argument = '{ hello(name: "World") }'
result = schema.execute(query_with_argument)
print(result.data['hello'])