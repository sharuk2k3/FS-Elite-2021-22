/* 
Write a MongoDB Query to get all the documents from inventory collection,
where the dim_cm array contains at least one element that is both 
greater than 22 and less than 30.
.
Sample Document:
----------------
{ 
	item: "journal", 
	qty: 25, 
	tags: ["blank", "red"], 
	dim_cm: [ 14, 21 ] 
}

Note: To write the query, use printjson() method from 'mongosh' module
    e.g., To display all the douments from 'students' collection
        => printjson( db.inventory.find())
    Where,
    db => databse connection object
    inventory => collections name
    find => method to retrieve  all the docuemnts

*/

// Write the query here.

printjson(db.inventory.find({"dim_cm":{$elemMatch: {$gt: 22, $lt: 30}}}));