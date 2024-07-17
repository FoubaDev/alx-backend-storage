# 0x02. Redis basic
In this project, I learned :

* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache



## Tasks :

* **0. Writing strings to Redis**
  * [exercise.py](./exercise.py): 
  Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

* **1. Reading from Redis and recovering original type**
  * [1-use_or_create_database](./1-use_or_create_database): Write a script that creates or uses the database my_db.

* **2. Insert document**
  * [2-insert](./2-insert):

Write a script that inserts a document in the collection school:

* The document must have one attribute name with value “Holberton school”
* The database name will be passed as option of mongo command


* **3. All documents**
  * [3-all](./3-all):

 Write a script that lists all documents in the collection school:

* The database name will be passed as option of mongo command

* **4. All matches**
  * [4-match](./4-match):
Write a script that lists all documents with name="Holberton school" in the collection school:

* The database name will be passed as option of mongo command


* **5. Count**
  * [5. Count](./5. Count):

Write a script that displays the number of documents in the collection school:

* The database name will be passed as option of mongo command.


* **6. Update**
  * [6-update](./6-update):
Write a script that adds a new attribute to a document in the collection school:

* The script should update only document with name="Holberton school" (all of them)
* The update should add the attribute address with the value “972 Mission street”
* The database name will be passed as option of mongo command


* **7. Delete by match**
  * [7-delete](./7-delete):

 Write a script that deletes all documents with name="Holberton school" in the collection school:

* The database name will be passed as option of mongo command


* **8. List all documents in Python**
  * [8-all.py](./8-all.py):

 Write a Python function that lists all documents in a collection:

* Prototype: def list_all(mongo_collection):
* Return an empty list if no document in the collection
* mongo_collection will be the pymongo collection object


* **9. Optimize search and score**
  * [9-insert_school.py](./9-insert_school.py):

 Write a Python function that inserts a new document in a collection based on kwargs:

* Prototype: def insert_school(mongo_collection, **kwargs):
* mongo_collection will be the pymongo collection object
* Returns the new _id


* **10. Change school topics**
  * [10-update_topics.py](./10-update_topics.py):

 Write a Python function that changes all topics of a school document based on the name:

* Prototype: def update_topics(mongo_collection, name, topics):
* mongo_collection will be the pymongo collection object
* name (string) will be the school name to update
* topics (list of strings) will be the list of topics approached in the school


* **11. Where can I learn Python?**
  * [11-schools_by_topic.py](./11-schools_by_topic.py):

 Write a Python function that returns the list of school having a specific topic:

* Prototype: def schools_by_topic(mongo_collection, topic): 
* mongo_collection will be the pymongo collection object
* topic (string) will be topic searched

* **12. Log stats**
  * [12-log_stats.py](./12-log_stats.py):

 Write a Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: logs
* Collection: nginx
* Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
