from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///rozgrywki.db", echo=True)
meta = MetaData()
druzyny_dict = {
    1: "Chicago Bulls",
    2: "Los Angeles Lakers",
    3: "Minnesota Timberwolves",
    4: "Golden State Warriors"
}
druzyny = Table(
            'druzyny', meta,
            Column('id', Integer, primary_key=True),
            Column('nazwa', String),
            sqlite_autoincrement=True)
mecze = Table(
            'mecze', meta,
            Column('id', Integer, primary_key=True),
            Column('id_pierwsze', Integer, ForeignKey('druzyny.id')),
            Column('id_drugie', Integer, ForeignKey('druzyny.id')),
            Column('wynik', String),
            sqlite_autoincrement=True)
meta.create_all(engine)


class Druzyny:
    def __init__(self, name):
        self.name = name

    def dodaj_druzyne(self):
        ins = druzyny.insert().values(nazwa=self.name)
        conn = engine.connect()
        result = conn.execute(ins)

    def zmien_indeks(self, idd, nidd):
        conn = engine.connect()
        stmt1 = druzyny.update().where(druzyny.c.id == idd).values(id=nidd)
        stmt2 = mecze.update().where(mecze.c.id_pierwsze == idd).values(id_pierwsze=nidd)
        conn.execute(stmt1)
        conn.execute(stmt2)
        s1 = druzyny.select()
        s2 = druzyny.select()
        conn.execute(s1).fetchall()
        conn.execute(s2).fetchall()


class Mecze:
    def __init__(self, id_pierwsze, id_drugie, wynik):
        self.id_pierwsze = id_pierwsze
        self.id_drugie = id_drugie
        self.wynik = wynik

    def dodaj_mecz(self):
        ins = mecze.insert().values(id_pierwsze=self.id_pierwsze, id_drugie=self.id_drugie, wynik=self.wynik)
        conn = engine.connect()
        result = conn.execute(ins)

    def pokaz_wyniki(self):
        conn = engine.connect()
        s = mecze.select()
        result = conn.execute(s)
        for row in result:
            print("Mecz pomiędzy {} i {} z wynikiem {}".format(druzyny_dict[row[1]], druzyny_dict[row[2]], row[3]))

    def wyeksportuj(self):
        f = open("wyniki.txt", "a")
        conn = engine.connect()
        s = mecze.select()
        result = conn.execute(s)
        for row in result:
            z1 = row[1]
            z2 = row[2]
            f.write("Mecz pomiedzy {} i {} z wynikiem {}".format(druzyny_dict[z1], druzyny_dict[z2], row[3]))
            f.write("\n")


d1 = Druzyny("Chicago Bulls")
d2 = Druzyny("Los Angeles Lakers")
d3 = Druzyny("Minnesota Timberwolves")
d4 = Druzyny("Golden State Warriors")
"""d1.dodaj_druzyne()
d2.dodaj_druzyne()
d3.dodaj_druzyne()
d4.dodaj_druzyne()
"""
m1 = Mecze(1, 2, "120:118")
m2 = Mecze(3, 2, "110:114")
m3 = Mecze(4, 1, "108:120")
m4 = Mecze(3, 4, "124:112")
"""m1.dodaj_mecz()
m2.dodaj_mecz()
m3.dodaj_mecz()
m4.dodaj_mecz()"""
#m1.pokaz_wyniki()
m1.wyeksportuj()


