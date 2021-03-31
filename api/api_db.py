# Import the flask library to make code available to entire app
import flask
from flask import request, jsonify
import psycopg2

# Create Flask app object
app = flask.Flask(__name__)

# Start the debugger
app.config["DEBUG"] = True 


# Connect to PG db
# conn = psycopg2.connect("dbname=books_db user=postgres password=postgres")
conn = psycopg2.connect(
  host="localhost",
  port=5432,
  database="books_db",
  # user="postgres",
  # password="postgres"
)

def connect():
  conn = None
  try:
    params = config()
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    print(db_version)

    cur.close()

  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  finally:
    if conn is not None:
      conn.close()
      print('Database connection closed.')

if __name__ == '__main__':
  connect()

# Define data that will come back from db (SQLite)
# def dict_factory(cursor, row):
#   d = {}
#   for idx, col in enumerate(cursor.description):
#     d[col[0]] = row[idx]
#   return d


# Set the api path and method to be received on that path
@app.route('/', methods=['GET'])
def home():
  # This is what will be rendered when the http GET is called
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# Route to return all available entries in our catalog:
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
  return jsonify(books)


# GET data by specific ID: (id is provided by ?id=0)
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
 


  # if ID is provided as part of URL, then assign it to a variable
  if 'id' in request.args:
      id = int(request.args['id'])
  else:  #Otherwise, display an error in the browser
      return "Error: No ID field provided."

  results = []  # Empty list to store results


# Loop through data and match results that fit requested ID.
  for book in books:
    if book['id'] == id:
      results.append(book)

# Use Flask jsonify function to convert list of Python distonaries to JSON
  return jsonify(results)


# Method (object function) to tell app server to run
app.run()