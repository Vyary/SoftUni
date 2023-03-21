from abc import ABC, abstractmethod


class ISender(ABC):
    def __init__(self, sender: str):
        self.sender = sender

    @abstractmethod
    def format(self) -> str:
        pass


class IMSender(ISender):
    def format(self) -> str:
        return "".join(["I'm ", self.sender])


class IReceiver(ABC):
    def __init__(self, receiver: str):
        self.receiver = receiver

    @abstractmethod
    def format(self) -> str:
        pass


class IMReceiver(IReceiver):
    def format(self) -> str:
        return "".join(["I'm ", self.receiver])


class IContent(ABC):
    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def format(self) -> str:
        pass


class MyContent(IContent):
    def format(self) -> str:
        return "\n".join(["<myML>", self.content, "</myML>"])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender: ISender):
        pass

    @abstractmethod
    def set_receiver(self, receiver: IReceiver):
        pass

    @abstractmethod
    def set_content(self, content: IContent):
        pass


class Email(IEmail):
    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IReceiver):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self) -> str:
        return (
            f"Sender: {self.__sender}\n"
            f"Receiver: {self.__receiver}\n"
            f"Content:\n{self.__content}"
        )


email = Email()
sender = IMSender("qmal")
email.set_sender(sender)
receiver = IMReceiver("james")
email.set_receiver(receiver)
content = MyContent("Hello, there!")
email.set_content(content)
print(email)
