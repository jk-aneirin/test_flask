from flask import Flask,Response,redirect,url_for,request,session,abort
from flask_login import LoginManager,login_required,\
        login_user,logout_user
from models import User
app = Flask(__name__)

app.config.update(
        DEBUG = True,
        SECRET_KEY = '?><12342'
        )

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

users = [User(id) for id in range(1,21)]

@app.route('/')
@login_required
def admin():
    return Response("This is admin page!")

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']
        if pwd == username + '_password':
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
            <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=pwd>
            <p><input type=submit value=Login>
            </form>
            ''')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@lm.user_loader
def load_user(userid):
    return User(userid)

if __name__ == "__main__":
    app.run(host='0.0.0.0')



