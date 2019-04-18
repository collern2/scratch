from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <center>
                <br>{0}<br>
            </center>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = "Hello Rhodes 2019!"
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
