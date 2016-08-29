#Генератор банковских счетов QT-version 0.8
Программа для генерации банквоский счетов и генерации ключа проверки.

![ScreenShot](http://savepic.org/8372535.png)

## Установка на Windows
1. Установить [python 3.5](https://www.python.org/downloads/) и записать в переменные среды
2. Запустить в консоли pip3 install -r requirements.txt

##Установка на *nix
1. Установить [python 3.5](https://www.python.org/downloads/)
2. pip3 install -r requirements.txt

##Сборка под Windows
Сборка под Windows делается с помощью pyinstaller из develop ветки http://pythonhosted.org/PyInstaller/installation.html#installing-from-the-archive

Сборка acc_gen.exe
pyinstaller --onefile --noconsole main.py --name acc_gen

На данный момент у сборки таким образом есть надостаток: https://github.com/fleytman/generator_bank_accounts/issues/2

##Запуск
Двойной щелчок по main.py в проводнике или
python3 main.py в консоли

Запускалось под Windows 8 и Windows 10
