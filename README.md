# Client-Server-communication-using-sockets-||Python 
•Established connection between three physical machines
•Creation of a parallel server

This development project aims to set up a computer system
centralized auction.
Indeed, the auction is one of the oldest sales techniques. Currently,
many individuals and professionals use this sales system to get rid of
of certain objects in order to be able to obtain liquidity to finance a new project or
simply to pay off some debts. This system is structured according to the model
client-server, it provides a set of functions, manages multiple information in a
persistent, and uses a well-defined communication protocol between clients and server.
![image](https://user-images.githubusercontent.com/60547288/159450185-28e281ca-b0ec-4ef2-a878-a197713a8fdd.png)

Project components:

-Socket :
Used to establish the client-server connection in this project.
The exchange of messages between the 2 client and server machines then follows the following scenario:
Each machine creates a socket then each socket will be associated with a port of the host machine.
Once the two sockets will be explicitly connected if using a protocol in mode
connected, and each machine reads and/or writes in its socket, then the data goes from one socket
to another across the network when finished each machine closes its socket.

-Threads :
Thread is a lightweight "thread" process within the program; i.e. a sequel
linear and continuous of instructions that are executed sequentially one after the other.
We added threads to help organize the execution of each function, which
improves project performance.

-TCP Protocol :
Sockets allow us to establish a TCP/IP connection between 2 programs. There is no
no restrictions on the location of the programs they can be located remotely or
of course on the same computer (localhost 127.0.0.1). We just had to identify the connection
TCP/IP.
![image](https://user-images.githubusercontent.com/60547288/159450879-b83133f9-8032-4f06-9eaa-7010aeaab318.png)

![image](https://user-images.githubusercontent.com/60547288/159450961-251a9e91-3746-4c14-a572-23d3f8e16527.png)

![image](https://user-images.githubusercontent.com/60547288/159451030-39d553f2-539d-47e5-a641-453c4d57dfa7.png)




