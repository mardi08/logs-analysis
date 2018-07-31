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
errors_query =  "(" \
                + "SELECT time::date, count(time::date) as errors \
                from log where log.status != '200 OK' group by \
                time::date order by time::date desc" \
                + ")"
success_query = "(" \
                + "SELECT time::date, count(time::date) as success \
                from log where log.status = '200 OK' group by \
                time::date order by time::date desc" \
                + ")"
errors_success_query =  "(" + "SELECT log_success.time::date, log_success.success,\
                        log_errors.errors from " \
                        + success_query \
                        + " as log_success join " \
                        + errors_query \
                        + " as log_errors on log_success.time::date \
                        = log_errors.time::date order by log_success.time::date desc" \
                        + ")"

calc_query = "(" \
             + "SELECT time::date, (round((100 * ((1.0 * errors) / (1.0 * success))),2)) as error_rates from " \
             + errors_success_query \
             + "as status_summary" \
             + ")"
final_query = "SELECT * from " \
              + calc_query \
              + " as error_table where error_table.error_rates > 1.0;"

# Getting all queries
cur.execute(final_query)
results = cur.fetchall()

print("")
print("days with more than 1% of error requests: ")

for rows in results:
    date_string = str(rows[0])
    datee = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    print(rows[0].strftime("%B")+ " " + rows[0].strftime("%d") + ", " + rows[0].strftime("%Y") + " -- " + str(rows[1]) + "% errors.")

print("")

# end session
cur.close
db.close
