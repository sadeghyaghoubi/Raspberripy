import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class RobotController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ایجاد دکمه‌های کنترلی
        forward_button = QPushButton("Forward")
        backward_button = QPushButton("Backward")
        left_button = QPushButton("Left")
        right_button = QPushButton("Right")

        # چیدمان دکمه‌ها در یک لایه عمودی
        layout = QVBoxLayout()
        layout.addWidget(forward_button)
        layout.addWidget(backward_button)
        layout.addWidget(left_button)
        layout.addWidget(right_button)

        # اتصال دکمه‌ها به توابع کنترل ربات
        forward_button.clicked.connect(self.move_forward)
        backward_button.clicked.connect(self.move_backward)
        left_button.clicked.connect(self.turn_left)
        right_button.clicked.connect(self.turn_right)

        # تنظیم پنجره اصلی
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Robot Controller")

    def move_forward(self):
        # کد برای حرکت ربات به جلو
        print("Moving forward")

    def move_backward(self):
        # کد برای حرکت ربات به عقب
        print("Moving backward")

    def turn_left(self):
        # کد برای چرخش ربات به چپ
        print("Turning left")

    def turn_right(self):
        # کد برای چرخش ربات به راست
        print("Turning right")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = RobotController()
    controller.show()
    sys.exit(app.exec_())