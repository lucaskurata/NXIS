from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('C:/Users/Kurata/Desktop/fornecedor.html', methods=['GET', 'POST'])
def form():
    return render_template('fornecedor.html')

@app.route('/processa-fornecedor', methods=[ 'POST'])
def hello():
    return render_template('processa-fornecedor.html')

if __name__ == "__main__":
    app.run()