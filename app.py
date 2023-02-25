from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/test', methods={'GET', "POST"})
def mytestfunction():
    if request.method == 'GET':
        return jsonify("Helloooo")
    else:
        input_json = request.json
        x=input_json['x']
        y=input_json['y']
        output={
            "function" : "2*sum",
            "result" : x+y+x+y
        }
        return jsonify(output)
    
if __name__== '__main__':
    app.run('0.0.0.0',port=8409)