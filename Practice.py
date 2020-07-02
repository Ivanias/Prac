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

    count=0
    json_body=[]
    while count<=10:
        for i in [j for j in range(11)]:
            table={
                    "measurement": "sec_table",
                    "tags": {
                            "param": i,
                    },
                    "fields": {
                        "value": random.randrange(1, 100)
                    }
                }
            json_body.append(table)
        count=count+1
    client.write_points(json_body)
    results = client.query('select * from sec_table')
    points=results.get_points(tags={'param':'0'})
    for i in points:
        print(i)

if __name__ == "__main__":
    main()