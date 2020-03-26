# Backend

This is the server side of the application, where all the magic happens.  
The architecture follows an API/SERVICE/MODEL structure.  
The _app.py_ file is the entry point for requests, and interacts with the _services_,where business logic is implemented.  
In _model_, objects relevant to the structure are declared.

A next step would be a _repository_ layer, where persistence could be implemented.

# Algorithm

The algorithm for path detection implements simple operations in a matrix recursively.  
All possible moves a knight can make are tested and, if they are inside the board, stored.  
Once the desired amount of turns has been taken, the stored positions are the desired result.
