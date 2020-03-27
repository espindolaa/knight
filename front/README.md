# Frontend

This is the client, written in Angular using TypeScript.  
It follows a very common architecture for web apps, implementing INTERFACE/SERVICE/MODELS layers.  
In the interface, _components_ folder, are the components that the user will interact with.  
In the _service_, some business logic and backend calls are stored. The interface evokes the services to retrieve/alter data.  
In the _models_, objects used throughout the application are declared.  

There is also a _assets_ folder, that stores images and files used in the app.

# Starting the client

After installing the required packages with `npm install`, a simple `ng serve` in the console should set up the client.
