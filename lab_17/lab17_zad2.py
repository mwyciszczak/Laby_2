from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()


class Druzyna(base):
    __tablename__ = "druzyna"

    id_druzyny = Column("id_druzyny", Integer, primary_key=True)
    nazwa_druzyny = Column("nazwa_druzyny", String)


class Mecz(base):
    __tablename__ = "mecz"

    id_meczu = Column("id_meczu", Integer, primary_key=True)
    druzyna1 = Column("druzyna1", String, ForeignKey("druzyna.id_druzyny"))
    druzyna2 = Column("druzyna2", String, ForeignKey("druzyna.id_druzyny"))
    wynik = Column("wynik", String)


engine = create_engine("sqlite:///baza.db", echo=True)
#engine.execute('pragma foreign_keys=on') ale czemu to nie działa????`
base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
session.execute('pragma foreign_keys=on')

teams_dict = {}
qdruzyny = session.execute("SELECT * FROM druzyna")
for x in qdruzyny:
    teams_dict[x[0]] = x[1]
print(teams_dict)
qmecz = session.execute("SELECT * FROM mecz")
for x in qmecz:
    print("Mecz pomiędzy {} oraz {} z wynikiem {}".format(teams_dict[int(x[1])], teams_dict[int(x[2])], x[3]))

session.commit()
session.close()
