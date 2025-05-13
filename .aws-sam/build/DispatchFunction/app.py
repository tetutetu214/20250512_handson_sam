import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Welcome to Lambda-lith ToDo API',
            'endpoints': {
                'GET /todos': 'List all todos',
                'POST /todos': 'Create a new todo',
                'GET /todos/{id}': 'Get a specific todo',
                'PUT /todos/{id}': 'Update a todo',
                'DELETE /todos/{id}': 'Delete a todo'
            }
        })
    }
