# AcromeBBT_Demo

The provided Python code establishes communication between the Acrome Ball Balancing Table interface and the Acrome Smart Motor Drivers. Here's a summary of the code:

The code imports necessary modules, classes, and functions for the program to run, including smd, socket, copy, sys, traceback, struct, time, and concurrent.futures.
It creates a queue object s_q for sharing data between threads.
The Server class is defined, which creates a socket and receives data from a client.
The loop_server function continuously receives position data from a server and puts it into a queue for further processing.
The loop_smd function continuously reads joystick data and sends it to a server while also receiving data from the server to control two actuators.
The code tries to assign the string 'COM5' to the variable smd_port. If an IndexError occurs, it means the user did not provide the correct number of command line arguments.
Several objects and variables are initialized, including an instance of the Master class for communication with hardware devices, an instance of the Server class, and a socket object for UDP communication.
A thread pool executor is created with a maximum of 6 worker threads. The loop_server and loop_smd functions are submitted to the executor to run in separate threads.
Exception handling is performed to catch and print any exceptions that occur during the execution of the server and master daemon threads.
Please note that without the specific implementations of the Server and Master classes, it's difficult to provide a comprehensive understanding of the code's functionality and how it interacts with the Acrome Ball Balancing Table and Smart Motor Drivers.
