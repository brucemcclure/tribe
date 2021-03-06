from main import db

class Users(db.Model):
    __tablename__ = 'users'

    userid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    profile_pic = db.Column(db.String())
    account_active = db.Column(db.Boolean(), default = True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    
    
    def __repr__(self):
        return f"<User {self.username}>"    
