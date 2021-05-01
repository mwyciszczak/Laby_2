from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


class Movies:
    def __init__(self, name):
        self.engine = create_engine("sqlite:///{}.db".format(name), echo=True)
        self.meta = MetaData()
        self.table = Table(
            '{}'.format(name), self.meta,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('director', String),
            Column('actors', String),
            Column('vod', String),
            sqlite_autoincrement=True)
        self.meta.create_all(self.engine)

    def delete_movie(self, title):
        conn = self.engine.connect()
        stmt = self.table.delete().where(self.table.c.title == title)
        conn.execute(stmt)
        s = self.table.select()
        conn.execute(s).fetchall()

    def add_movie(self, titl, dirr, acto, vodd):
        ins = self.table.insert().values(title=titl, director=dirr, actors=acto, vod=vodd)
        conn = self.engine.connect()
        result = conn.execute(ins)

    def show_movies(self):
        conn = self.engine.connect()
        s = self.table.select()
        result = conn.execute(s)
        for row in result:
            print("Film o tytule {}, w reżyserii {}, z {} dostępny na {}".format(row[1], row[2], row[3], row[4],))

    def update_movie(self, titl, ntitle, ndir, nactor, nvod):
        conn = self.engine.connect()
        stmt = self.table.update().where(self.table.c.title == titl).values(title=ntitle, director=ndir, actors=nactor, vod=nvod)
        conn.execute(stmt)
        s = self.table.select()
        conn.execute(s).fetchall()


t = Movies("filmy")
#t.add_movie('tytul', 'rezyser', 'akotrzy', 'tak')
t.show_movies()
t.update_movie('tytul', 'nowy tytul', 'nowy rezyser', 'nowi aktorzy', 'nowe vod')
t.show_movies()




