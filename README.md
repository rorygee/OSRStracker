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
![Screencap 1](https://i.ibb.co/pjLMynm/2020-09-07-23-36-06-127-0-0-1-23bce2823613.png)

![Screencap 2](https://i.ibb.co/zJL41rN/2020-09-07-23-38-35-127-0-0-1-04eec7a7def6.png)

![Screencap 3](https://i.ibb.co/s3DPzZY/2020-09-07-16-44-55-127-0-0-1-6e5f5527a867.png)

## Live Version
Soon™