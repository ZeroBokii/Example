'''
    Web运行时,flask程序运行起来,用户通过浏览器访问
    离线脚本,自定义的一个py文件+使用flask中定义好的功能
'''

from script import create_app, db

app = create_app()
with app.app_context():
    db.drop_all()
    # db.create_all()
    # data = db.session.query(models.Users).all()
    # print(data)