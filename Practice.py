import sys
import json
import requests
import random
from influxdb import InfluxDBClient as IC
from datetime import datetime
from datetime import time
from datetime import date

def main():
    client=IC(host="localhost", port=8086)
    client.create_database("prac")
    client.switch_database("prac")

    mass=[0,0,0,0,0,0,0,0,0,0]
    count=0
    json_body=[]
    for i in [j for j in range(10)]:
        mass[i]=random.randrange(1, 100)
        table={
                "measurement": "sec_table",
                "tags": {
                        "param": i,
                        "count" : count
                },
                "fields": {
                    "value": mass[i]

                }
            }
        json_body.append(table)
    count=1
    while count<11:
        izm=random.randrange(-1, 2)
        if izm== 0:
            while izm==0:
                izm=random.randrange(-1, 2)
        for y in [h for h in range(10)]:
            #izm=random.randrange(-1, 2)
            mass[y]=mass[y]+izm
            table={
                "measurement": "sec_table",
                "tags": {
                        "param": y,
                        "count" : count
                    },
                "fields": {
                    "value": mass[y]
                    }
            }
            json_body.append(table)
        #json_body.append(table)
        count=count+1




    client.write_points(json_body)
    results = client.query('select * from sec_table')
    points=results.get_points(tags={'param':'0'})
   # for i in points:
   #     print(i)
   # for i in mass:
   #     print(i)   

if __name__ == "__main__":
    main()