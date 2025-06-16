from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'jhasdfaslkj;d;skaojshdasdasdsfhgjhg;ohi'

@app.route('/')
def index():
    user_agent = request.user_agent.string
    if 'Mobile' in user_agent or 'Android' in user_agent or 'iPhone' in user_agent:
        return render_template('index_phone.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)