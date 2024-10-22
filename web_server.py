from flask import Flask, request
from manager import EntryManager
from  resources import Entry

app = Flask(__name__)
FOLDER = '/users/dmitry/tmp/'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route("/api/entries/")
def get_entries():
    entry = EntryManager(FOLDER)
    entry.load()
    new_list = []
    for i in entry.entries:
        i = i.json()
        new_list.append(i)
    return new_list

@app.route("/api/save_entries/", methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    json = request.get_json()
    for i in json:
        entry = Entry.from_json(i)
        entry_manager.entries.append(entry)
        entry_manager.save()
    return {'status': 'success'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

# Some text