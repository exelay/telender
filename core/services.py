import asyncio
import yaml

from telethon import TelegramClient


class Sender:
    input_data: dict
    client: TelegramClient

    def __init__(self, input_file):
        self.input_file = input_file

    def send(self):
        self._parse_input_file()
        self._set_telegram_client()
        self._send_messages()

    def _parse_input_file(self):
        with open(self.input_file, 'r') as f:
            self.input_data = yaml.safe_load(f)

    def _set_telegram_client(self):         # TODO: попробовать обойти авторизацию,
        api_id = self.input_data['api_id']  #  либо складывать и искать файлы сессий в конкретной папке
        api_hash = self.input_data['api_hash']
        sender = self.input_data['sender']
        self.client = TelegramClient(sender, api_id, api_hash)
        self.client.start()

    def _send_messages(self):
        user_list = self.input_data['target_users']
        message = self.input_data['message']

        loop = asyncio.get_event_loop()
        for user in user_list:
            loop.run_until_complete(
                self.client.send_message(user, message)
            )
