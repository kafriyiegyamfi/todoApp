#from flask import Flask
# 
#app = Flask(__name__)
# 
#@app.route('/')
#def index():
#    return 'Hello world'
#
#@app.route('/whereami')
#def whereami():
#    return 'Ghana!'
#
#
from flask import *
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('form.html',items=items)

items =[]
#@app.route('/foo/<name>')
#def foo(name):
#    return render_template('index.html',to=name)
@app.route('/todo')
def add_todo():
    item= request.args.get("item")
    print(item)
    items.append(item)
    return redirect("http://localhost:5000/",code=302)

@app.route('/get_todos')
def get_todos():
    resp= Reponse(json.dumps(items))
    resp.header['Contents-Type']="application/json"
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    