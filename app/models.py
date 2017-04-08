from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    isbn = db.Column(db.Integer, unique=True, index=True)
    name = db.Column(db.String(120), index=True)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
    
    @staticmethod
    def findByName(name):
        return Book.query.filter(Book.name.like(name+'%')).all()
    
    @staticmethod
    def findByCategoryName(name):
        categories = Category.query.filter(Category.name.like(name+'%')).all()
        if categories:
            books = []
            for category in categories:
                 books += category.books.all()
            return books
        else:
            return None
    def __repr__(self):
        return '<Book %r>' % self.name
        

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(64), index=True)
    books = db.relationship('Book', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return '<Category %r>' % self.name
