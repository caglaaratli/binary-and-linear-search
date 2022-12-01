# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from numpy import random

boyut = int(
    input("kac elemanlı bir dizi siralanacak ve icerisinde eleman aranacak ?"))
dizi1 = random.randint(100, size=boyut)


def lineer_search(arr, x):
    for i in range(boyut):
        if arr[i] == x:
            return i
    return -1


print("siralanmamis dizi : ", dizi1)
x = int(input("hangi degeri arayacaksiniz ? : "))

print("LINEER SEARCH İCİN ARAMA SONUCU :")
result_lineer = lineer_search(dizi1, x)
if (result_lineer != -1):
    print("Element found at index: ", result_lineer)
else:
    print("Element not found")


class Window(QMainWindow):
    # değişken

    number = dizi1

    def __init__(self):
        super().__init__()

        # program adı
        self.setWindowTitle("Linear arama ")

        # pencere büyüklüğü
        self.setGeometry(100, 100, 1280, 720)
        self.UiComponents()
        self.show()

    def UiComponents(self):

        # kontrol değişkenleri
        self.start = False
        self.binaryStart = False

        self.label_list = []

        # aranacak değer
        self.desired = x

        # sayaç
        self.counter = 0
        # binary arama için gerekli değişkenler
        self.first = 0
        self.last = len(self.number) - 1
        self.mid = 0
        # fonksiyon sayacı
        c = 0

        # grafiği oluştur
        for i in self.number:
            label = QLabel(str(i), self)

            # grafik stil özellikleri
            label.setStyleSheet("border: 1px solid black;background: white ")

            # grafiğin içindeki yazının konumu
            label.setAlignment(Qt.AlignBottom)

            label.setGeometry(50 + c * 30, 290, 20, i + 10)

            self.label_list.append(label)

            c = c + 1
        # Butonlar
        self.search_button = QPushButton("Linear", self)

        # Butonların konumu
        self.search_button.setGeometry(100, 70, 100, 30)

        # Butonlara basınca çalışacak fonksiyonlar
        self.search_button.clicked.connect(self.search_action)

        # Durdur butonu
        pause_button = QPushButton("Durdur", self)

        # Durdur butonunun konumu
        pause_button.setGeometry(100, 120, 100, 30)

        # basınca ne olacak ?
        pause_button.clicked.connect(self.pause_action)

        # Text kısmı
        self.result = QLabel("Aranan Değer : " + str(self.desired), self)

        # text konumu
        self.result.setGeometry(350, 120, 300, 40)

        # text stili
        self.result.setStyleSheet("border : 3px solid black;")

        # Font ekleyelim
        self.result.setFont(QFont('Times', 10))

        # Texti center aldık
        self.result.setAlignment(Qt.AlignCenter)

        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        # grafiğin animasyon süresi
        timer.start(200)

    def showTime(self):

        if self.start:

            if self.label_list[self.counter].text() == str(self.desired):

                self.label_list[self.counter].setStyleSheet(
                    "border: 1px solid black;background: lightgreen")

                self.result.setText("Değer Bulundu : "
                                    + str(self.counter))

                self.start = False

                self.counter = 0

            else:

                self.label_list[self.counter].setStyleSheet(
                    "border: 1px solid black; background: grey")

            self.counter += 1

            if self.counter == len(self.label_list):
                self.start = False

                self.result.setText("Bulunamadı")

    def search_action(self):
        self.start = True
        self.result.setText("Linear arama başladı...")

    def pause_action(self):
        self.start = False
        self.result.setText("Paused")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
