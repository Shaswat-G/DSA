class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
    
    def send_message(self, message: str):
        notification = self.create_notification()
        return notification.send(message)

class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()

# Usage
def notify_user(factory: NotificationFactory, message: str):
    return factory.send_message(message)

# Client code doesn't need to know about specific notification types
email_factory = EmailFactory()
notify_user(email_factory, "Welcome aboard!")