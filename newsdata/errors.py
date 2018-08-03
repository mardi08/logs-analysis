#!/usr/bin/env python
import psycopg2
import datetime

# Global variables
DBNAME = "news"
TOP_COUNT = 3

# connect to database
db = psycopg2.connect(database=DBNAME)

# open cursor to perform database operations
cur = db.cursor()

'''
Constructing sql queries
'''
# query to count rows with error status from log table
errors_query = "(" \
               + "SELECT time::date, count(time::date) as errors \
               from log where log.status != '200 OK' group by \
               time::date order by time::date desc" \
               + ")"
# query to count rows with success status from log table
success_query = "(" \
                + "SELECT time::date, count(time::date) as success \
                from log where log.status = '200 OK' group by \
                time::date order by time::date desc" \
                + ")"
# joining errors and success new tables
errors_success_query = "(" + \
                       "SELECT log_success.time::date, log_success.success,\
                       log_errors.errors from " \
                       + success_query \
                       + " as log_success join " \
                       + errors_query \
                       + " as log_errors on log_success.time::date \
                       = log_errors.time::date order by log_success.time::date desc" \
                       + ")"
# calculate the error rate in percent
calc_query = "(" \
             + "SELECT time::date, (round((100 * ((1.0 * errors) \
             / ((1.0 * success) + (1.0 * errors)) )),2))\
              as error_rates from " \
             + errors_success_query \
             + "as status_summary" \
             + ")"
# filtering out unnecessary information
final_query = "SELECT * from " \
              + calc_query \
              + " as error_table where error_table.error_rates > 1.0;"

# Getting all queries
cur.execute(final_query)
results = cur.fetchall()

# Print out the analysis result
print("")
print("days with more than 1% of error requests: ")

for rows in results:
    date_string = str(rows[0])
    datee = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    print(
        rows[0].strftime("%B") + " " + rows[0].strftime("%d")
        + ", " + rows[0].strftime("%Y") + " -- " + str(rows[1]) + "% errors."
        )

print("")

# end session
cur.close
db.close
