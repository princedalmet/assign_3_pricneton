from flask import Flask

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello_ecs():
    # Response message
    return 'Hello from princeton ECS Container!'

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Use port 5000 as defined in Dockerfile
