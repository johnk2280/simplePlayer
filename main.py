import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qimage2ndarray
import cv2


class OniPlayer(QtWidgets.QWidget):

    def __init__(self, width=1280, height=720, fps=33):
        super().__init__()

        self.video = None
        self.play = None
        self.pause = None

        # Инициализируем переменные для Видео
        self.video_size = QtCore.QSize(width, height)
        self.camera_capture = cv2.VideoCapture(cv2.CAP_DSHOW)
        self.video_capture = cv2.VideoCapture()
        self.fps = fps
        self.frame_timer = QtCore.QTimer()

        # Вызываем функцию запуска камеры
        self.setup_camera(fps)

        # Инициализируем переменные для GUI
        self.frame_label = QtWidgets.QLabel()
        self.quit_button = QtWidgets.QPushButton('Quit')
        self.play_pause_button = QtWidgets.QPushButton('Play')
        self.stop_button = QtWidgets.QPushButton('Stop')
        self.next_button = QtWidgets.QPushButton('Next')
        self.prev_button = QtWidgets.QPushButton('Previous')
        self.browse_button = QtWidgets.QPushButton('Open')
        self.horizontal_slider = QtWidgets.QSlider(self.frame_label)
        self.camera_video_button = QtWidgets.QPushButton('Switch to video')

        self.main_layout = QtWidgets.QGridLayout()

        # Вызываем фцнкцию отрисовки GUI
        self.setup_ui()

    def setup_ui(self):
        # Главное окно
        self.setWindowTitle('ONI Player')
        self.setWindowIcon(QtGui.QIcon('media/player-play_114441.png'))
        # self.show()

        # Поле вывода изображения
        self.frame_label.setFixedSize(self.video_size)

        # Коннектим кнопки с функциями класса
        self.quit_button.clicked.connect(self.close_win)
        self.play_pause_button.clicked.connect(self.play_pause_video)
        self.stop_button.clicked.connect(self.stop_video)
        self.next_button.clicked.connect(self.get_next_video_frame)
        self.prev_button.clicked.connect(self.get_prev_video_frame)
        self.browse_button.clicked.connect(self.browse_folder)
        self.camera_video_button.clicked.connect(self.switch_camera_video)


        # Распологаем слайдер по горизонтали
        self.horizontal_slider.setOrientation(QtCore.Qt.Horizontal)

        # Рисуем поля для кнопок и поля вывода изображения
        self.main_layout.addWidget(self.frame_label, 0, 0, 1, 4)
        self.main_layout.addWidget(self.quit_button, 6, 0, 1, 4)
        self.main_layout.addWidget(self.stop_button, 3, 0, 1, 1)
        self.main_layout.addWidget(self.prev_button, 3, 1, 1, 1)
        self.main_layout.addWidget(self.play_pause_button, 3, 2, 1, 1)
        self.main_layout.addWidget(self.next_button, 3, 3, 1, 1)
        self.main_layout.addWidget(self.camera_video_button, 4, 0, 1, 4)
        self.main_layout.addWidget(self.browse_button, 5, 0, 1, 4)
        self.main_layout.addWidget(self.horizontal_slider, 1, 0, 2, 4)

        self.setLayout(self.main_layout)

    def setup_camera(self, fps):
        self.camera_capture.set(3, self.video_size.width())
        self.camera_capture.set(4, self.video_size.height())

        self.frame_timer.timeout.connect(self.display_video_stream)
        self.frame_timer.start(int(1000 // fps))

    def display_video_stream(self):
        if not self.video:
            ret, frame = self.camera_capture.read()
        else:
            ret, frame = self.video_capture.read()

        if not ret:
            return False

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Конвертация цвета в RGB
        if not self.video:
            frame = cv2.flip(frame, 1)  # делаем зеркальное отображение с камеры
        else:
            frame = cv2.resize(frame, (self.video_size.width(), self.video_size.height()), interpolation=cv2.INTER_AREA)

        image = qimage2ndarray.array2qimage(frame)
        self.frame_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def close_win(self):
        # Добавить логику для завершения openni
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            cv2.destroyAllWindows()
            self.camera_capture.release()
            self.video_capture.release()
            self.close()

    def play_pause_video(self):
        if not self.pause:
            self.frame_timer.stop()
            self.play_pause_button.setText('Play')
        else:
            self.frame_timer.start(int(1000 // self.fps))
            self.play_pause_button.setText('Pause')
        self.pause = not self.pause

    def switch_camera_video(self):
        if not self.video:
            path = self.browse_folder()
            if len(path[0]):
                self.video_capture.open(path[0])
                self.camera_video_button.setText('Switch to camera')
        else:
            self.camera_video_button.setText('Switch to video')
            self.video_capture.release()
        self.video = not self.video

    def stop_video(self):
        pass

    def get_next_video_frame(self):
        pass

    def get_prev_video_frame(self):
        pass

    def browse_folder(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users', filter='*.mp4')
        return path


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = OniPlayer()
    player.show()
    sys.exit(app.exec_())
