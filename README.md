# OSRS Tracker
Rewrite of a previously failed project, this currently consists of an database interface and a pretty looking graphical view for recorded experience data from a given Old School Runescape account.

A few other features are being worked on, including a comparison view, alternate graph types and (hopefully) a live graph for viewing experience gains over a single session, but this will be limited by the frequency at which Jagex updates experience records.

Database currently depends on Mysql Connector but will likely change to something like sqlalchemy for flexibility and security.

## Prerequisites
If you are looking at deploying this on your own web server, the following libraries are needed:</p>
* Flask
* WTForms
* Mysql connector
* Requests

## Screenshots
![Screencap 1](https://i.ibb.co/CPcFsqp/2020-09-02-19-20-52-127-0-0-1-85a9c48461bc.png)

![Screencap 2](https://i.ibb.co/CWHg7Yb/2020-09-02-19-21-09-127-0-0-1-6ac09519ee93.png)

## Live Version
Soon™