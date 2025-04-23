from app import create_app
import awsgi

app = create_app()

@app.route("/health")
def health():
    return "OK", 200

def lambda_handler(event, context):
    return awsgi.response(app, event, context)