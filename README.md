# logs-analysis

The program runs the following analysis based on data in ```news``` database:
- ```popular_authors.py``` : Produced report of 3 most popular articles.
- ```popular_articles.py``` : Produced report of 3 most popular authors.
- ```errors.py```: Produced report of days which more than 1 % of requests lead to errors.

## Code Design

**popular_articles**

The program takes necessary information from the ```log``` table which then is joined with ```articles``` table. The joining process involved matching the slugs from each table as its primary key. The process is coded within a single query and python script is written to present output information in organized way

**popular_authors**

Sql script is also done in a single query. The *popular_articles.py* query is used with a condition of matching authors id from log table and popular articles table. Again, python script is written to present output information in organized way.

Both ```popular_articles.py``` and ```popular_authors.py``` are set to show the top 3. However, adjustmenst can be made by changing the global variable ```TOP_COUNT``` that exists in both executable python files.

**errors**

sql script is done in a single query. The query is structured by extracting new tables individually and group by dates. One table takes rows based on success responses (with status:```200 OK```) and the other takes rows based on failed responses. After joining both tables, the query does the calculation and filter out any error rates below 1%.


### Requirements
___
You will need the following dependencies installed on your system to run the programs:
- Python 2.7
- PostgreSQL
- psycopg2


### How to run the program
_______
To get a report of 3 most popular articles:
```
./newsdata/popular_articles.py
```

To get a report of 3 most popular authors:
```
./newsdata/popular_authors.py
```

To get a report of days with more than 1 % requests lead to errors:
```
./newsdata/errors.py
```
### Potential Problems
___
the following errors may occur:
```
/usr/bin/env: ‘python\r’: No such file or directory
```
if you received the error above while trying to run the programs, do the following step:

1. open the python file that you are trying to run using vim or vi
2. Administer the following command
```
:set ff=unix
```
3. exit the vim or vi editor
```
:wq
```
> you need to go through the steps above for every python file that you will execute
