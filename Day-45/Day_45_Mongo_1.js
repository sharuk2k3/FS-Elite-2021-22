/* 
Write a MongoDB query to Count the number of orders in the collection "orders"
with the field 'date' greater than "15-03-2021".
.
Sample Document:
----------------
{
	"_id": 0,
	"name": "Pepperoni",
	"size": "small",
	"price": 19,
	"quantity": 10,
	"date": "2021-03-13T08:14:30Z"
}

Note: To write the query, use printjson() method from 'mongosh' module
    e.g., To display all the douments from 'students' collection
        => printjson( db.orders.find())
    Where,
    db => databse connection object
    orders => collections name
    find => method to retrieve  all the docuemnts

*/

// Write the query here.
printjson(db.orders.countDocuments({
    "date":{$gt: new Date("2021-03-15")}
}));