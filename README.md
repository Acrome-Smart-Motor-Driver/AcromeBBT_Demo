# Acrome Ball Balancing Table - Acrome Smart Motor Driver Communication

This Python code facilitates communication between the Acrome Ball Balancing Table interface and the Acrome Smart Motor Drivers. It allows data exchange between the interface and the motor drivers, enabling control of the table's actuators based on joystick input.

## Code Overview

The provided Python code consists of the following components:

1. Importing necessary modules and classes: The required modules and classes for the program's functionality are imported, including socket, copy, sys, traceback, struct, time, and concurrent.futures.

2. Server Class: This class creates a socket and receives data from a client.

3. `loop_server` Function: This function continuously receives position data from a server and shares it with a master by putting it into a queue.

4. `loop_smd` Function: This function continuously reads joystick data and sends it to a server while also receiving data from the server to control two actuators.

5. Exception Handling: The code handles exceptions that may occur during the execution of the server and master daemon threads.

## Usage

To use this code for communication between the Acrome Ball Balancing Table interface and the Acrome Smart Motor Drivers, follow these steps:

1. Ensure that the necessary Python modules are installed. You can use `pip` to install any missing dependencies.

2. Connect the Acrome Ball Balancing Table and the Acrome Smart Motor Drivers to your system.

3. Adjust the code as needed to specify the correct IP address, port, and any other configuration details for the server and socket objects.

4. Run the Python script.

## Notes

- This code assumes the availability of the `smd.smd` module, which contains the `Master` and `Index` classes required for motor driver communication. Make sure this module is present or importable.

- The specific implementation details of the `Server` and `Master` classes are not provided in the code snippet. These classes likely encapsulate the communication protocols and interfaces specific to the Acrome Ball Balancing Table and Acrome Smart Motor Drivers.

- It's important to have a clear understanding of the Acrome Ball Balancing Table and Acrome Smart Motor Driver's documentation and APIs to properly integrate and utilize this code.

- Additional error handling and exception cases may need to be implemented to ensure robustness and reliability in a production environment.

- Consider documenting the specific steps and requirements for setting up the communication between the Acrome Ball Balancing Table and the Acrome Smart Motor Drivers to provide comprehensive usage instructions.

Please consult the relevant documentation or contact the Acrome Robotics for further details on the Acrome Ball Balancing Table and Acrome Smart Motor Drivers' integration and usage.
