# study_flaskbbs
用于自己学习的一个库,主要跟新自己学习flask,尝试进行实战开发

### v0.1 
配置了flask连接映射数据库的基本配置,并且建立了用户的数据模型

在`config.py`中更改连接数据库相关配置,并在数据库中创建对应的`DATABASE`
并在app.py中配置`migrate = Migrate(app, db)`
并且通过
* 将ORM模型映射到数据库中三部曲
* 0. migrate = Migrate(app, db)
* 1. flask db init
* 2. flask db migrate
* 3. flask db upgrade
来映射到数据库即可
