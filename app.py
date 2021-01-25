from flask import Flask, render_template


app =  Flask(__name__)


@app.route('/')
def landing():
   landing = "active"
   return render_template('landing.html', landing=landing)

@app.route('/logIn')
def logIn():
   return ('logIn')

@app.route('/SigIn')
def SigIn():
   return ('SigIn')

@app.route('/program')
def program():
   program = "active"
   return render_template('program.html', program=program)


if __name__ == "__main__":
    app.run(debug=True, port=4000)