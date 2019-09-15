# PyMLX90614
Python library for MLX90614 infrared temperature sensors, using [smbus2](https://pypi.org/project/smbus2/). Compatible with Python 2 and 3.

You might need to enter this command on your Raspberry Pi:

`echo "Y" > /sys/module/i2c_bcm2708/parameters/combined`

(Consider putting it in rc.local so it's executed each bootup)

## Usage

```python
sensor = MLX90614(0x5A)
print sensor.get_amb_temp()
print sensor.get_obj_temp()
```

## License

This project is licensed under the terms of the MIT license.