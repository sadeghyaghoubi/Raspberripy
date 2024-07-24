import bluetooth
import RPi.GPIO as GPIO

# تنظیم پین‌های موتور
in1 = 17
in2 = 18
in3 = 22
in4 = 23
enable_a = 24
enable_b = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)


# تابع کنترل موتورها
def motor_control(direction, speed):
    if direction == "forward":
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
    elif direction == "backward":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    elif direction == "left":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
    elif direction == "right":
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

    p_a = GPIO.PWM(enable_a, 1000)
    p_b = GPIO.PWM(enable_b, 1000)
    p_a.start(speed)
    p_b.start(speed)


# برقراری ارتباط بلوتوث
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

port = server_socket.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_socket, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("در انتظار اتصال بلوتوث هستم...")

client_socket, client_info = server_socket.accept()
print("متصل شد:", client_info)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("دریافت کردم:", data)

    # تفسیر دستورات دریافتی و کنترل موتورها
    if data == b"forward":
        motor_control("forward", 50)
    elif data == b"backward":
        motor_control("backward", 50)
    elif data == b"left":
        motor_control("left", 50)
    elif data == b"right":
        motor_control("right", 50)
    else:
        motor_control("stop", 0)

client_socket.close()
server_socket.close()
GPIO.cleanup()