from todo_common import table, create_response

def lambda_handler(event, context):
    try:
        # パスパラメータからIDを取得
        todo_id = event['pathParameters']['id']
        
        # DynamoDBから削除
        table.delete_item(Key={'id': todo_id})
        
        return create_response(204)
    except Exception as e:
        print(f"Error: {str(e)}")
        return create_response(500, {'error': 'Error deleting todo'})
