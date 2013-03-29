#ifndef _SENSORINIT_H_
#define _SENSORINIT_H_

// Include Wire.h for I2C conveniant functions
#include <Wire.h>

// Accelerometer Addresses (ADXL345) 10-bit
#define ACCEL_ADDR 0x53

#define ACCEL_POWER_CTL 0x2D;	//Power Control Register
#define ACCEL_DATA_FORMAT 0x31;
#define ACCEL_DATAX0 0x32;	//X-Axis Data 0
#define ACCEL_DATAX1 0x33;	//X-Axis Data 1
#define ACCEL_DATAY0 0x34;	//Y-Axis Data 0
#define ACCEL_DATAY1 0x35;	//Y-Axis Data 1
#define ACCEL_DATAZ0 0x36;	//Z-Axis Data 0
#define ACCEL_DATAZ1 0x37;	//Z-Axis Data 1

// Gyroscope Address (L3G4200D) 8-bit
#define GYRO_ADDR 0x68

#define GYRO_CTRL_REG1 0x20
#define GYRO_CTRL_REG2 0x21
#define GYRO_CTRL_REG3 0x22
#define GYRO_CTRL_REG4 0x23
#define GYRO_CTRL_REG5 0x24

#define GYRO_DATAXL 0x28
#define GYRO_DATAXH 0x29
#define GYRO_DATAYL 0x2A
#define GYRO_DATAYH 0x2B
#define GYRO_DATAZL 0x2C
#define GYRO_DATAZH 0x2D

// Compass Address (HMC5883L) 8-bit
#define COMP_ADDR 0x1E

#define COMP_CONFREGA 0x00
#define COMP_CONFREGB 0x01
#define COMP_MODEREG 0x02
#define COMP_DATAXL 0x03
#define COMP_DATAXH 0x04
#define COMP_DATAZL 0x05
#define COMP_DATAZH 0x06
#define COMP_DATAYL 0x07
#define COMP_DATAYH 0x08

// Barometer Address (BMP085) 16-bit
#define BARO_ADDR 0x77

#define BARO_CAL_AC1 0xAA  // R   Calibration data (16 bits)
#define BARO_CAL_AC2 0xAC  // R   Calibration data (16 bits)
#define BARO_CAL_AC3 0xAE  // R   Calibration data (16 bits)
#define BARO_CAL_AC4 0xB0  // R   Calibration data (16 bits)
#define BARO_CAL_AC5 0xB2  // R   Calibration data (16 bits)
#define BARO_CAL_AC6 0xB4  // R   Calibration data (16 bits)
#define BARO_CAL_B1 0xB6  // R   Calibration data (16 bits)
#define BARO_CAL_B2 0xB8  // R   Calibration data (16 bits)
#define BARO_CAL_MB 0xBA  // R   Calibration data (16 bits)
#define BARO_CAL_MC 0xBC  // R   Calibration data (16 bits)
#define BARO_CAL_MD 0xBE  // R   Calibration data (16 bits)

#define BARO_CONTROL 0xF4
#define BARO_TEMPDATA 0xF6
#define BARO_PRESSUREDATA 0xF6
#define BARO_READTEMPCMD 0x2E
#define BARO_READPRESSURECMD 0x34


// Base Functions

void writeTo(uint8_t device,uint8_t address, uint8_t val) {
    Wire.beginTransmission(device); // start transmission to device
    Wire.write(address);             // send register address
    Wire.write(val);                 // send value to write
    Wire.endTransmission();         // end transmission
}

void readI2C(uint8_t device,uint8_t address,uint8_t bufferlength,uint8_t* buffer){
    Wire.beginTrasnmission(device);
    Wire.write(address);
    Wire.endTransmission;

    Wire.beginTransmission(device);
    Wire.requestFrom(device,bufferlength);

    unsigned int i = 0;
    while(Wire.available()){
        buffer[i]=Wire.read();
        i++;
        }
    Wire.endTransmission();
    }

void sensorInit(void){
    // Begin Wire
    Wire.begin();

    // Initialize Accelerometer
    //Put the ADXL345 into +/- 4G range by writing the value 0x01 to the DATA_FORMAT register.
    writeTo(ACCEL_DATA_FORMAT, 0x01);
    //Put the ADXL345 into Measurement Mode by writing 0x08 to the POWER_CTL register.
    writeTo(ACCEL_POWER_CTL, 0x08);

    // Initialize Gyroscope
    setupL3G4200D(500);

    // Initialize Compass
    writeTo(COMP_ADDR,0x00);
    writeTo(COMP_ADDR,0x02);

    // Initialize Barometer

    }

void setupL3G4200D(int scale){
  //From  Jim Lindblom of Sparkfun's code

  // Enable x, y, z and turn off power down:
  writeTo(GYRO_ADDR, GYRO_CTRL_REG1, 0x0F);

  // If you'd like to adjust/use the HPF, you can edit the line below to configure CTRL_REG2:
  writeTo(GYRO_ADDR, GYRO_CTRL_REG2, 0x00);

  // Configure CTRL_REG3 to generate data ready interrupt on INT2
  // No interrupts used on INT1, if you'd like to configure INT1
  // or INT2 otherwise, consult the datasheet:
  writeTo(GYRO_ADDR, GYRO_CTRL_REG3, 0x08);

  // CTRL_REG4 controls the full-scale range, among other things:

  if(scale == 250){
    writeTo(GYRO_ADDR, GYRO_CTRL_REG4, 0x00);
  }else if(scale == 500){
    writeTo(GYRO_ADDR, GYRO_CTRL_REG4, 0x10);
  }else{
    writeTo(GYRO_ADDR, GYRO_CTRL_REG4, 0x30);
  }

  // CTRL_REG5 controls high-pass filtering of outputs, use it
  // if you'd like:
  writeTo(GYRO_ADDR, GYRO_CTRL_REG5, 0x00);
}

#endif //_SENSORINIT_H_
