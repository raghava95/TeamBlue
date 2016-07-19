import json
import datetime
from jsonHandler import *
from events import *

class Manager(object):

    def __init__(self):
         pass

    def add(self,event):
        jsonObj = JsonHandler()
        jsonObj.add_events(event)


    def delete(self,event_id):
        jsonObj=JsonHandler()
        jsonObj.delete_event(event_id)


    def update(self,event):
        jsonObj = JsonHandler()
        jsonObj.update_event(event)

    def read(self,event_id):
        jsonObj = JsonHandler()
        return jsonObj.read_event(event_id)

    def upcoming(self):
        data = None
        filename="json_data.json"
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst = []
        for i in data:
            if data[i]['date'] > today:
                event = Event(i, data[i]['name'], data[i]['info'], data[i]['date'], data[i]['venue'], data[i]['city'])
                lst.append(event)
        return lst
    
    
    
    def completed(self):
        data = None
        filename="json_data.json"
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst = []
        for i in data:
            if data[i]['date'] < today:
                event = Event(i, data[i]['name'], data[i]['info'], data[i]['date'], data[i]['venue'], data[i]['city'])
                lst.append(event)
        return lst
    
    
    def search_city(self, city):
        data = None
        filename="json_data.json"
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        lst = []
        for i in data:
            if data[i]['city'] == city:
                event = Event(i, data[i]['name'], data[i]['info'], data[i]['date'], data[i]['venue'], data[i]['city'])
                lst.append(event)
        return lst
    
    
    def search_date(self, date):
        data = None
        filename="json_data.json"    
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        lst = []
        for i in data:
            if data[i]['date'] == date:
                event = Event(i, data[i]['name'], data[i]['info'], data[i]['date'], data[i]['venue'], data[i]['city'])
                lst.append(event)
        return lst


    def list_events(self, date1, date2):
        data = None
        filename="json_data.json"        
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        lst = []
        for i in data:
            if data[i]['date'] > date1 and data[i]['date'] < date2:
                event = Event(i, data[i]['name'], data[i]['info'], data[i]['date'], data[i]['venue'], data[i]['city'])
                lst.append(event)
        return lst

