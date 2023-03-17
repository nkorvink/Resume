This program is an edited version of a3, where when a response is sent to the server, 
before it is sent it checks if there is a @[KETWORD] that it will then replace the @[KEYWORD] with data pulled from an API. 
Then the message is sent to the server. It does this by seperating the message into a list, searching for the @[KETWORD]
in the list, and then replacing the value with the intended valuse, pulled from an API.