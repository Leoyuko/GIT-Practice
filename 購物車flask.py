pip3 install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"""<h1>購物車shopping<h1> 
<p>商品清單</p >
<p>Smart Watch</p > 
<p>Wallet</p >
<p>Headphone</p >
<p>Digital Camera</p >
"""

if __name__=="__main__":
    app.run()

