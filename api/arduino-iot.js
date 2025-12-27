const { ArduinoIoTCloud } = require('@arduino/arduino-iot-js');

ArduinoIoTCloud.connect(options)
  .then(() => {
    console.log("Connected to Arduino Cloud");
    return ArduinoIoTCloud.onPropertyValue(thingId, variableName, showUpdates = value => console.log(value));
  })
  .then(() => console.log("Callback registered"))
  .catch(error => console.log(error));
