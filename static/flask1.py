from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/Success/<int:score>')
def Success(score):
    return render_template('result.html', outcome='pass', score=score)

@app.route('/Fail/<int:score>')
def Fail(score):
    return render_template('result.html', outcome='fail', score=score)

@app.route('/result/<int:marks>')
def result(marks):
    outcome = "Success" if marks > 50 else "Fail"
    return redirect(url_for(outcome, score=marks))

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        eng = float(request.form['English'])
        math = float(request.form['Maths'])
        phy = float(request.form['Physics'])
        pl = float(request.form['Programming Language'])
        isl = float(request.form['Islamiat'])
        totalscores = (eng + math + phy + pl + isl) / 5
        result = "Success" if totalscores >= 50 else "Fail"
        return redirect(url_for(result, score=int(totalscores)))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
