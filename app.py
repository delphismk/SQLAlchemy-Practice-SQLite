# ✅ 問題2：SQLAlchemyとNeo4jによる関係性の可視化
#
# 🔹目的：
# ORM（SQLAlchemy）によるオブジェクトDB操作と、グラフDB（Neo4j）による関係性のモデリングを一気に体得する問題
# 🔸要件：
# あなたは社内の社員管理システムのDB設計・実装担当です。以下のような仕様でSQLAlchemyとNeo4jを使って両方の操作系に習熟してください。
#
# ✅ A. SQLAlchemyを使って以下のような操作を行え：
import sqlalchemy
import sqlalchemy.orm

engine = sqlalchemy.create_engine(
    'sqlite:///:memory:',
    # echo=True
)

Base = sqlalchemy.orm.declarative_base()

# 	1.	Employeeクラス（ORM）を作成し、(id, name)を持つテーブルを作る
class Employee(Base):
    __tablename__ = 'employee'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(
        sqlalchemy.String(14))
    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}')"

#Baseにengineを渡し、EmployeeTABLEをactivate
Base.metadata.create_all(engine)

#Read, Writeのためのセッション用意
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# 	2.	“Mike”, “Nancy”, “Kaito”を登録する
p1 = Employee(name = 'Mike')
session.add(p1)
p2 = Employee(name = 'Nancy')
session.add(p2)
p3 = Employee(name = 'Kaito')
session.add(p3)
session.commit()

# 	3.	“Mike”の名前を”Michel”に変更
p4 = session.query(Employee).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# 	4.	残っている全員を表示（session.query().all()）
result = session.query(Employee).all()
print(result)


