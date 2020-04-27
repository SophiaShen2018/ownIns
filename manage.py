# -*- encoding=UTF-8 -*-

# 脚本

from ownIns import app, db
from flask_script import Manager
from ownIns.models import *
import random

manager = Manager(app)

def get_image_url():
    # return 'https://github.com/SophiaShen2018/ownIns/blob/master/assets/pic' + str(random.randint(1, 2)) + '.jpg'
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 20):
        db.session.add(User('用户'+str(i+1), 'pwd'+str(i+1)))
        for j in range(0, 2):
            db.session.add(Image(get_image_url(), i+1))
            for k in range(0, 5):
                db.session.add(Comment('这是一条评论'+str(k), 1+2*i+j, i+1))
    # 提交事务
    db.session.commit()



if __name__ == '__main__':
    manager.run()