#Autoonomous system

##Include FFF document + Clean up

#Software Architecture

##Original Software
* Libraries Provided
* Basic Implmentation used as referance

##Scheduling (Interrupt Timer)
* ISR Development
* 3 Process timers (50Hz Fast, 10Hz Medium, 1Hz Slow)
 * Timer Setup Procedure
 * 50Hz used only for sensor reading and alerts ?
 * 10Hz used for actuator modification
 * 1Hz used for misc functions
* Process priorities for timer
* Process registeration mechanisim
* Function Pointers Process Array

##UART Wireless Communication
* Mavlink Protocol
* Interrupt driven

##I2C sensor communication
* I2C/TWI protocol breakdown

##Sensor Filtering and Estimation Example (Baro is easiest)
* Read Value of the sensor and register it into the buffer array
* Apply Kalman filter to the reading (High frequency => previous state as estimate)
* Using the filtered value it is passed through the conversion algortithm to get a value for the height.
* Use the height calculated to check the condition for the required height
* Take decision action for the current flight mode

##List of Terms
* Polling
* Interrupts
* Overflow Timers
* Compartive Timers

#Appendix

##Quaternion Math
* Advantages and disadvantages
* Example for illustration purpose
