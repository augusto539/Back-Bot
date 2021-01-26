from flask import Flask, render_template, request, redirect, url_for


app =  Flask(__name__)


@app.route('/')
def landing():
   landing = "active"
   return render_template('landing.html', landing=landing)

@app.route('/logIn')
def logIn():
   logIn="active"
   return render_template("logIn.html", logIn=logIn)


@app.route('/SigIn', methods=["GET", "POST"])
def SigIn():

   if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(name, email, password)

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('landing'))

   SigIn="active"
   return render_template("SigIn.html", SigIn=SigIn)


@app.route('/program', methods=["GET", "POST"])
def program():

   if request.method == 'POST':
        name = request.form['name']
        massage = request.form['massage']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        _filter = request.form['_filter']

        print(name, massage, start_time, end_time, _filter)

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('landing'))

   program = "active"
   return render_template('program.html', program=program)


if __name__ == "__main__":
    app.run(debug=True, port=4000)