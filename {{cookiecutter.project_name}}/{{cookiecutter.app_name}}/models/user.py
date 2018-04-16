# coding: utf-8


from {{cookiecutter.app_name}}.extensions import db, bcrypt


class User(db.Model):
    """Basic user model"""
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    is_admin = db.Column(db.Boolean(), default=False)

    def __init__(self, **kwargs):
        """Create instance."""
        super(User, self).__init__(**kwargs)
        if self.password:
            self.set_password(self.password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        """Represent instance as a unique string."""
        # return "<User %s>" % self.username
        return '<User({username!r})>'.format(username=self.username)