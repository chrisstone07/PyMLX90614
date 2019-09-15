from mlx90614 import MLX90614
from smbus2 import SMBus

if __name__ == "__main__":
    address = 0x5A
    bus = SMBus(1)
    sensor = MLX90614(bus, address)
    print sensor.get_amb_temp()
    print sensor.get_obj_temp()
