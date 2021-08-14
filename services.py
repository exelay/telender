import yaml


class Sender:
    mailing_data: dict

    def __init__(self, input_file):
        self.input_file = input_file

    def send(self):
        self._get_mailing_data()

    def _get_mailing_data(self):
        with open(self.input_file, 'r') as f:
            self.mailing_data = yaml.safe_load(f)

