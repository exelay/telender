from cleo import Command

from services import Sender


class RunCommand(Command):
    """
    Start messaging to telegram users from user list.

    run
        {input-file? : Path to the input *.yaml file}
    """
    default_input_file = 'input.yaml'

    def handle(self):
        input_file = self.argument('input-file')
        if not input_file:
            input_file = self.default_input_file
        sender = Sender(input_file)
        sender.send()
