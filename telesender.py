from cleo import Application
from core.run_command import RunCommand

application = Application()
application.add(RunCommand())

if __name__ == "__main__":
    application.run()
