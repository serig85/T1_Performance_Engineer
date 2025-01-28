from flask import Flask, request
import json
server_port = 5000
app = Flask(__name__)

@app.route('/stub', methods=['POST'])
def zadacha():
    jdata = request.data
    data = json.loads(jdata)
    return obhod(data)

def obhod(json_arg):
    for i in json_arg:
        if i == 'age':
           json_arg[i] = 96
        if type(json_arg) not in [dict, list, tuple]:
            continue
        if type(json_arg) == list:
            for l in json_arg:
                if type(l) in [dict, list, tuple]:
                    obhod(l)
            continue
        if type(json_arg[i]) in [dict, list, tuple]:
            obhod(json_arg[i])
    return json.dumps(json_arg, ensure_ascii= False)



if __name__ == "__main__":
    meteo = ''
    s ='no_data'
    count = 0
    app.run('0.0.0.0',port=server_port)