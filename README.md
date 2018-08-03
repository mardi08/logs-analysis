# logs-analysis

The program runs the following analysis based on data in ```news``` database:
- ```popular_authors.py``` : Produced report of 3 most popular articles.
- ```popular_articles.py``` : Produced report of 3 most popular authors.
- ```errors.py```: Produced report of days which more than 1 % of requests lead to errors.

### Dependencies
___
You will need the following dependencies installed on your system to run the programs:
- Python 2.7
- PostgresSQL


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