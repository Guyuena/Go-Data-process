import binascii

# 计算 CRC-8
def crc8(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x07
            else:
                crc <<= 1
    return crc & 0xFF

# 打印 CRC 结果
with open("crc_results.txt", "w") as file:
    for brightness in range(101):
        # 将亮度值转换为字节
        brightness_byte = bytes([brightness])

        # 构建数据帧
        data = bytearray([0xaa, 0xaa, 0x22, 0x20, 0x89, 0x00, 0x00, 0x01])
        data.append(brightness_byte[0])
        checksum = crc8(data)
        data.append(checksum)
        data.extend([0x55, 0x55])

        # 将数据帧转换为十六进制字符串形式
        hex_data = ' '.join(['{:02X}'.format(byte) for byte in data])

        # 打印亮度值和 CRC 结果
        print(f"{brightness}%：{hex_data}", file=file)

print("CRC 结果已写入 crc_results.txt 文件。")
