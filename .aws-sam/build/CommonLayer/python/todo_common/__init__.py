import os
import json
import boto3
import decimal
import uuid
from datetime import datetime

# デシマル型をJSONに変換するためのエンコーダ
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

# DynamoDB接続
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('TABLE_NAME', 'PythonTodos'))

# レスポンス作成ヘルパー
def create_response(status_code, body=None):
    response = {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization'
        }
    }
    
    if body is not None:
        response['body'] = json.dumps(body, cls=DecimalEncoder)
        
    return response

# 新しいToDo ID生成
def generate_todo_id():
    return str(uuid.uuid4())

# 現在のタイムスタンプ取得
def get_timestamp():
    return datetime.now().isoformat()
