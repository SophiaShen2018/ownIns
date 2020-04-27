# -*- encoding=UTF-8 -*-

from ownIns import db
from datetime import datetime
import random


class User(db.Model):
    # ci 大小写敏感
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))
    profile_url = db.Column(db.String(512))
    # images = db.relationship('Image')
    images = db.relationship('Image', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.profile_url = 'https://github.com/SophiaShen2018/ownIns/blob/master/assets/profile' + str(random.randint(1, 5)) + '.jpg'
        self.profile_url = 'http://images.nowcoder.com/head/' + str(random.randint(0, 40)) + 'm.png'
    def __repr__(self):
        return ('<User %d %s>' % (self.id, self.username)).encode('gbk')


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_date = db.Column(db.DateTime)
    comments = db.relationship('Comment')
    # status = db.Column(db.Integer, default=0)  # 0 正常 1 删除

    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image%d %s> % (self.id, self.url)'


class Comment(db.Model):
    # ci 大小写敏感
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(512))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer, default=0) # 0 正常 1 删除
    user = db.relationship('User')

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return ('<Comment %d %s>' % (self.id, self.content)).encode('gbk')