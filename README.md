# logs-analysis

The program runs the following analysis based on data in ```news``` database:
- ```popular_authors.py``` : Produced report of 3 most popular articles.
- ```popular_articles.py``` : Produced report of 3 most popular authors.
- ```errors.py```: Produced report of days which more than 1 % of requests lead to errors.


### How to run the program
_______
To get a report of 3 most popular articles:
```
python newsdata/popular_articles.py
```
<br>
To get a report of 3 most popular authors:
```
python newsdata/popular_authors.py
```
<br>
To get a report of days with more than 1 % requests lead to errors:
```
python newsdata/errors.py
```
