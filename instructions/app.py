import os
import psycopg2
from flask import Flask, jsonify, Response, request, render_template
from flask_cors import cross_origin


app = Flask(__name__)

# Get database credentials from environment variables
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']
db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']

# Add CORS header to responses
@app.after_request
def add_cors_header(response):
    allowed_origins = ['http://localhost:3000', 'https://example.com']
    if request.headers.get('Origin') in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,privatekey'
    response.headers['Access-Control-Expose-Headers'] = 'Content-Type,Authorization,privatekey'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

# Define route to display data
@app.route('/temp')
def display_data():
    # Connect to Postgres database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    # Query database for data
    cur = conn.cursor()
    cur.execute("SELECT time, value FROM \"CM_HAM_DO_AI1/Temp_value\"")
    data = cur.fetchall()

    conn.close()

    # Convert data to array of objects and return response
    return jsonify([{'time': row[0], 'value': row[1]} for row in data])

@app.route('/ph')
def display_data2():
    # Connect to Postgres database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    # Query database for data
    cur = conn.cursor()
    cur.execute("SELECT time, value FROM \"CM_HAM_PH_AI1/pH_value\"")
    data = cur.fetchall()

    conn.close()

    # Convert data to array of objects and return response
    return jsonify([{'time': row[0], 'value': row[1]} for row in data])

@app.route('/oxygen')
def display_data3():
    # Connect to Postgres database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    # Query database for data
    cur = conn.cursor()
    cur.execute("SELECT time, value FROM \"CM_PID_DO/Process_DO\"")
    data = cur.fetchall()

    conn.close()

    # Convert data to array of objects and return response
    return jsonify([{'time': row[0], 'value': row[1]} for row in data])

@app.route('/pressure')
def display_data4():
    # Connect to Postgres database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    # Query database for data
    cur = conn.cursor()
    cur.execute("SELECT time, value FROM \"CM_PRESSURE/Output\"")
    data = cur.fetchall()

    conn.close()

    # Convert data to array of objects and return response
    return jsonify([{'time': row[0], 'value': row[1]} for row in data])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)