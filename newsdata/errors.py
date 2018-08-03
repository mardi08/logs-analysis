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

final_query = """
SELECT *
FROM
  (SELECT TIME::date,
          (
              round(
                  (100 * (
                      (1.0 * errors)/((1.0 * success) + (1.0 * errors)))),2
                    )
            )
          AS error_rates
   FROM
     (SELECT log_success.time::date,
             log_success.success,
             log_errors.errors
      FROM
        (SELECT TIME::date,
                count(TIME::date) AS success
         FROM log
         WHERE log.status = '200 OK'
         GROUP BY TIME::date
         ORDER BY TIME::date DESC) AS log_success
      JOIN
        (SELECT TIME::date,
                count(TIME::date) AS errors
         FROM log
         WHERE log.status != '200 OK'
         GROUP BY TIME::date
         ORDER BY TIME::date DESC)
         AS log_errors ON log_success.time::date = log_errors.time::date
      ORDER BY log_success.time::date DESC) AS status_summary) AS error_table
WHERE error_table.error_rates > 1.0;
"""

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
