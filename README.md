# ESP32-S3-WROOM-1-N16R8

## Datasheet:

- https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf

## Docs:
- https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html

![ESP32-S3-WROOM-1 N16R8 DevKitC v1.1](ESP32-S3_DevKitC-1.1.png)

## ESP-IDF:
- [Link](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/linux-macos-setup.html)
## MicroPython
- [Link](https://github.com/micropython/micropython/blob/master/ports/esp32/README.md)

# MicroPython ESP32-S3 N16R8
## Build

# Tested on Ubuntu WSL 2024.
- ``` wsl --install Ubuntu ```

### Una vez instalado Ubuntu:
#### Actualizar e instalar requerimientos:
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install -y build-essential git wget flex bison gperf pkg-config python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```

### Clonar Esta repo, MicroPython y ESP-IDF compatible con MicroPython(En la actualidad 5.04 a 5.1.2):
```bash
git clone https://github.com/PIBSAS/ESP32-S3-WROOM-1-N16R8.git
```
```bash
git clone https://github.com/micropython/micropython.git
```
```bash
mkdir esp
cd esp
git clone -b v5.0.4 --recursive https://github.com/espressif/esp-idf.git
```

### Instalar CMake mediante idf_tools.py:
```bash
cd esp-idf/tools
```
```bash
python3 idf_tools.py install cmake
```

### Regresar un directorio y ejuctar el script para ESP32S3:
```bash
cd ..
./install.sh esp32s3
```

### Ejecutar:
```bash
. ./export.sh
```

### Copiar el directorio GENERIC_S3_N16R8 y su contenido al directorio boards:
```bash
cd
cp -r MicroPython-ESP32-S3-N16R8/GENERIC_S3_N16R8 micropython/ports/esp32/boards
```

### Dirigirnos al directorio MicroPython y ejecutar mpy-cross:
```bash
cd
cd micropython/
make -C mpy-cross
```

### Movernos a ports/esp32 y ejecutar submodules:
```bash
cd ports/esp32/
```
```bash
make submodules
```
### Indicar el IDF_TARGET
```bash
export IDF_TARGET=esp32s3
```
### Compillar MicroPython para ESP32 S3
```bash
make BOARD=GENERIC_S3_N16R8
```
#### Al final nos indica
- Project build complete. To flash, run this command:
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p (PORT) -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 build-GENERIC_S3_N16R8/bootloader/bootloader.bin 0x8000 build-GENERIC_S3_N16R8/partition_table/partition-table.bin 0x10000 build-GENERIC_S3_N16R8/micropython.bin
```

#### Or run 'idf.py -p (PORT) flash'
| bootloader  |  @0x000000  |  18672  (   14096 remaining)  |
|-------------|-------------|-------------------------------|
| partitions  | @0x008000   |   3072  (    1024 remaining)  |
| application | @0x010000   | 1396208  (  635408 remaining) |
| total       |             | 1461744                       |

- Se debe cambiar ``(PORT)`` por ``COM29`` por ejemplo o en linux ``/dev/ttyACM0``

# Windows:
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyACM0 erase_flash
```
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p COM29 -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 build-GENERIC_S3_N16R8/bootloader/bootloader.bin 0x8000 build-GENERIC_S3_N16R8/partition_table/partition-table.bin 0x10000 build-GENERIC_S3_N16R8/micropython.bin
```

# WSL:
## Instalar USBIPD:
```bash
winget install --interactive --exact dorssel.usbipd-win
```

### Abrir Terminal(Administrador) enchufar el esp32 y escribir:
```bash
usbipd list
```
- Observar el ``BUSID`` del esp ``(USB-Enhanced-SERIAL CH343 (COM29)``. Ej: ``2-1``

### Escribir:
```bash
usbipd bind --busid 2-1
```

```bash
usbipd attach --wsl --busid 2-1
```
## En WSL Ubuntu(Distro) agregar el usuario al grupo ``dialout``:
```bash
sudo adduser $USER dialout
```

### En Terminal(Administrador) Comprobar que figure Attached en la columna STATE con:
```bash
usbipd list
``` 
### Luego en WSL borramos la flash:
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyACM0 erase_flash
```

```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyACM0 -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 build-GENERIC_S3_N16R8/bootloader/bootloader.bin 0x8000 build-GENERIC_S3_N16R8/partition_table/partition-table.bin 0x10000 build-GENERIC_S3_N16R8/micropython.bin
```
# Linux:
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyACM0 erase_flash
```
```bash
$HOME/.espressif/python_env/idf5.0_py3.10_env/bin/python ../../../esp/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyACM0 -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 build-GENERIC_S3_N16R8/bootloader/bootloader.bin 0x8000 build-GENERIC_S3_N16R8/partition_table/partition-table.bin 0x10000 build-GENERIC_S3_N16R8/micropython.bin
```

## Reference

+ [micropython/micropython/issues/8635](https://github.com/micropython/micropython/issues/8635#issuecomment-1129218506)
