from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, distinct, desc, select

#create engine to connect to database
engine = create_engine("sqlite:///_HI.sqlite")
connection = engine.connect()

#declare a base
Base = automap_base()

Base.prepare(engine, reflect=True)

measurements = Base.classes.measurements
stations = Base.classes.stations

#create a session
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Welcome to my Weather App!</h1>'



@app.route('/api/v.1.0/precipitation')
def precipitation():
    """Query for the dates and temperature observations from the last year"""
    # precipitation values list
    prcp_list = session.query(measurements.prcp).\
    group_by(measurements.date).\
    order_by(desc(measurements.date)).limit(365).all()

    # Precipitation Date List
    prcp_date_list = session.query(measurements.date).\
    group_by(measurements.date).\
    order_by(desc(measurements.date)).limit(365).all()

    for result in results:
         [(prcp_list), (prcp_date_list)]

    return jsonify(results)


@app.route('/api/v.1.0/stations')
def stations():
    """List of Stations with their Number of Observations"""
    return'active = session.query(measurements.station,
    func.count(measurements.station).label('qty')
    ).group_by(measurements.station
    ).order_by(desc('qty')).all()
active'

@app.route('/api/v.1.0/tobs')
def tobs():
    return'temp_list = session.query(measurements.tobs).\
filter_by(station='USC00519281').\
group_by(measurements.date).\
order_by(desc(measurements.date)).limit(365).all()

temp_date_list = session.query(measurements.date).\
group_by(measurements.date).\
order_by(desc(measurements.date)).limit(365).all()

initial_tobs_df = pd.DataFrame(temp_date_list).join(pd.DataFrame(temp_list))
temp_df = initial_tobs_df.set_index('date')
temp_df.head()'

@app.route('/api/v.1.0/start')
def start():
    return'<h1> You are on the start page!</h1>'

@app.route('/api/v.1.0/end')
def startend():
    return'<h1> You are on the start/end page!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
