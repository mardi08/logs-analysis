import psycopg2

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
# Getting the slug from the path
path_substring = "reverse(split_part(reverse(path), '/', 1))"
# query to get all informations from log table
log_query = "(SELECT count(*) as num, " \
    + path_substring \
    + " as log_slug from log group by " \
    + path_substring \
    + " order by num desc)"
# joining articles table with log table, only take matching slugs
articles_log_query = "(articles join" \
    + log_query \
    + " as log_query on articles.slug = log_query.log_slug)"
# joining authors table with log_articles table
final_query = "SELECT name, sum(num) as views from authors join "\
    + articles_log_query\
    + " as log_articles on authors.id = log_articles.author group by authors.id;"

# Getting all queries
cur.execute(final_query)
results = cur.fetchall()

'''
popular authors
'''
# print out header information - popular articles
print("")
print("The most popular " + str(TOP_COUNT) + " authors of all time are:")

# print out top viewed articles
count = 0
for row in results:
    if count == TOP_COUNT:
        break
    print(row[0] + " -- " + str(row[1]) + " views.")
    count += 1
print("")

# end session
cur.close
db.close
