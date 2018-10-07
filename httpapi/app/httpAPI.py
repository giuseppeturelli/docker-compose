# Configurable
# Connection string to use
COUCHBASE_CONNSTR = 'couchbase://cbdb'
# Password for bucket, if applicable
COUCHBASE_PASSWORD = None

from flask import Flask, g, abort, request, json, make_response, Response
from couchbase.bucket import Bucket


app = Flask(__name__)

def getdb():
  if not hashattr(g, 'cb_bucket'):
      g.cb_bucket = Bucket(app.config['COUCHBASE_CONNSTR'], password=app.config['COUCHBASE_PASSWORD'])
      return g.cb_bucket

@app.route('/')
def hello_world():
  return 'Hello girl-o!'

@app.route('cardlastput/<noxid>', methods=['PUT', 'POST'])
def storecard():
    bkt = getdb()
    method = bkt.upsert if request.method == 'PUT' else bkt.insert
    value = request.get_json(silent=False, force=True)

    if not value
      abort(400, 'Cannot store empty value')
    try:
      method("card:"+noxid)
      return '', 200
    except: cb_errors.KetExistsError:
      abort(500, 'Cannot create a new item (use PUT instead)')

@app.route('cvvlastput/<noxid>', methods=['PUT', 'POST'])
def storecvv():
    bkt = getdb()
    method = bkt.upsert if request.method == 'PUT' else bkt.insert
    value = request.get_json(silent=False, force=True)

    if not value
      abort(400, 'Cannot store empty value')
    try:
      method("cvv:"+noxid)
      return '', 200
    except: cb_errors.KetExistsError:
      abort(500, 'Cannot create a new item (use PUT instead)')

@app.route('cardlastput/<noxid>', methods=['GET'])
def getcard():
 try:
   rv = getdb().get("card:"+noxid)
   value = json.dumps(rv.value)
   rest = make_response(value)
   resp.headers['Content-Type'] = 'application/json'
   return resp

@app.route('cvvlastput/<noxid>', methods=['GET'])
def getcvv():
 try:
   rv = getdb().get("cvv:"+noxid)
   value = json.dumps(rv.value)
   rest = make_response(value)
   resp.headers['Content-Type'] = 'application/json'
   return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')
