lemail = []
ltask =[]
lpriority=[]

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    lemailhtml = lemail
    ltaskhtml = ltask
    lpriorityhtml = lpriority

    return render_template('index.html', ltaskhtml=ltaskhtml, lemailhtml=lemailhtml, lpriorityhtml=lpriorityhtml)

from flask import request, redirect

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    task = request.form['task']
    priority = request.form['priority']
    lemail.append(email)
    ltask.append(task)
    lpriority.append(priority)
    print("Values added")
    return redirect('/')


from flask import request, redirect


@app.route('/cleanup/', methods=['POST'])
def cleanup():
    global lemail
    global ltask
    global lpriority

    lemail = []
    ltask = []
    lpriority = []
    # cleanallvalues()
    print("Cleanup attempted")

    return redirect('/')

if __name__ == "__main__":
    app.run()