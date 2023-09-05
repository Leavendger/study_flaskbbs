HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'pythonbbs'
USERNAME = 'root'
PASSWORD = '1234'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,
                                                                                           password=PASSWORD,
                                                                                           host=HOSTNAME, port=PORT,
                                                                                           db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
