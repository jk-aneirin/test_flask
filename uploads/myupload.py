from flask import Flask,request,url_for,redirect,render_template,flash,session
from flask_uploads import UploadSet,configure_uploads,IMAGES,UploadNotAllowed

SECRET_KEY = ('\xa3\xb6\x15\xe3E\xc4\x8c\xbaT\x14\xd1:'
                      '\xafc\x9c|.\xc0H\x8d\xf2\xe5\xbd\xd5')

UPLOADED_PHOTOS_DEST = '/tmp/photolog'
app = Flask(__name__)
app.config.from_object(__name__)

uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)


@app.route('/')
def index():
    try:
        imgurl = session['imgurl']
    except:
        imgurl = None
    return render_template('index.html',imgurl = imgurl)

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method == 'POST':
        photo = request.files.get('photo')
        try:
            filename = uploaded_photos.save(photo)
        except UploadNotAllowed:
            flash("upload is not allowed!")
        else:
            session['imgurl'] = uploaded_photos.url(filename)
            return redirect(url_for('index'))
    return render_template('new.html')


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
