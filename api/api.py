# Import the flask library to make code available to entire app
import flask
from flask import request, jsonify

# Create Flask app object
app = flask.Flask(__name__)

# Start the debugger
app.config["DEBUG"] = True 

#Test data for catalog, each object in the list is called a dictionary
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


# Set the api path and method to be received on that path
@app.route('/', methods=['GET'])
def home():
  # This is what will be rendered when the http GET is called
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# Route to return all available entries in our catalog:
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
  return jsonify(books)


# GET data by specific ID:
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
  #if ID is provided as part of URL, then assign it to a variable
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