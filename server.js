// import express JS module into app 
// and creates its variable. 
var express = require('express'); 
var app = express(); 
  
// Creates a server which runs on port 3000 and  
// can be accessed through localhost:3000 
app.listen(3000, "192.168.4.2") 
  
// Function callName() is executed whenever  
// url is of the form localhost:3000/stop 
app.get('/stop', Stop); 
app.get('/slow', Slow);
  
function Stop(req, res) { 
    
    console.log("Stop")
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python',["./motor_test.py", "Stop"]); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
 
    } )

}

function Slow(req, res) {
    console.log("Stop")
    // Use child_process.spawn method from
    // child_process module and assign it
    // to variable spawn
    var spawn = require("child_process").spawn;

    // Parameters passed in spawn -
    // 1. type_of_script
    // 2. list containing Path of the script
    //    and arguments for the script

    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will
    // so, first name = Mike and last name = Will
    var process = spawn('python',["./motor_test.py", "Slow"]);

    // Takes stdout data from script which executed
    // with arguments and send this data to res object
    process.stdout.on('data', function(data) {
        res.send(data.toString());

    } )

}