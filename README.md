# ESP32-S3-WROOM-1-N16R8

## Datasheet:

- https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf

## Docs:
- https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html

![ESP32-S3-WROOM-1 N16R8 DevKitC v1.1](ESP32-S3_DevKitC-1.1.png)


# MicroPython ESP32-S3 N16R8
## Build

Tested on Ubuntu 22.04.

1. Install dependencies:

   ```bash
   sudo apt update
   sudo apt install -y build-essential git libffi-dev pkg-config python3 python3-venv
   ```

2. Clone MicroPython and this repository:

   ```bash
   git clone https://github.com/micropython/micropython.git
   git clone https://github.com/PIBSAS/ESP32-S3-WROOM-1-N16R8.git
   ```

3. Install esp-idf:

   [Link](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/linux-macos-setup.html)
   [Link](https://github.com/micropython/micropython/blob/master/ports/esp32/README.md)
   

   ```bash
   sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
   ```

   ```bash
   mkdir -p ~/esp
   cd ~/esp
   git clone -b v5.0.4 --recursive https://github.com/espressif/esp-idf.git
   ```

   ```bash
   cd ~/esp/esp-idf
   ./install.sh esp32s3
   ```

   ```bash
   . $HOME/esp/esp-idf/export.sh
   . ./export.sh
   ```
   o creamos un alias para luego tambien poder usarlo para programar.

   ### Opcional para usar esp-IDF:
   ```bash
   alias get_idf='. $HOME/esp/esp-idf/export.sh'
   ```

   ```bash
   idf.py build
   ```
   Fin del opcional, continuar con:
   
5. Copy GENERIC_S3_N16R8 to micropython/ports/esp32/boards:
   
   ```bash
   cp -r MicroPython-ESP32-S3-N16R8/GENERIC_S3_N16R8 micropython/ports/esp32/boards
   ```

6. Build:
   
   ```bash
   cd micropython/ports/esp32
   make submodules
   export IDF_TARGET=esp32s3
   make BOARD=GENERIC_S3_N16R8
   ```

## Reference

+ [micropython/micropython/issues/8635](https://github.com/micropython/micropython/issues/8635#issuecomment-1129218506)
