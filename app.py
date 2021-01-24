from flask import Flask, render_template


app =  Flask(__name__)


@app.route('/')
def landing():
   return render_template('landing.html')

@app.route('/logIn')
def logIn():
   return ('logIn')

@app.route('/SigIn')
def SigIn():
   return ('SigIn')

@app.route('/program')
def programar():
   return render_template('program.html')


if __name__ == "__main__":
    app.run(debug=True, port=4000)