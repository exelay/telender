from cleo import Application
from run_command import RunCommand

application = Application()
application.add(RunCommand())

if __name__ == "__main__":
    application.run()
