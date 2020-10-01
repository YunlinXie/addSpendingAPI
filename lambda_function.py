import json
import sys
import logging
import pymysql
#rds settings
rds_host  = "spendingtracker.c81xwphxtime.us-west-2.rds.amazonaws.com"
name = 'admin'
password = 'spendless2020'
db_name = 'spendingtracker'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    # TODO implement
    """
    This function fetches content from MySQL RDS instance
    """
    
    print("!!!!!event", event)
    event_body = json.loads(event['body'])
    # item_count = 0
    query = ('INSERT INTO spending(DATE, AMOUNT) VALUES '
             '("{0}", {1});').format(event_body["date"], event_body["amount"])

    print(query)


    with conn.cursor() as cur:
        cur.execute(query)

    conn.commit()
    
    return {
        'statusCode': 200,
        'body': json.dumps("OK")
    }

