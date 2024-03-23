'''Sample web app to test a database connection'''
from flask import Flask
from flask import Flask, jsonify
import pymysql

def hardcoded_credentials():
    return dict(username='username', password='password', host='rds-endpoint')


def configure_app(credentials):
    return pymysql.connect(
        host=credentials['host'],
        user=credentials['username'],
        password=credentials['password'],
        database='information_schema'
    )

app = Flask(__name__)


@app.route('/')
def db_connect():
    credentials = hardcoded_credentials()
    try:
        conn = configure_app(credentials)
        # If connection is successful, return a success message
        return jsonify(db_status="CONNECTED", credentials=credentials)
    except Exception as e:
        # If there's an error, return an error message
        return jsonify(db_status="DISCONNECTED", error_message=str(e))


if __name__ == '__main__':
    # Make the server publicly available by default
    app.run(debug=True, host='0.0.0.0')
