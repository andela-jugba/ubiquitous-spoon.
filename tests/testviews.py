from unittest import TestCase
from app import create_app, db
from flask import url_for
from app.models import Book, Category

class TestViews(TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def testIndexView(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Brand' in response.get_data(as_text=True))
        
    def testSecondView(self):
        response = self.client.get(url_for('main.second'))
        self.assertTrue('Brand' in response.get_data(as_text=True))
        
    def testSearchBookByName(self):
        response = self.client.post(url_for('main.index'), data={'name': 't'})
        self.assertTrue(response.status_code==302)
        
        response = self.client.post(url_for('main.index'), data={'name': 't'}, follow_redirects=True)
        self.assertTrue(response.status_code==200)
        self.assertTrue('No records found' in response.get_data(as_text=True))
        
        
        category_one = Category(name='One')
        category_two = Category(name='Two')
        db.session.add_all([category_one,category_two])
        db.session.commit()
        book_one = Book(name='New World Order', category=category_one)
        book_two = Book(name='Things Fall Apart', category=category_two)
        book_three = Book(name='Pinkberry', category=category_two)
        book_four = Book(name='New Scopes', category=category_two)
        db.session.add_all([book_one,book_two, book_three, book_four])
        db.session.commit()
        
        response = self.client.post(url_for('main.index'), data={'name': 't'}, follow_redirects=True)
        self.assertTrue(response.status_code==200)
        self.assertTrue('Things Fall Apart' in response.get_data(as_text=True))



        
