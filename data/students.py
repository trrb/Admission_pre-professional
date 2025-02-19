import sqlalchemy


from .db_session import SqlAlchemyBase


class Students(SqlAlchemyBase):
    __tablename__ = 'students'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    number = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    parent1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    parent2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    subj1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj4 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj5 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj6 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj7 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj8 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj9 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj10 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj11 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj12 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    subj13 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

