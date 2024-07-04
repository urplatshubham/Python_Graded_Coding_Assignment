"""Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

●       The program should read a configuration file (you can provide them with a sample configuration file).

●       It should extract specific key-value pairs from the configuration file.

●       The program should store the extracted information in a data structure (e.g., dictionary or list).

●       It should handle errors gracefully in case the configuration file is not found or cannot be read.

●       Finally save the output file data as JSON data in the database.

●       Create a GET request to fetch this information.

Sample Configuration file: 

[Database]

host = localhost

port = 3306

username = admin

password = secret

 

[Server]

address = 192.168.0.1

port = 8080

 

Sample Output: 

Configuration File Parser Results:

Database:

- host: localhost

- port: 3306

- username: admin

- password: secret

 

Server:

- address: 192.168.0.1

- port: 8080 

"""
import yaml as y
import json
import sqlite3
def read_config_file():
        
        try:
            #1. reading the file
            with open('config.yml', 'r') as configfile:
                
                config_data = y.safe_load(configfile)

            kv_pairs = {}
            for k,v in config_data.items():
            #2. extracting key-value pairs from the config file
                kv_pairs[k] = v #3. storing in an empty dictionary
        
            return kv_pairs
        except Exception(FileNotFoundError):
            print("Configuration file not found!")
            return None
    
def put_jsonfile_toDB():

    kv_pair=read_config_file()
    kv_pairs_json = json.dumps(kv_pair)#5. converting the dictionary data to json data
    
    print("Dictionary data converted to JSON string successfully")

    try:
        conn = sqlite3.connect('Project_DB.db')
        print("Establishing connection with Database")
        cursor = conn.cursor()
    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Project_DB_table (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   section TEXT,
                   key TEXT,
                   value TEXT) 
        ''') #creating a table if it does not exist with columns of id, section, key and value
        print("Database Table created")

        cursor.execute('INSERT INTO Project_DB_table (section, key, value) VALUES (?, ?, ?)',
                       ('Database', 'config_data', kv_pairs_json)) 
                    #cont. 5. putting json data into database 

        conn.commit()
        print("Data inserted successfully into the Database")
    except sqlite3.Error as e:
        
        print(f"An error occurred while connecting with the database: {e}")
    finally:
        if conn:
            
            conn.close()
     
    

def main():
    put_jsonfile_toDB()
        
if __name__ == "__main__":
    main()
    



    


