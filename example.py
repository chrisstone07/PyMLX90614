from mlx90614 import MLX90614

if __name__ == "__main__":
    address = 0x5A
    sensor = MLX90614(address)
    print sensor.get_amb_temp()
    print sensor.get_obj_temp()
