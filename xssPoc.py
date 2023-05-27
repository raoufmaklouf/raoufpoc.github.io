from flask import Flask

app = Flask(__name__)

@app.route('/gtoken')
def gtoken():
    return '<script>alert(document.domain)</script>'

if __name__ == '__main__':
    app.run()
    
   
