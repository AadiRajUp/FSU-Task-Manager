from extensions import db

class UID(db.Model):
    __tablename__ = 'UID_TABLE'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<UID {self.username}>"
