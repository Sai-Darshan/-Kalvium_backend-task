
Build a server server that responds to mathematical operations sent via URL. it also maintains a history of the last 20 operations performed on the server.

Let’s assume your server is at: localhost:3000. Here’s some sample requests:



GET request
Response
Endpoint
/
HTML
Lists all the get endpoint samples you can demo (like below)


/history
HTML
Lists the last 20 operations performed on the server, and the answers.

Eg 1
/5/plus/3
JSON
{question:”5+3”,answer: 8}

Eg 2
/3/minus/5
JSON
{question:”3-5”, answer: -2}

Eg 3
/3/minus/5/plus/8
JSON
{question:”3-5+8”, answer: 6}


Eg 4
/3/into/5/plus/8/into/6
JSON
{question:”3*5+8*6”, answer: 63}
.. so on






Above shows 3 operators. Implement as many as you can. As you can see the URL can be composed as large as possible.

The task will be scored on: 
 a) How well the code is composed and written
 b) the amount of functionality added, and
 c) history of submissions (as viewed on github).
 d) The /history URL works even after a server restart
