"""
hello: Mimimal Python-Flask webapp
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    """Hello Python"""
    return 'Hello, python!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
