from unittest import TestCase
from app import db, create_app
from app.models import Category, Book

class TestModel(TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    
    def testCategoryCreation(self):
        category_1 = Category(name='One')
        self.assertIsNone(category_1.id)
        db.session.add(category_1)
        db.session.commit()
        self.assertIsNotNone(category_1.id)
        self.assertEqual(str(category_1), "<Category u'One'>")
    
    def testSearchCategoryByName(self):
        category_one = Category(name='One')
        category_two = Category(name='Two')
        db.session.add_all([category_one,category_two])
        db.session.commit()
        book_one = Book(name='New World Order', category_id=category_one.id)
        book_two = Book(name='Things Fall Apart', category_id=category_two.id)
        book_three = Book(name='Pinkberry', category_id=category_two.id)
        book_four = Book(name='New Scopes', category_id=category_two.id)
        db.session.add_all([book_one,book_two, book_three, book_four])
        db.session.commit()
        
        self.assertEqual(len(category_one.books.all()), 1)
        self.assertEqual(len(category_two.books.all()), 3)
        self.assertEqual(len(Book.findByCategoryName(category_two.name)), 3)
        self.assertIsNone(Book.findByCategoryName('New Category'))
    
    def testBookCreation(self):
        book_one = Book(name='Play')
        self.assertIsNone(book_one.id)
        db.session.add(book_one)
        db.session.commit()
        self.assertIsNotNone(book_one.id)
        self.assertEqual(str(book_one), "<Book u'Play'>")
        
    def testSearchBookByName(self):
        book_one = Book(name='New World Order')
        book_two = Book(name='Things Fall Apart')
        book_three = Book(name='Pinkberry')
        book_four = Book(name='New Scopes')
        db.session.add_all([book_one,book_two, book_three, book_four])
        db.session.commit()
        
        self.assertEqual(len(Book.findByName('New World')), 1)
        self.assertEqual(len(Book.findByName('N')), 2)
