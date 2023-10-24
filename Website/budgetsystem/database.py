import os
from sqlalchemy import create_engine, text

connString = "mysql+pymysql://czvuqeftlb8rqjlu3quy:pscale_pw_WCwUaYbgDQYt0YDTEdfKleAP6As0TrV7KjGvdi15OGA@aws.connect.psdb.cloud/reddcareers?charset=utf8mb4"

engine = create_engine(connString,connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

