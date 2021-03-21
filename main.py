import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaContent
import gui


class OniPlayer(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.depth_media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.color_media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.depth_media_player.setVideoOutput(self.video_widget_left)
        self.color_media_player.setVideoOutput(self.video_widget_right)
        self.depth_media_player.stateChanged.connect(self.media_state_changed)
        self.depth_media_player.positionChanged.connect(self.position_changed)
        self.depth_media_player.durationChanged.connect(self.set_duration)

        self.depth_buffer = QtCore.QBuffer()

        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_video)

        self.stop_button.setEnabled(False)
        self.stop_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.stop_button.clicked.connect(self.stop_video)

        self.next_button.setEnabled(False)
        self.next_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipForward))
        self.next_button.clicked.connect(self.get_next_frame)

        self.prev_button.setEnabled(False)
        self.prev_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipBackward))
        self.prev_button.clicked.connect(self.get_prev_frame)

        self.open_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton))
        self.open_button.clicked.connect(self.open_device)

        self.quit_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogCancelButton))
        self.quit_button.clicked.connect(self.quit_player)

        self.horizontalSlider.setRange(0, 0)
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        self.horizontalSlider.sliderPressed.connect(self.play_video)
        self.horizontalSlider.sliderReleased.connect(self.play_video)

    def open_device(self):
        path = self.browse_folder()
        if path:
            self.depth_media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(path)))
            self.color_media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(path)))

            self.play_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.next_button.setEnabled(True)
            self.prev_button.setEnabled(True)

    def play_video(self):
        if self.depth_media_player.state() == QMediaPlayer.PlayingState:
            self.depth_media_player.pause()
            self.color_media_player.pause()
        else:
            self.depth_media_player.play()
            self.color_media_player.play()

    def stop_video(self):
        if self.depth_media_player.state() == QMediaPlayer.PlayingState \
                or self.depth_media_player.state() == QMediaPlayer.PausedState:
            self.depth_media_player.stop()
            self.color_media_player.stop()

    def media_state_changed(self):
        if self.depth_media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
            self.play_button.setText('Pause')
        else:
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            self.play_button.setText('Play')

    def position_changed(self, position):
        self.horizontalSlider.setSliderPosition(position)

    def set_duration(self, duration):
        self.horizontalSlider.setRange(0, duration)

    def set_position(self, position):
        self.depth_media_player.setPosition(position)
        self.color_media_player.setPosition(position)

    def get_next_frame(self):
        if self.depth_media_player.state() == QMediaPlayer.PlayingState \
                or self.depth_media_player.state() == QMediaPlayer.PausedState:
            self.horizontalSlider.setSliderPosition(self.horizontalSlider.value() + 1000)
            self.set_position(self.horizontalSlider.value())

    def get_prev_frame(self):
        if self.depth_media_player.state() == QMediaPlayer.PlayingState \
                or self.depth_media_player.state() == QMediaPlayer.PausedState:
            self.horizontalSlider.setSliderPosition(self.horizontalSlider.value() - 1000)
            self.set_position(self.horizontalSlider.value())

    def browse_folder(self):
        p = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users')
        return p[0]

    def quit_player(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = OniPlayer()
    player.show()
    sys.exit(app.exec_())
