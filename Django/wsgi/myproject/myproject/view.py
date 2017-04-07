__author__ = 'rodrigo'
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db import connections
import datetime
from django.core import serializers
import json
import collections
from datetime import datetime
import pytz # $ pip install pytz
import requests
import urllib



def welcome(request):
    return HttpResponse("Welcome!")

#############Company########################
def GET_insertCompany(request):
    c = connections['default2'].cursor()
    result = c.execute(
        "INSERT INTO company (name, address, city, zipCode, state, country, phoneNumber, insertedData,updatedData) VALUES (\'" + str(
            request.GET.get('name')) + "\',\'" + str(request.GET.get('address')) + "\',\'" + str(
            request.GET.get('city')) + "\',\'" + str(request.GET.get('zipCode')) + "\',\'" + str(
            request.GET.get('state')) + "\',\'" + str(request.GET.get('country')) + "\',\'" + str(
            request.GET.get('phoneNumber')) + "\', (TIMESTAMP \'" + str(
            datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r

def GET_selectACompany(request):
    c = connections['default2'].cursor()
    c.execute("select * from company where id = \'" + str(request.GET.get('companyID')) + "\'")
    rows = c.fetchall()

    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['name'] = row[1];
            d['address'] = row[2];
            d['city'] = row[3];
            d['zipCode'] = row[4];
            d['state'] = row[5];
            d['country'] = row[6];
            d['phoneNumber'] = row[7];
            d['insertedData'] = str(row[8]);
            d['updatedData'] = str(row[9]);

        return HttpResponse(json.dumps(d), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r

def GET_selectAllCompany(request):
    c = connections['default2'].cursor()
    c.execute("select * from company")
    rows = c.fetchall()

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['id'] = row[0];
        d['name'] = row[1];
        d['address'] = row[2];
        d['city'] = row[3];
        d['zipCode'] = row[4];
        d['state'] = row[5];
        d['country'] = row[6];
        d['phoneNumber'] = row[7];
        d['insertedData'] = str(row[8]);
        d['updatedData'] = str(row[9]);
        objects_list.append(d)

    return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')

def GET_insertBus(request):
    c = connections['default2'].cursor()
    result = c.execute(
        "INSERT INTO bus ( route_id, company_id,  name, brand, adaptedforWheelChair, model, capacity, insertedData,updatedData ) VALUES (\'" + str(
            request.GET.get('route_id')) + "\',\'" + str(request.GET.get('company_id')) + "\',\'" + str(
            request.GET.get('name')) + "\',\'" + str(request.GET.get('brand')) + "\',\'" + str(
            request.GET.get('adaptedforWheelChair')) + "\',\'" + str(
            request.GET.get('model')) + "\',\'" + request.GET.get('capacity') + "\', (TIMESTAMP \'" + str(
            datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectAbus(request):
    c = connections['default2'].cursor()
    c.execute("select * from bus where id = \'" + str(request.GET.get('busID')) + "\'")
    rows = c.fetchall()

    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['route_id'] = row[1];
            d['company_id '] = row[2];
            d['name'] = row[3];
            d['brand'] = row[4];
            d['adaptedforWheelChair'] = row[5];
            d['model'] = row[6];
            d['capacity'] = row[7];
            d['insertedData'] = str(row[8]);
            d['updatedData'] = str(row[9]);

        return HttpResponse(json.dumps(d), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_selectbusFromCompany(request):
    c = connections['default2'].cursor()
    c.execute("select * from bus where company_id = \'" + str(request.GET.get('company_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['route_id'] = row[1];
            d['company_id '] = row[2];
            d['name'] = row[3];
            d['brand'] = row[4];
            d['adaptedforWheelChair'] = row[5];
            d['model'] = row[6];
            d['capacity'] = row[7];
            d['insertedData'] = str(row[8]);
            d['updatedData'] = str(row[9]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_selectbusFromRoute(request):
    c = connections['default2'].cursor()
    c.execute("select * from bus where route_id = \'" + str(request.GET.get('route_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['route_id'] = row[1];
            d['company_id '] = row[2];
            d['name'] = row[3];
            d['brand'] = row[4];
            d['adaptedforWheelChair'] = row[5];
            d['model'] = row[6];
            d['capacity'] = row[7];
            d['insertedData'] = str(row[8]);
            d['updatedData'] = str(row[9]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r

        #############GeoPosition########################


def GET_insertgeoPosition(request):

    #Get lat
    latitude_float = float(request.GET.get('lat'))
    latitude_hour = (int(latitude_float/100))*-1;#Getting hour
    latitude_hour = latitude_hour-((latitude_float+(latitude_hour*100))/60)#converting min to hour

    #Get lon
    longitude_float = float(request.GET.get('lon'))
    longitude_hour = (int(longitude_float/100))*-1;#Getting hour
    longitude_hour = longitude_hour-((longitude_float+(longitude_hour*100))/60)#converting min to hour



    c = connections['default2'].cursor()
    result = c.execute("INSERT INTO geoPosition (bus_id, position, altitude, ttff, satellites, speedotg, course, date, inserteddata, updateddata) VALUES  (" + str(request.GET.get('bus_id')) + ", ST_GeomFromText(\' POINT(" + str(latitude_hour) + " " + str(longitude_hour) + ")\', 26910)" +", "+ str(request.GET.get('alt')) +", "+ str(request.GET.get('TTFF')) +", "+ str(request.GET.get('sat')) +", "+ str(request.GET.get('speedOTG')) +", "+ str(request.GET.get('course')) +", (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")

    print("INSERT INTO geoPosition (bus_id, position, altitude, ttff, satellites, speedotg, course, date, inserteddata, updateddata) VALUES  (" + str(request.GET.get('bus_id')) + ", ST_GeomFromText(\' POINT(" + str(latitude_hour) + " " + str(longitude_hour) + ")\', 26910)" +", "+ str(request.GET.get('alt')) +", "+ str(request.GET.get('TTFF')) +", "+ str(request.GET.get('sat')) +", "+ str(request.GET.get('speedOTG')) +", "+ str(request.GET.get('course')) +", (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r

def GET_selectLastGeoPosition(request):
    c = connections['default2'].cursor()


    c.execute("select id,bus_id,POSITION ,altitude,ttff,satellites,speedotg,course,DATE,inserteddata,updateddata, ST_X(position),ST_Y(position)  from geoPosition where bus_id = \'" + str(
        request.GET.get('bus_id')) + "\' ORDER BY date DESC LIMIT 1 ")
    rows = c.fetchall()


    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['bus_id'] = row[1];
            d['altitude'] = row[3];
            d['ttff'] = row[4];
            d['satellites'] = row[5];
            d['speedotg'] = row[6];
            d['course'] = row[7];
            d['date'] = str(row[8]);
            d['NAME'] = 'Bus id' + str(d['bus_id']);
            d['TEL'] = '-'
            d['URL'] = '-'
            d['ADDRESS1'] = '-'
            d['ADDRES2'] = '-'
            d['CITY'] = '-'
            d['ZIP'] = '-';


            g = collections.OrderedDict()
            g['type'] = "Point"
            list = [row[11],row[12]]
            g['coordinates'] = list



            inside = {'type':'Feature','id':row[0],'properties':d,'geometry':g}
            objects_list.append(inside)

        result = {'type':'FeatureCollection', 'features': objects_list}
        return HttpResponse(json.dumps(result), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


#############Route########################
def GET_insertRoute(request):
    c = connections['default2'].cursor()
    result = c.execute("INSERT INTO route ( name, insertedData,updatedData ) VALUES (\'" + str(
        request.GET.get('name')) + "\', (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(
        datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectARoute(request):
    c = connections['default2'].cursor()
    c.execute("select * from route where id = \'" + str(request.GET.get('route_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['name'] = row[1];
            d['insertedData'] = str(row[2]);
            d['updatedData'] = str(row[3]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


#############busStop########################
def GET_insert_BusStop(request):
    c = connections['default2'].cursor()
    result = c.execute(
        "INSERT INTO busStop ( name, observation, position, insertedData, updatedData ) VALUES (\'" + str(
            request.GET.get('name')) + "\',\'" + str(
            request.GET.get('observation')) + "\',ST_GeomFromText(\' POINT(" + str(request.GET.get('lat')) + " " + str(
            request.GET.get('lon')) + ")\', 26910)" + ", (TIMESTAMP \'" + str(
            datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectABusStop(request):
    c = connections['default2'].cursor()
    c.execute("select * from busStop where id = \'" + str(request.GET.get('busStop_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['name'] = row[1];
            d['observation'] = row[2];
            d['position'] = str(row[3]);
            d['insertedData'] = str(row[4]);
            d['updatedData'] = str(row[5]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET__insert_BusStop_has_route(request):
    c = connections['default2'].cursor()
    result = c.execute(
        "INSERT INTO busStop_has_route ( busStop_id,  route_id,   insertedData, updatedData  ) VALUES (\'" + str(
            request.GET.get('busStop_id')) + "\',\'" + str(request.GET.get('route_id')) + "\', (TIMESTAMP \'" + str(
            datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectBusStop_has_route_busStop(request):
    c = connections['default2'].cursor()
    c.execute("SELECT busStop.id, busStop.name, busStop.observation, ST_X(busStop.position), ST_Y(busStop.position) FROM busStop INNER JOIN busStop_has_route ON  (busStop_has_route.busstop_id=busStop.id) WHERE busStop_has_route.route_id = \'" + str(request.GET.get('route_id')) + "\'")
    rows = c.fetchall()

    objects_list = []


    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            #d['NAME'] = str(row[1].encode('utf-8'))
            #d['TEL'] = str(row[2].encode('utf-8'))
            d['NAME'] = str(row[1])
            d['TEL'] = str(row[2])
            d['URL'] = '-'
            d['ADDRESS1'] = '-'
            d['ADDRES2'] = '-'
            d['CITY'] = '-'
            d['ZIP'] = '-';


            g = collections.OrderedDict()
            g['type'] = "Point"
            list = [row[3],row[4]]
            g['coordinates'] = list

            inside = {'type':'Feature','id':row[0],'properties':d,'geometry':g}
            objects_list.append(inside)



        result = {'type':'FeatureCollection', 'features': objects_list}
        return HttpResponse(json.dumps(result), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_selectBusStop_has_route_route_id(request):
    c = connections['default2'].cursor()
    c.execute("select * from busStop_has_route where route_id = \'" + str(request.GET.get('route_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['busStop_id'] = row[0];
            d['route_id'] = row[1];
            d['insertedData'] = str(row[2]);
            d['updatedData'] = str(row[3]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_insertWeekDay(request):
    c = connections['default2'].cursor()
    result = c.execute( "INSERT INTO weekDay (  name  ) VALUES (\'" + str(request.GET.get('name')) + "\')")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectAWeekDay(request):
    c = connections['default2'].cursor()
    c.execute("select * from weekDay where id = \'" + str(request.GET.get('weekday_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['name'] = row[1];
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r

def GET_selectAllWeekDay(request):
    c = connections['default2'].cursor()
    c.execute("select * from weekDay")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['name'] = row[1];
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r

def GET__insert_scheduleRouteatBusStop(request):
    c = connections['default2'].cursor()
    result = c.execute(
        "INSERT INTO scheduleRouteatBusStop ( weekDay_id, route_id, busStop_id, time,insertedData, updatedData) VALUES (\'" + str(request.GET.get('weekDay_id')) + "\',\'" + str(request.GET.get('route_id')) +"\',\'" + str(request.GET.get('busStop_id'))+ "\', (time \'" + str(request.GET.get('time')) + "\') , (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'), (TIMESTAMP \'" + str(datetime.now(pytz.timezone("Brazil/West"))) + "\'))")
    j = {'status': 'Ok'}
    r = HttpResponse(json.dumps(j))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r


def GET_selectAScheduleRouteatBusStop(request):
    c = connections['default2'].cursor()
    c.execute("select * from scheduleRouteatBusStop where id = \'" + str(request.GET.get('scheduleRouteatBusStop_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['weekDay_id'] = row[1];
            d['route_id'] = row[2];
            d['busStop_id'] = row[3];
            d['time'] = str(row[4]);
            d['insertedData'] = str(row[5]);
            d['updatedData'] = str(row[6]);
            objects_list.append(d)

        return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_selectscheduleRouteatBusStop_route(request):
    c = connections['default2'].cursor()
    c.execute("select * from scheduleRouteatBusStop where route_id = \'" + str(request.GET.get('route_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['weekDay_id'] = row[1];
            d['route_id'] = row[2];
            d['busStop_id'] = row[3];
            d['time'] = str(row[4]);
            d['insertedData'] = str(row[5]);
            d['updatedData'] = str(row[6]);
            objects_list.append(d)

            return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r


def GET_selectscheduleRouteatBusStop_busStop(request):
    c = connections['default2'].cursor()
    c.execute("select * from scheduleRouteatBusStop where busStop_id  = \'" + str(request.GET.get('busStop_id')) + "\'")
    rows = c.fetchall()

    objects_list = []
    if (len(rows) > 0):
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0];
            d['weekDay_id'] = row[1];
            d['route_id'] = row[2];
            d['busStop_id'] = row[3];
            d['time'] = str(row[4]);
            d['insertedData'] = str(row[5]);
            d['updatedData'] = str(row[6]);
            objects_list.append(d)

            return HttpResponse(json.dumps(objects_list), content_type='application/json;charset=utf8')
    else:
        j = {'size': '0'}
        r = HttpResponse(json.dumps(j))
        r['Access-Control-Allow-Origin'] = '*'
        r['Content-Type'] = 'application/json'
        return r



def GET_getBusTimeAtBusStop(request):


    ##Select the closest busstops
    c = connections['default2'].cursor()
    c.execute("SELECT ST_Distance(busstop.position,newgeoTable.position) AS distance, busstop.id AS busstop_id FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 1) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = "+str(request.GET.get('route_id'))+" ORDER BY distance ASC LIMIT " + str(request.GET.get('busStopLimit')))
    rows_busStopCloseToBus = c.fetchall()

    #Select the first and the last busstop
    c.execute("SELECT busstop_has_route.busstop_id AS first_busstopID, (a.last_busstopID) FROM (SELECT busstop_id AS last_busstopID FROM busstop_has_route WHERE busstop_has_route.route_id = "+str(request.GET.get('route_id'))+" ORDER BY busstop_id DESC LIMIT 1 ) a,  busstop_has_route WHERE busstop_has_route.route_id = "+str(request.GET.get('route_id'))+ " LIMIT 1")
    rows_testLastbusStop = c.fetchall()

    for row in rows_busStopCloseToBus:

        #Get the last bus stop close to the bus
        if(row[1]==rows_testLastbusStop[0][0]):#if is the last busstop register
            numTestLastBusStop  = rows_testLastbusStop[0][1]
        else:
            numTestLastBusStop = row[1] - 1

        #Get the diference between the closest busstop with the current position and the last position
        c.execute("SELECT ST_Distance(busstop.position,newgeoTable.position) AS distance FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 2) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = 1 AND busstop.id = "+str(numTestLastBusStop))
        rows_DiferenceOfDistance = c.fetchall()

        #if is correct the the current position is larger then the last
        if(rows_DiferenceOfDistance[0][0]>=rows_DiferenceOfDistance[1][0]):

            #print("Correct : " + str(row[1]))
            #select the next bus stop until desired bus stop
            if(int(request.GET.get('busStopDesired'))>=int(row[1])):
                c.execute("SELECT ST_AsText(newgeoTable.position), ST_AsText(busstop.position) FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 1) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = 1 AND busstop.id >= "+ str(row[1]) +" AND busstop.id <="+ str(request.GET.get('busStopDesired')))
            else:
                c.execute("SELECT ST_AsText(newgeoTable.position), ST_AsText(busstop.position) FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 1) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = 1 AND busstop.id >= "+ str(row[1]) +" OR  busstop.id <="+ str(request.GET.get('busStopDesired')))
            rows_geoposition = c.fetchall()


            print( str(row[1]) + " " + str(request.GET.get('busStopDesired')))
            waypoints = (str('\'')+ str(rows_geoposition[0][0])+'\'');
            for row_position in rows_geoposition:
                    waypoints = waypoints + ', \''+ str(row_position[1])+'\'';

            print (waypoints)
            c.execute("SELECT ST_Length(ST_MakeLine(ARRAY["+waypoints+"])::geography)")
            final_distance = c.fetchall()


            distance = final_distance[0][0]
            velocity= float(request.GET.get('velocity'))
            min = ((distance/1000.0)/velocity)*60.0 #metros->km/velocity*60 = minutos
            seconds = (min - int(min))*60
            d = collections.OrderedDict()
            d['duration'] = str(int(min))+ " mins : "+str(int(seconds))+" secs";

            return HttpResponse(json.dumps(d), content_type='application/json;charset=utf8')
            ##Working for google api
            # objects_list = []
            # objects_list.append(d)

            # print("Correct : " + str(row[1]))
            # if(request.GET.get('busStopDesired')>row[1]):
            #     c.execute("SELECT ST_Y(newgeoTable.position) AS currentBus_lat, ST_X(newgeoTable.position) AS currentBus_lon, ST_Y(busstop.position) AS busStopDesired_lat,ST_X(busstop.position) AS busStopDesired_lon FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 1) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = 1 AND busstop.id >="+ str(row[1]) +" AND busstop.id <="+ str(request.GET.get('busStopDesired')))
            # else:
            #     c.execute("SELECT ST_Y(newgeoTable.position) AS currentBus_lat, ST_X(newgeoTable.position) AS currentBus_lon, ST_Y(busstop.position) AS busStopDesired_lat,ST_X(busstop.position) AS busStopDesired_lon FROM (SELECT * FROM geoposition ORDER BY geoposition.id DESC LIMIT 1) AS newgeoTable, busstop INNER JOIN busstop_has_route ON  busstop.id = busstop_has_route.busstop_id WHERE busstop_has_route.route_id = 1 AND busstop.id >="+ str(row[1]) +" OR busstop.id <="+ str(request.GET.get('busStopDesired')))
            # rows_geoposition = c.fetchall()
            #
            # print(rows_geoposition)
            # waypoints = ''
            # i = 0
            # for row_position in rows_geoposition:
            #     if i <> 0:
            #         waypoints = waypoints + '|' + str(row_position[2]) +','+ str(row_position[3])
            #     i = i+1
            #
            # payload = {'origin': str(rows_geoposition[0][0])+','+str(rows_geoposition[0][1]), 'destination': str(rows_geoposition[len(rows_geoposition)-1][2])+','+str(rows_geoposition[len(rows_geoposition)-1][3]),'waypoints':waypoints,'key':'AIzaSyDWRHdV-sb-NllQn2szQvbCXJCEmsEedVc'}
            #
            # r = requests.get("https://maps.googleapis.com/maps/api/directions/json",params=urllib.unquote(urllib.urlencode(payload)));
            # data = json.loads(r.text);
            # print(r.url)
            # print(data['routes'][0]['legs'][0]['duration']['text'])
        else:
            print("Incorrect BusStop")

    d = collections.OrderedDict()
    d['duration'] = "Not find next time for next bus";
    r = HttpResponse(json.dumps(d))
    r['Access-Control-Allow-Origin'] = '*'
    r['Content-Type'] = 'application/json'
    return r