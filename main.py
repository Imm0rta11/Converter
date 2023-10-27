try:
    import sys
    import os
    import moviepy
    from moviepy.editor import VideoFileClip
    from moviepy.editor import AudioFileClip
    from moviepy.editor import AudioClip
    import PyQt5
    from ui_ import Ui_MainWindow
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
    from PyQt5 import uic
except ImportError:
    print('LOG: Import Error')
    os.exit()
else:
    print('LOG: Import has inited!')
 
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
format_mapping = {0: mp3, 1: ogg, 2: wav}
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
        print(Qfile)

    def SelectDerectory_MP3():
            global mp3_file
            global Qfile
            global mp3_or_mp4
            mp3_or_mp4 = False
            Qfile, _ = QFileDialog.getOpenFileName()
            if Qfile:
                ui.label.setText(str(Qfile))
                mp3_file = Qfile
            print(Qfile)

    def Convert():
        try:
            global Qfile
            global format
            if Qfile:
                file_type = os.path.splitext(Qfile)[1]
            if file_type == wav or file_type == mp3 or file_type == ogg:
                if mp3_or_mp4:
                    video_clip = VideoFileClip(mp4_file)
                    audio_clip = video_clip.audio
                    audio_clip.write_audiofile(mp4_file + selected_format)

                if not mp3_or_mp4 and file_type:
                    global mp3_file
                    audio_file = AudioFileClip(mp3_file)
                    audio_file.write_audiofile(mp3_file + selected_format)
            else:
                ui.label.setText('Please chose correct format file!')
        except NameError:
            print('LOG: directore has not chose')


    def set_selected_format(index):
        try:
            global selected_format
            selected_format = format_mapping[index]
        except IndexError:
            print('LOG: list out of range')

    try:
        ui.pushButton_2.clicked.connect(Convert)
        ui.pushButton.clicked.connect(SelectDerectory_MP4)
        ui.pushButton_3.clicked.connect(SelectDerectory_MP3)
        ui.comboBox.currentIndexChanged.connect(set_selected_format)
        ui.comboBox.addItem(mp3)
        ui.comboBox.addItem(ogg)
        ui.comboBox.addItem(wav)
    except :
        pass
    else:
        print('LOG: Button has inited and connected!')

program()
sys.exit(app.exec_())
