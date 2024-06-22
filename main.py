
from flask import Flask, render_template, request
import gemini

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    client = gemini.Client()
    response = client.text_generation(
        prompt=question,
        length=256,
        temperature=0.7,
        top_p=1.0,
        stop=['\n'],
    )
    return render_template('index.html', answer=response.candidates[0].output)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
