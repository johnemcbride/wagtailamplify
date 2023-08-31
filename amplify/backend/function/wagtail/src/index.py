import mysite.wsgi
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))


def handler(event, context):
    # print('received event:')
    # print(event)
    #
    # return {
    #     'statusCode': 200,
    #     'headers': {
    #         'Access-Control-Allow-Headers': '*',
    #         'Access-Control-Allow-Origin': '*',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    #     },
    #     'body': json.dumps('Hello from your new Amplify Python lambda!')
    # }
    from apig_wsgi import make_lambda_handler
    _real_handler = make_lambda_handler(mysite.wsgi.application)

    return _real_handler(event, context)
