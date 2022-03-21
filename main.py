
from helper import yPrint
from command_handler import CommandHandler


def main():
    commandHandler = CommandHandler()
    while True:
        userInput = None
        while userInput == None:
            print()
            yPrint("============================", True)
            yPrint("===== Playlist Manager =====", True)
            yPrint("============================", True)
            userInput = commandHandler.getUserInput()
        if userInput == 0:
            break
        commandHandler.executeUserCommand(userInput)


if __name__ == "__main__":
    main()
