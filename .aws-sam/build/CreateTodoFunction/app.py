import json
from todo_common import table, create_response, generate_todo_id, get_timestamp

def lambda_handler(event, context):
    try:
        # リクエストボディを取得
        body = json.loads(event['body']) if event.get('body') else {}
        
        # タイトルがなければエラー
        if 'title' not in body:
            return create_response(400, {'error': 'Title is required'})
        
        # 新しいToDoアイテムを作成
        todo_id = generate_todo_id()
        new_todo = {
            'id': todo_id,
            'title': body['title'],
            'completed': False,
            'createdAt': get_timestamp()
        }
        
        # DynamoDBに保存
        table.put_item(Item=new_todo)
        
        return create_response(201, new_todo)
    except Exception as e:
        print(f"Error: {str(e)}")
        return create_response(500, {'error': 'Error creating todo'})
