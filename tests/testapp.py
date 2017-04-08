from unittest import TestCase
from app import create_app
from flask import current_app

class TestApp(TestCase):
  def setUp(self):
    self.app = create_app('test')
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    self.app_context.pop()

  def testThatAppExist(self):
    self.assertTrue(current_app is not None)

  def testAppConfig(self):
    self.assertTrue(self.app.config['TESTING'])


