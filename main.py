import sys
import os
import moviepy
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from moviepy.editor import AudioClip
import PyQt5
from sampel import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Dialog)
Dialog.show()
Qfile = None
mp3_or_mp4 = None
wav = '.wav'
mp3 = '.mp3'
ogg = '.ogg'
selected_format = None


def program():
    def SelectDerectory_MP4():
        global mp3_or_mp4
        mp3_or_mp4 = True
        global mp4_file
        Qfile, _ = QFileDialog.getOpenFileName()
        if Qfile:
            ui.label.setText(str(Qfile))
            mp4_file = Qfile

    def SelectDerectory_MP3():
        global mp3_file
        global Qfile
        global mp3_or_mp4
        mp3_or_mp4 = False
        Qfile, _ = QFileDialog.getOpenFileName()
        if Qfile:
            ui.label.setText(str(Qfile))
            mp3_file = Qfile

    def Convert():
        global Qfile
        global format
        if mp3_or_mp4:
            video_clip = VideoFileClip(mp4_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(mp4_file + selected_format)

        if not mp3_or_mp4:
            global mp3_file
            audio_file = AudioFileClip(mp3_file)
            audio_file.write_audiofile(mp3_file + selected_format)

    def set_selected_format(index):
        global selected_format
        format_mapping = {0: mp3, 1: ogg, 2: wav}
        selected_format = format_mapping[index]

    ui.pushButton_2.clicked.connect(Convert)
    ui.pushButton.clicked.connect(SelectDerectory_MP4)
    ui.pushButton_3.clicked.connect(SelectDerectory_MP3)
    ui.comboBox.currentIndexChanged.connect(set_selected_format)
    ui.comboBox.addItem(mp3)
    ui.comboBox.addItem(ogg)
    ui.comboBox.addItem(wav)


program()
sys.exit(app.exec_())
