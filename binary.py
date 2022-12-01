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


def bubble_sort(dizi):
    n = boyut
    for i in range(n):
        for j in range(n-i-1):
            if (dizi[j] > dizi[j+1]):
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]

    return dizi


print("siralanmamis dizi : ", dizi1)
x = int(input("hangi degeri arayacaksiniz ? : "))

def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1

print("siralanmis dizi:" ,bubble_sort(dizi1))


print("BINARY SEARCH İCİN ARAMA SONUCU  : ")
result_binary = binary_search(bubble_sort(dizi1), 0, boyut-1, x)
if result_binary != -1:
	print("Element is present at index", str(result_binary))
else:
	print("Element is not present in array")


class Window(QMainWindow):

    # değişken

    number = bubble_sort(dizi1)

    def __init__(self):
        super().__init__()

        # program adı
        self.setWindowTitle("Binary arama ")

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
        self.binary_search_button = QPushButton("Binary", self)
        # Butonların konumu
        self.binary_search_button.setGeometry(100, 30, 100, 30)

        # Butonlara basınca çalışacak fonksiyonlar
        self.binary_search_button.clicked.connect(self.binary_search_action)
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

        if self.binaryStart:
            # binary araması
            self.mid = (self.first + self.last)//2

            if self.first > self.last:
                self.binaryStart = False
                self.result.setText("Bulunamadı")

            if self.number[self.mid] == self.desired:

                self.binaryStart = False

                self.result.setText("Değer bulundu : " + str(self.mid))

                self.label_list[self.mid].setStyleSheet(
                    "border : 2px solid green; "
                    "background-color : lightgreen")

            else:
                self.label_list[self.mid].setStyleSheet(
                    "border : 1px solid black; "
                    "background-color : grey")

            if self.number[self.mid] > self.desired:
                self.last = self.mid - 1

            if self.number[self.mid] < self.desired:
                self.first = self.mid + 1

    def binary_search_action(self):
        self.binaryStart = True
        self.result.setText("Binary arama başladı...")

    def pause_action(self):
        self.start = False
        self.result.setText("Paused")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

