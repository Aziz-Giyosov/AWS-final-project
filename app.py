from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database credentials (replace with your actual values if different)
DB_HOST = "db-aziz.ct6ei6agkus4.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres" # Make sure this is correct
TABLE_NAME = "travel_destinations"

def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

@app.route('/destinations', methods=['GET'])
def get_destinations():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        # Use the actual column names from your table
        cur.execute(f"SELECT city, country, category, best_time_to_travel FROM {TABLE_NAME};")
        destinations = cur.fetchall()
        cur.close()
        conn.close()
        destination_list = []
        for dest in destinations:
            destination_list.append({
                'destination': dest[0], # 'city' from DB maps to 'destination' in JSON
                'country': dest[1],
                'category': dest[2],
                'best_time_to_travel': dest[3]
            })
        return jsonify(destination_list)
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

@app.route('/destinations', methods=['POST'])
def add_destination():
    data = request.get_json()
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        try:
            # Use the actual column names from your table
            cur.execute(f"INSERT INTO {TABLE_NAME} (city, country, category, best_time_to_travel) VALUES (%s, %s, %s, %s);",
                        (data.get('city'), data.get('country'), data.get('category'), data.get('best_time_to_travel')))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'message': 'Destination added successfully'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cur.close()
            conn.close()
            return jsonify({'error': f'Error adding destination: {e}'}), 500
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

@app.route('/destinations/<string:destination_name>', methods=['DELETE'])
def delete_destination(destination_name):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        try:
            # Use 'city' as the identifier for deletion
            cur.execute(f"DELETE FROM {TABLE_NAME} WHERE city = %s;", (destination_name,))
            conn.commit()
            cur.close()
            conn.close()
            if cur.rowcount > 0:
                return jsonify({'message': f'Destination "{destination_name}" deleted successfully'}), 200
            else:
                return jsonify({'message': f'Destination "{destination_name}" not found'}), 404
        except psycopg2.Error as e:
            conn.rollback()
            cur.close()
            conn.close()
            return jsonify({'error': f'Error deleting destination: {e}'}), 500
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
