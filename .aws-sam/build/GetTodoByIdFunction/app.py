from todo_common import table, create_response

def lambda_handler(event, context):
    try:
        # パスパラメータからIDを取得
        todo_id = event['pathParameters']['id']
        
        # DynamoDBから指定されたIDのToDoを取得
        response = table.get_item(Key={'id': todo_id})
        
        # アイテムが見つからない場合は404エラー
        if 'Item' not in response:
            return create_response(404, {'error': 'Todo not found'})
        
        return create_response(200, response['Item'])
    except Exception as e:
        print(f"Error: {str(e)}")
        return create_response(500, {'error': 'Error fetching todo'})
