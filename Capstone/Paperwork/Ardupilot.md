#Process Ardupilot.pde

##Preamble
*	Include all the required libraries for the system
*	Include Local modules "defines.h","Parameters.h","GCS.h" (Ground Control Station)

##Initializing process
*	Initialize Serial ports for FTDI (Serial to USB), GPS and Telemetry each named Serial1,2,3 respectively.
*	Param_loader ??? weird stuff
*	Create Arduino_Mega_ISR_Registery object to hold ISR functions

