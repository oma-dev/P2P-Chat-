

IMPORTANT: The files should be run with python shell. I used (Right Click > Edit with IDLE > Edit With Idle 3.x (32 Bit), then either Run from Run > Run Module, or press F5.)

There are 4 executables total;

detectingOfficer (Service_Listener): Listens for messages (that will contain username and IPs) on port 5000, and writes them to my "phonebook", which is shared between it, server and client.

hearMeOut (Service_Advertiser): Lets me pick a username, and send it to the broadcast alongside with my IP, on port 5000. Also has a function, which helps me to find out the local broadcast IP. (The one which ends with .255)

Server (Chat_Listener): Listens to messages coming from other clients (Chat_Clients). Knows the name of the sender by checking the username corresponding to the IP, using the phonebook as a source. Closes and reopens the socket if the enduser on the other side of the socked disconnects. Any message received is logged to the "messagelog" with the timestamp and the senders username.

Client (Chat_Client): Lets me send messages to other servers (Chat_Listeners). Shows me the user list, using the phonebook as the source, and lets me message the one I want by typing his/her/their username. I can back out and message another user I want by typing "z�r�ck". Any message sent is logged to the "messagelog" with the timestamp, and "You" as the username for indicating myself.

Chatlog's are registered to be really easy to read on the "messagelog" text file, and we couldn't decide which executable to print them, so we don't have any function printing the chat logs, although we can program one if we absolutely need to do it.



The program has been tested on Windows 10.

We didn't add a Requirements.txt because no external libraries were used.

There are some example messages and contacts on messagelog.txt and phonebook.txt to give you an idea of the template.

Please excuse the silly filenames.

IMPORTANT: The files should be run with python shell. I used (Right Click > Edit with IDLE > Edit With Idle 3.x (32 Bit), then either Run from Run > Run Module, or press F5.)
