import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("Hello World")
notification = Notify.Notification.new(
    "Hello World",
    "This is a test notification.",
    "dialog-information"
)
notification.show()
