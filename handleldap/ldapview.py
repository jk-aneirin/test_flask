from flask import Flask,render_template,request,url_for,redirect
from ldapcontroll import OperateLdap

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    global username
    if request.method=='POST':
        username=request.form['u']
        pwd=request.form['p']
        o=OperateLdap('server3.wm.org',username,pwd)
        if o.succeed:
            return redirect(url_for('updatepwd'))
        else:
            return "Wrong Password or User name does not Exist!"
    else:
        return render_template('index.html')

@app.route('/updatepwd',methods=['GET','POST'])
def updatepwd():
    global username
    if request.method=='POST':
        if request.form['pwd1']==request.form['pwd2']:
            finalpwd=request.form['pwd2']
            conn=OperateLdap('server3.wm.org','admin','123456')
            if username=="":
                return redirect(url_for('index'))
            else:
                conn.ModifyPwd(username,finalpwd)
            return "Update the password successfully!"
        else:
            return render_template('updatepwd.html')

    return render_template('updatepwd.html')
if __name__=='__main__':
    username=""
    app.run(host='0.0.0.0')


