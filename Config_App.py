from flask import Flask, jsonify, Response
import sqlite3
import json
from pathlib import Path

app = Flask(__name__)

DB = 'Project_DB.db'
def get_dbconnection():
    db_path = Path(DB) 
    try: 
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row  # fetching rows from DB as dictionaires
        return conn
    except Exception(db_path):
        print(f"Database file {DB} does not exist.")

@app.route('/get_config_details', methods=['GET'])#to fetch the json data from an API call
def get_config_details():
    print("API connection successful")
    conn=get_dbconnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Project_DB_table')
    rows=cursor.fetchall() #fetching all the records
    conn.close()

    show_config_data={}
    for r in rows: #fetching all each data in the respective lists
        section= r['section']
        key= r['key']
        value= r['value']

        if section not in show_config_data:
            show_config_data[section]=[]
        try:
            parsed_value = json.loads(value) #loading the value from json to be formatted according to the o/p
            formatted_value = json.dumps(parsed_value, indent=4)
        except json.JSONDecodeError:
            formatted_value = value

        show_config_data[section].append(f"- {key}: {formatted_value}")

    formatted_data = "Configuration File Parser Results:\n\n"
    
    for section, items in show_config_data.items(): #printing as per the output
        formatted_data += f"{section}:\n"
        for item in items:
            formatted_data += f"{item}\n"
        formatted_data += "\n"
    
    return Response(formatted_data, mimetype='text/plain') #returning the response when API requests

@app.route('/check_insert', methods=['GET'])
def check_insert():
    conn = get_dbconnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Project_DB_table')
    rows = cursor.fetchall()
    conn.close()

    if len(rows) > 0:
        return "Data has been inserted into the database."
    else:
        return "No data found in the database."

if __name__ == '__main__':
    print("Starting server....")
    app.run(debug=True)