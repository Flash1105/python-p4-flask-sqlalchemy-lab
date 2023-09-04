from os import environ
import re

from server.app import app, db
from server.models import Animal, Enclosure, Zookeeper

class TestApp:
    '''Flask application in app.py'''

  

    def test_animal_route(self):
        '''has a resource available at "/animal/<id>".'''
       
    def test_animal_route_has_attrs(self):
        '''displays attributes in animal route in <ul> tags called Name, Species.'''
       
        
    def test_animal_route_has_many_to_one_attrs(self):
        '''displays attributes in animal route in <ul> tags called Zookeeper, Enclosure.'''
      
    def test_zookeeper_route(self):
        '''has a resource available at "/zookeeper/<id>".'''
       

    def test_zookeeper_route_has_attrs(self):
        '''displays attributes in zookeeper route in <ul> tags called Name, Birthday.'''
      
    def test_zookeeper_route_has_one_to_many_attr(self):
        '''displays attributes in zookeeper route in <ul> tags called Animal.'''
        
    def test_enclosure_route(self):
        '''has a resource available at "/enclosure/<id>".'''
       

    def test_enclosure_route_has_attrs(self):
        '''displays attributes in enclosure route in <ul> tags called Environment, Open to Visitors.'''
        
    def test_enclosure_route_has_one_to_many_attr(self):
        '''displays attributes in enclosure route in <ul> tags called Animal.'''
        