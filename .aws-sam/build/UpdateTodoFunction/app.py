import json
from todo_common import table, create_response, get_timestamp

def lambda_handler(event, context):
    try:
        # パスパラメータからIDを取得
        todo_id = event['pathParameters']['id']
        
        # リクエストボディを取得
        body = json.loads(event['body']) if event.get('body') else {}
        
        # 既存のToDoを確認
        response = table.get_item(Key={'id': todo_id})
        if 'Item' not in response:
            return create_response(404, {'error': 'Todo not found'})
        
        # 更新式の構築
        update_expression = "SET "
        expression_values = {}
        
        if 'title' in body:
            update_expression += "title = :title, "
            expression_values[':title'] = body['title']
        
        if 'completed' in body:
            update_expression += "completed = :completed, "
            expression_values[':completed'] = body['completed']
        
        update_expression += "updatedAt = :updatedAt"
        expression_values[':updatedAt'] = get_timestamp()
        
        # DynamoDBを更新
        response = table.update_item(
            Key={'id': todo_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ReturnValues="ALL_NEW"
        )
        
        return create_response(200, response['Attributes'])
    except Exception as e:
        print(f"Error: {str(e)}")
        return create_response(500, {'error': 'Error updating todo'})
