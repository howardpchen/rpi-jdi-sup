#!/usr/bin/python
import os
import paho.mqtt.client as mqtt
import sqlite3
import datetime, time
from sqlite3 import Error

# Author: Po-Hao Chen MD MBA, Nathan M. Cross MD MS
# Copyright (c) 2017 Po-Hao Chen, Nathan M. Cross
#
# The code will subscribe to all messages coming from a specific location and
# then write it to a database.
# This is server-side code so can run on any machine that supports Python
# and you wish to use as a server.
#
# The example code uses public iot server run by Eclipse.
# The server serves to route messages not to store or process them.
#
# Your listener device/computer will subscribe to the relevant "topic"
# which will allow the relevant messages to be delivered as a stream to it
# for processing.

# For testing, the script will run and listen for 30 seconds and then quit

listener_id = "RadIoT_database"
location = 'testLocation'
sqlite3_file = "RadIOT.sqlite3"
sql_create_table = """
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `phonelog` (
    `location`  TEXT,
    `device`    TEXT,
    `message`   TEXT,
    `timestamp` INTEGER
);
COMMIT;
                """

def create_table(conn, create_table_sql):
    try: 
        c = conn.cursor()
        c.executescript(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    try: 
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None
        
if not os.path.exists('file'):
    conn = create_connection(sqlite3_file)
    if conn is not None:
        create_table(conn, sql_create_table)
    else:
        print("Error: cannot create database connection.")

client=mqtt.Client(listener_id)
client.connect("iot.eclipse.org")
client.subscribe("/".join([location, "+"]))

def process_msg(client, userdata, message, screen_log=True):
    global sqlite3_file
    received = str(message.payload.decode("utf-8"))
    # Process the data into message and timestamp.
    # The message format is "Message@timestamp"
    try:
        m = received.split('@')[0]
        timestamp = float(received.split('@')[1])
    except:
        print ("Error processing input")
        return

    if (screen_log):
        print("received: ", received)
        print("topic=",message.topic)
        print("message=", m)
        print("timestamp=", datetime.datetime.fromtimestamp(timestamp))

    topics = message.topic.split('/')
    
    # An example of our topic is "testLocation/RadIOT_phone1"
    location = topics[0]
    device = topics[1]

    # Data processing finished. Now place data into permenant storage.

    db = sqlite3.connect(sqlite3_file)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO phonelog(location, device, message, timestamp)
                  VALUES(?,?,?,?)''', (location, device, m, timestamp))
    db.commit()
    print("wrote to database message", m, "by device", device, "at", location,
          "on timestamp", datetime.datetime.fromtimestamp(timestamp))
    db.close()

client.on_message = process_msg

print("Start listening to phone events for 30sec, then exit.")
client.loop_start()
time.sleep(30) # Listen for messages for 30 seconds, then quit.
client.loop_stop()
