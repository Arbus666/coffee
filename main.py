import sqlite3
import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>712</width>
    <height>396</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>300</y>
      <width>191</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Показать информацию</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>161</width>
      <height>241</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>30</y>
      <width>171</width>
      <height>231</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>30</y>
      <width>161</width>
      <height>221</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>712</width>
     <height>36</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)  # загружаем дизайн
        self.pushButton.clicked.connect(self.display_coffee_info)

    def display_coffee_info(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        coffee_data = cursor.fetchall()
        for coffee in coffee_data:
            coffee_id = coffee[0]
            coffee_name = coffee[1]
            roast_level = coffee[2]
            ground_or_whole = coffee[3]
            flavor_description = coffee[4]
            price = coffee[5]
            package_volume = coffee[6]
            self.label.setText(f"ID: {coffee_id}\n"
                               f"Название сорта: {coffee_name}\n"
                               f"Степень обжарки: {roast_level}\n"
                               f"Молотый/в зернах: {ground_or_whole}\n"
                               f"Описание вкуса: {flavor_description}\n"
                               f"Цена: {price}\n"
                               f"Объем упаковки: {package_volume}")
            break

        count = 1
        for coffee in coffee_data:
            if count == 3:
                break
            else:
                coffee_id = coffee[0]
                coffee_name = coffee[1]
                roast_level = coffee[2]
                ground_or_whole = coffee[3]
                flavor_description = coffee[4]
                price = coffee[5]
                package_volume = coffee[6]
                self.label_2.setText(f"ID: {coffee_id}\n"
                                     f"Название сорта: {coffee_name}\n"
                                     f"Степень обжарки: {roast_level}\n"
                                     f"Молотый/в зернах: {ground_or_whole}\n"
                                     f"Описание вкуса: {flavor_description}\n"
                                     f"Цена: {price}\n"
                                     f"Объем упаковки: {package_volume}")
                count += 1

        count = 1
        for coffee in coffee_data:
            if count == 4:
                break
            else:
                coffee_id = coffee[0]
                coffee_name = coffee[1]
                roast_level = coffee[2]
                ground_or_whole = coffee[3]
                flavor_description = coffee[4]
                price = coffee[5]
                package_volume = coffee[6]
                self.label_3.setText(f"ID: {coffee_id}\n"
                                     f"Название сорта: {coffee_name}\n"
                                     f"Степень обжарки: {roast_level}\n"
                                     f"Молотый/в зернах: {ground_or_whole}\n"
                                     f"Описание вкуса: {flavor_description}\n"
                                     f"Цена: {price}\n"
                                     f"Объем упаковки: {package_volume}")
                count += 1
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
