from todo_common import table, create_response

def lambda_handler(event, context):
    try:
        # DynamoDBからすべてのToDoを取得
        response = table.scan()
        items = response.get('Items', [])
        
        return create_response(200, {'todos': items})
    except Exception as e:
        print(f"Error: {str(e)}")
        return create_response(500, {'error': 'Error fetching todos'})
