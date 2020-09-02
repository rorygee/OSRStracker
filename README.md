# OSRS Tracker
Rewrite of a previously failed project, this currently consists of an database interface and a pretty looking graphical view for recorded experience data from a given Old School Runescape account.

A live version will exist as soon as I can wrangle with pythonanywhere and implement rate limiting on the server side.

A few other features are being worked on, including a comparison view, alternate graph types and (hopefully) a live graph for viewing experience gains over a single session, but this will be limited by the frequency at which Jagex updates experience records.


## Prerequisites
If you are looking at deploying this on your own web server, the following libraries are needed:</p>
* Flask
* WTForms
* Mysql connector
* Requests

## Screenshots
![Screencap 1](https://i.ibb.co/CPcFsqp/2020-09-02-19-20-52-127-0-0-1-85a9c48461bc.png)

![Screencap 2](https://i.ibb.co/CWHg7Yb/2020-09-02-19-21-09-127-0-0-1-6ac09519ee93.png)