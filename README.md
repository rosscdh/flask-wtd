flask-wtd
=========

What the Diff version running in flask with honcho


Install
-------

```
pip install -r requirements.txt
```


Running
-------

```
honcho start
```

New terminal or you could run this using Postman (https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en) or similar

```
http -f POST http://localhost:5000/wtd a=test2003 b=testing2020
```

Responds with

```
HTTP/1.0 200 OK
Content-Length: 337
Content-Type: text/html; charset=utf-8
Date: Sat, 15 Feb 2014 09:42:52 GMT
Server: Werkzeug/0.9.4 Python/2.7.2

<style type="text/css"><!--

.insert { background-color: #aaffaa }
.delete { background-color: #ff8888; text-decoration: line-through }
.tagInsert { background-color: #007700; color: #ffffff }
.tagDelete { background-color: #770000; color: #ffffff }

--></style><span class="delete">test2003</span><span class="insert">testing2020</span>
```