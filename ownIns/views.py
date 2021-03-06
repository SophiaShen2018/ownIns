from ownIns import app, db
from ownIns.models import Image, User
from flask import render_template, redirect


@app.route('/')
def index():
    images = Image.query.order_by(db.desc(Image.id)).limit(10).all()
    return render_template('index.html', images=images)


@app.route('/profile/<int:user_id>/')
def profile(user_id):
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)


@app.route('/image/<int:image_id>/')
def image(image_id):
    image = Image.query.get(image_id)
    return render_template('pageDetail.html', image=image)
