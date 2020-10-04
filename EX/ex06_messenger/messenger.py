"""Messenger."""


class User:
    """User class."""

    def __init__(self, name):
        """
        User constructor.

        :param name: Name of the user.
        """
        self.name = name


class Chat:
    """Chat class."""

    def __init__(self, name, users):
        """
        Chat constructor.

        :param name: Name of the chat.
        :param users: Users in the chat.
        """
        self.name = name
        self.users = users
        self.messages = []


class Message:
    """Message class."""

    def __init__(self, user, content):
        """
        Message constructor.

        :param user: Author of the message.
        :param content: Content of the message.
        """
        self.user = user
        self.content = content
        self.reactions = 0


def write_message(user: User, chat: Chat, content: str) -> None:
    """
    Write a message to given chat.

    Create a message with given values and then add it to the chat's messages.

    :param user: Author of the message.
    :param chat: Chat to write the message to.
    :param content: Content of the message.
    """
    new_message = Message(user, content)
    chat.messages.append(new_message)


def delete_message(chat: Chat, message: Message) -> None:
    """
    Delete message from chat.

    :param chat: Chat to delete message from.
    :param message: Message to delete from chat.
    """
    if message in chat.messages:
        chat.messages.remove(message)


def get_messages_by_user(user: User, chat: Chat) -> list:
    """
    Get messages by user in chat.

    :param user: User whose messages to get.
    :param chat: Chat from where to get user's messages.
    :return: A list of messages.
    """
    messages = []
    for message in chat.messages:
        if message.user == user:
            messages.append(message)
    return messages


def react_to_last_message(chat: Chat) -> None:
    """
    Add reaction to last message in chat.

    :param chat: Chat in which the message is.
    """
    chat.messages[-1].reactions += 1


def find_most_reacted_message(chat: Chat) -> Message:
    """
    Find the most reacted message in chat.

    :param chat: Chat to get the message from.
    :return: Most reacted message.
    """
    a = 0
    for message in chat.messages:
        if message > a:
            a = message.reactions
            b = message
    return b


def count_reactions_in_chat(chat: Chat) -> int:
    """
    Count all reactions in chat.

    :param chat: Said chat.
    :return: The amount of reactions.
    """
    counter = 0
    for message in chat.messages:
        counter += message.reactions


def count_reactions_by_chat(chats: list) -> dict:
    """
    Count reactions in every chat.

    The function should return a dict where the key is the name of a chat and the value is the amount of reactions.

    :param chats: The chats in question.
    :return: A dictionary as described.
    """
    statistics = {}
    for chat in chats:
        number = count_reactions_in_chat(chat)
        statistics[chat.name] = number
    return statistics
