#coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://edmon:redhat@127.0.0.1:8888/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

#会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)    #编号
    name = db.Column(db.String(100), unique=True)   #昵称
    pwd = db.Column(db.String(100))                  #密码
    email = db.Column(db.String(100), unique=True)  #邮箱
    phone = db.Column(db.String(11), unique=True)   #手机
    info = db.Column(db.Text)                        #个人简介
    face = db.Column(db.String(255))                 #头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)   #添加时间
    uuid = db.Column(db.String(255), unique=True)   #唯一标识符
    userlogs = db.relationship('UserLog', backref='user')
    comments = db.Column(db.relationship("Comment", backref='user'))
    moviecols = db.Column(db.relationship("MovieCol", backref='user'))

    def __repr__(self):
        return '<User %r>' % self.name


#会员登录日志
class UserLog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)                 #编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #所属用户
    ip = db.Column(db.String(100))                               #登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)    #日志添加时间

    def __repr__(self):
        return '<UserLog %r>' % self.id


#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)    #编号
    name = db.Column(db.String(100), unique=True)   #标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    movies = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return '<Tag %r>' % self.name


#电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)    #编号
    title = db.Column(db.String(255), unique=True)  #标题
    url = db.Column(db.String(255), unique=True)    #链接
    info = db.Column(db.Text)                        #简介
    logo = db.Column(db.String(255), unique=True)   #封面
    star = db.Column(db.SmallInteger)                #星级
    playnum = db.Column(db.BigInteger)               #播放量
    commentnum = db.Column(db.BigInteger)            #评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id')) #所属标签
    area = db.Column(db.String(255))    #上映地区
    release_time = db.Column(db.Date)   #上映时间
    length = db.Column(db.String(100))  #电影时长
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)   #添加时间
    comments = db.Column(db.relationship("Comment", backref='movie'))
    moviecols = db.Column(db.relationship("MovieCol", backref='movie'))

    def __repr__(self):
        return  '<Movie %r>' % self.title


#上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)    #编号
    title = db.Column(db.String(255))                #标题
    logo = db.Column(db.String(255))                 #封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)   #添加时间

    def __repr__(self):
        return '<Preview %r>' % self.title


#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)    #编号
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.content


#电影收藏
class MovieCol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)    #编号
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.content