CREATE TABLE company (
  id SERIAL  NOT NULL ,
  name VARCHAR(30)   NOT NULL ,
  address VARCHAR(100)    ,
  city VARCHAR(30)    ,
  zipCode VARCHAR(9)    ,
  state VARCHAR(30)    ,
  country VARCHAR(30)    ,
  phoneNumber VARCHAR(12)    ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id));




CREATE TABLE weekDay (
  id SERIAL  NOT NULL ,
  name VARCHAR(10)   NOT NULL   ,
PRIMARY KEY(id));




CREATE TABLE busStop (
  id SERIAL  NOT NULL ,
  name VARCHAR(255)   NOT NULL ,
  observation VARCHAR(255)    ,
  position VARCHAR(60)    ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id));




CREATE TABLE route (
  id SERIAL  NOT NULL ,
  company_id INTEGER   NOT NULL ,
  name VARCHAR(30)   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(company_id)
    REFERENCES company(id));


CREATE INDEX route_FKIndex1 ON route (company_id);


CREATE INDEX IFK_companyRoute ON route (company_id);


CREATE TABLE bus (
  id SERIAL  NOT NULL ,
  company_id INTEGER   NOT NULL ,
  name VARCHAR(30)   NOT NULL ,
  brand VARCHAR(30)    ,
  adaptedforWheelChair BOOL    ,
  model VARCHAR(30)    ,
  capacity INTEGER   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(company_id)
    REFERENCES company(id));


CREATE INDEX bus_FKIndex1 ON bus (company_id);


CREATE INDEX IFK_companyBus ON bus (company_id);


CREATE TABLE geoPosition (
  id SERIAL  NOT NULL ,
  bus_id INTEGER   NOT NULL ,
  position VARCHAR(60)   NOT NULL ,
  date DATETIME   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(bus_id)
    REFERENCES bus(id));


CREATE INDEX geoPosition_FKIndex1 ON geoPosition (bus_id);


CREATE INDEX IFK_busPosition ON geoPosition (bus_id);


CREATE TABLE busStop_has_route (
  busStop_id INTEGER   NOT NULL ,
  route_id INTEGER   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(busStop_id, route_id)    ,
  FOREIGN KEY(busStop_id)
    REFERENCES busStop(id),
  FOREIGN KEY(route_id)
    REFERENCES route(id));


CREATE INDEX busStop_has_route_FKIndex1 ON busStop_has_route (busStop_id);
CREATE INDEX busStop_has_route_FKIndex2 ON busStop_has_route (route_id);


CREATE INDEX IFK_busStopRoute ON busStop_has_route (busStop_id);
CREATE INDEX IFK_routeBusStop ON busStop_has_route (route_id);


CREATE TABLE scheduleRouteatBusStop (
  id SERIAL  NOT NULL ,
  weekDay_id INTEGER   NOT NULL ,
  route_id INTEGER   NOT NULL ,
  busStop_id INTEGER   NOT NULL ,
  time TIME   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(id)    ,
  FOREIGN KEY(busStop_id, route_id)
    REFERENCES busStop_has_route(busStop_id, route_id),
  FOREIGN KEY(weekDay_id)
    REFERENCES weekDay(id));


CREATE INDEX scheduleRouteatBusStop_FKIndex1 ON scheduleRouteatBusStop (busStop_id, route_id);
CREATE INDEX scheduleRouteatBusStop_FKIndex2 ON scheduleRouteatBusStop (weekDay_id);


CREATE INDEX IFK_busStop_has_routeScheduleR ON scheduleRouteatBusStop (busStop_id, route_id);
CREATE INDEX IFK_weekDayScheduleRouteBusSto ON scheduleRouteatBusStop (weekDay_id);


CREATE TABLE bus_has_route (
  bus_id INTEGER   NOT NULL ,
  route_id INTEGER   NOT NULL ,
  insertedData DATETIME    ,
  updatedData DATETIME      ,
PRIMARY KEY(bus_id, route_id)    ,
  FOREIGN KEY(bus_id)
    REFERENCES bus(id),
  FOREIGN KEY(route_id)
    REFERENCES route(id));


CREATE INDEX bus_has_route_FKIndex1 ON bus_has_route (bus_id);
CREATE INDEX bus_has_route_FKIndex2 ON bus_has_route (route_id);


CREATE INDEX IFK_busRoute ON bus_has_route (bus_id);
CREATE INDEX IFK_routeBus ON bus_has_route (route_id);



