import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="You need to attend Meeting at 9pm",
        message="It's important!!",
        app_icon="C:\\Users\\Shaily Priya\\Documents\\noti\\icon.ico",
        timeout=10,
    )
