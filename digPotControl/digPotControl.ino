// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// AD5254
// This code is designed to work with the AD5254_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Potentiometers?sku=AD5254_I2CPOT_10K#tabs-0-product_tabset-2

#include<Wire.h>

// AD5254 I2C address is 0x2C(44)
#define Addr 0x2C
#define pot0 0x00
#define pot1 0x01
#define pot2 0x02
#define pot3 0x03

#define RESTORE_COMMAND 0xB8
#define STORE_COMMAND_MASK 0x90

byte inSerial[16];  //Buffer for recieving commands from bluetooth connection
byte outSerial[16];  //Buffer for sending through bluetooth connection
#define ID_INDEX 0
#define CODE_INDEX 1
#define SUBBUS_INDEX 2
#define DEVICEADDRESS_INDEX 3
#define POTADDRESS_INDEX 4
#define VALUESET_INDEX 5

#define SET_CODE 'S'
#define GET_CODE 'G'
#define ACK_CODE 'A'
#define ERROR_CODE 'E'


void interfacePollingLoop(byte deviceAddress)
{
  /*
   * Polls the AD5254 until an ACK is recieved. This function must be called to ensure that
   * a write to an EPROM register completed.
   */
  
  delay(3);
  byte errorCode = 1;
  
  while (errorCode != 0)
  {
    Wire.beginTransmission(deviceAddress);
    errorCode = Wire.endTransmission();
    delay(3);
  }
}


byte getResistance(byte deviceAddress, byte potAddress)
{
  /*
   * Gets the resistance for a specific potentiometer on the specified AD5254 device.
   * Return value is an 8 bit value that represents the wiper position, NOT the actual resistance
   *  ie. For a 50k pot, a wiper position of 128 would mean R = 25k
   */

  byte resValue;

  // Start I2C transmission
  Wire.beginTransmission(deviceAddress);
  // Select data register
  Wire.write(potAddress);
  // Stop I2C transmission
  Wire.endTransmission();

  // Request RDAC value
  Wire.requestFrom(deviceAddress, 1);

  // Read RDAC value from bus
  if (Wire.available() == 1)
  {
    resValue = Wire.read();
  }

  return resValue;
}


void setResistance(byte deviceAddress, byte potAddress, byte value)
{
  /*
   * Sets the resistance for a specific potentiometer on the specified AD5254 device.
   * Value is an 8 bit value that represents the wiper position, NOT the actual resistance
   *  ie. For a 50k pot, a wiper position of 128 would mean R = 25k
   */

  //Set the RDAC to the desired value
  
  // Start I2C transmission
  Wire.beginTransmission(deviceAddress);
  // Send instruction for POT channel-0
  Wire.write(potAddress);
  Wire.write(value);
  // Stop I2C transmission
  Wire.endTransmission();


  //Save the RDAC value to ROM so that it persists between power cycles

  delay(1);
  // Start I2C transmission
  Wire.beginTransmission(deviceAddress);
  // Send instruction for POT channel-0
  Wire.write(potAddress + STORE_COMMAND_MASK);
  // Stop I2C transmission
  Wire.endTransmission();

  interfacePollingLoop(deviceAddress);
  
}


void restoreResistances(byte deviceAddress)
{
  /*
   * Restores the resistance values from the AD5254's EEPROM
   */
  
  // Start I2C transmission
  Wire.beginTransmission(deviceAddress);
  // Send instruction to resrtore from EEPROM
  Wire.write(RESTORE_COMMAND);
  // Stop I2C transmission
  Wire.endTransmission();
}


void selectSubBus(byte subBus)
{
  switch (subBus)
  {
    case 'A':
      digitalWrite(2, LOW);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      break;
    case 'B':
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(4, HIGH);
      break;
    case 'C':
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, LOW);
      break;
    default:
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      break;
  }
}


void ProcessRequest(byte inSerial[])
{
  //Exract fields from incoming request
  outSerial[ID_INDEX] = inSerial[ID_INDEX];
  byte requestCode = inSerial[CODE_INDEX];
  byte subBus = inSerial[SUBBUS_INDEX];
  byte deviceAddress = inSerial[DEVICEADDRESS_INDEX];
  byte potAddress = inSerial[POTADDRESS_INDEX];
  byte value = inSerial[VALUESET_INDEX];

  //Select correct subBus
  selectSubBus(subBus);
  
  //Set resistor value request
  if (requestCode == SET_CODE)
  {
    setResistance(deviceAddress, potAddress, value);
    outSerial[CODE_INDEX] = ACK_CODE;  //Ack code
    outSerial[2] = '\n';
    outSerial[3] = 0;  //Null terminate
  }

  //Get resistor value request
  else if (requestCode == GET_CODE)
  {
    outSerial[CODE_INDEX] = ACK_CODE;  //Ack code
    
    //Encode register value with 2 bytes, where R = B2 - B3. This prevents accidently sending a newline character as a value
    outSerial[2] = getResistance(deviceAddress, potAddress) + 1;
    outSerial[3] = 1;
    if (outSerial[2] == '\n')
    {
      //Re-encode resistor value
      outSerial[2] += 1;
      outSerial[3] = 2;
    }
    
    outSerial[4] = '\n';
    outSerial[5] = 0;  //Null terminate
  }

  //Invalid request
  else
  {
    outSerial[CODE_INDEX] = ERROR_CODE;  //Error code
    outSerial[2] = '\n';  //Null terminate
    outSerial[3] = 0;  //Null terminate
  }

  Serial.print((char *) &outSerial[0]);
}


void setup()
{
  //Use builtin LED (13) to signal start and end of setup
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  
  // Initialise serial communication, set baud rate = 9600
  Serial.begin(9600);

  //Set TX and RX pins for bluetooth module
  pinMode(1, OUTPUT);
  pinMode(0, INPUT);

  //Set pins for controlling clock sensitiby on virtual buses
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  
  // Initialise I2C communication as Master
  Wire.begin();
  
  delay(300);
  pinMode(13, OUTPUT);
  
  //Restore resistances on all potentiometers
  
    //Restore all pots on virtualBus_A
  selectSubBus((char) 'A');
  for (int i=0; i<4; i++)
  {
    restoreResistances(Addr+i);
  }

    //Restore all pots on virtualBus_B
  selectSubBus((char) 'B');
  for (int i=0; i<4; i++)
  {
    restoreResistances(Addr+i);
  }

    //Restore all pots on virtualBus_C
  selectSubBus((char) 'C');
  for (int i=0; i<2; i++)
  {
    restoreResistances(Addr+i);
  }

  digitalWrite(13, LOW);
}


void loop()
{
  int i = 0;

  delay(25);
  if (Serial.available() > 0)
  {
    while (Serial.available() > 0)
    {
      inSerial[i] = Serial.read();
      i++;
      delay(2);
    }
    inSerial[i] = 0;
    ProcessRequest(inSerial);
  }
}
