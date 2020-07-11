class Loggable:
    def __init__(self):
        self.title=''
    def log(self):
        print('Log message from '+ self.title)

class Connection:
    def __init__(self):
        self.server=''
    def connect(self):
        print('Connecting to DB on '+self.server)

class sqlDB(Connection,Loggable):
    def __init__(self):
        super().__init__()
        self.title='Sql connction'
        self.server='an amazing Server'

def framework(item):
    if isinstance(item,Connection):
        item.connect()
    elif isinstance(item, Loggable):
        item.log()

SQL=sqlDB()
framework(SQL)

print()
log=Loggable()
log.title='aaa'
con=Connection()
con.server='bbb'

framework(log)
framework(con)