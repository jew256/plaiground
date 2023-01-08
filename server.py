from flask import Flask, request, jsonify, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask_cors import CORS
import openai
import subprocess
import time
# import config
import os

app = Flask(__name__)
CORS(app)

# openai.api_key = config.OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.openai.com/v1"

@app.route("/", methods=['GET'])
def root():
    return jsonify({'message': 'Welcome to the party'})    

@app.route("/code", methods=['POST'])
def code_call():
    code_json = request.get_json()
    response = {"responses": []}
    scripts = []
    i = 0
    for message in code_json.values():
        req = f"""
\"\"\"
wrap in a try, except. if the request succeeds, write "Successful" to `output{i}.txt`
in the except case, instead graph an error symbol and write 'Error: ', and the error to `output{i}.txt`
also in the except case, write a hint for a better prompt to `output.txt`
make the dates readable
the free version is being used, do not use premium features.
make sure to plot data for the requested period, if given
1. use the yahoo finance api to get any stock data
2. Create a figure and set the style to dark
3. {message}
4. Add axes, title, and legend
5. Save the graph as test{i}.png
6. Close the graph automatically
\"\"\""""

        print(req)
        completion = openai.Completion.create(engine="text-davinci-003", prompt=req, max_tokens=2000, temperature=0)
        scripts.append(completion.choices[0].text)
        print(completion.choices[0].text)
        i += 1
        time.sleep(0.1)
    for j in range(i):
        f = open(f"test{j}.py", "w")
        f.write(scripts[j])
        f.close()
        response["responses"].append(str(j))
    return jsonify(response)
    
@app.route('/plot<id>', methods=['GET'])
def plot_png(id):
    subprocess.call(["python", f"test{id}.py"])
    return send_file(f"test{id}.png", mimetype='image/png')

@app.route('/output', methods=['GET'])
def output():
    with open('output.txt', 'r') as f:
        text = f.read() 
    return text

if __name__ == "__main__":
    app.run(debug=True)