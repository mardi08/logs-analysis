import psycopg2

DBNAME = "news"

# connect to database
db = psycopg2.connect(database=DBNAME)

# open cursor to perform database operations
cur = db.cursor()

# execute command
path_substring = "reverse(split_part(reverse(path), '/', 1))" # Getting the slug from the path
cur.execute("SELECT count(*) as num, " + path_substring + " from log group by " + path_substring + " order by num desc;")

results = cur.fetchall()

print("results: ")
print results
cur.close
db.close
