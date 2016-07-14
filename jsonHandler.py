import json
import datetime
from events import *

class JsonHandler(object):

    def __init__(self):
        self._filename = "json_data.json"


    def add_events(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        d={event.get_event_id:{"name":event.get_name,"info":event.get_info,"date":event.get_date,"venue":event.get_venue,"city":event.get_city}}
        data.update(d)
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def delete_event(self,event_id):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        del data[event_id]
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def update_event(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        id=event.get_event_id()
        data[id]['name']=event.get_name()
        data[id]['info']=event.get_info()
        data[id]['data']=event.get_date()
        data[id]['venue']=event.get_venue()
        data[id]['city']=event.get_city()
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def read_event(self,event_id):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        event=Events()
        event.set_event_id(event_id)
        event.set_name(data[event_id]['name'])
        event.set_info(data[event_id]['info'])
        event.set_date(data[event_id]['date'])
        event.set_venue(data[event_id]['venue'])
        event.set_city(data[event_id]['city'])
        return event



    def upcoming_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst=[]
        for i in data:
            if data[i]['date'] > today:
                event=Events()
                event.set_event_id(i)
                event.set_name(data[i]['name'])
                event.set_info(data[i]['info'])
                event.set_date(data[i]['date'])
                event.set_venue(data[i]['venue'])
                event.set_city(data[i]['city'])
                lst.append(event)
        return lst


    def completed_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst=[]
        for i in data:
            if data[i]['date'] < today:
                event = Events()
                event.set_event_id(i)
                event.set_name(data[i]['name'])
                event.set_info(data[i]['info'])
                event.set_date(data[i]['date'])
                event.set_venue(data[i]['venue'])
                event.set_city(data[i]['city'])
                lst.append(event)
        return lst

    def search_events_city(self,city):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['city']==city:
                event = Events()
                event.set_event_id(i)
                event.set_name(data[i]['name'])
                event.set_info(data[i]['info'])
                event.set_date(data[i]['date'])
                event.set_venue(data[i]['venue'])
                event.set_city(data[i]['city'])
                lst.append(event)
        return lst


    def search_events_date(self,date):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['date'] == date:
                event = Events()
                event.set_event_id(i)
                event.set_name(data[i]['name'])
                event.set_info(data[i]['info'])
                event.set_date(data[i]['date'])
                event.set_venue(data[i]['venue'])
                event.set_city(data[i]['city'])
                lst.append(event)
        return lst



    def list_events(self,date1,date2):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['date'] > date1 and data[i]['date'] < date2:
                event = Events()
                event.set_event_id(i)
                event.set_name(data[i]['name'])
                event.set_info(data[i]['info'])
                event.set_date(data[i]['date'])
                event.set_venue(data[i]['venue'])
                event.set_city(data[i]['city'])
                lst.append(event)
        return lst
