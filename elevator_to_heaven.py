# Elevator simulation with custom button order

BUTTONS = [
    'f','l','a','g','{','f','1','a','5','h','d','r','i','v','i','n','g',
    '_','t','h','3','_','w','0','r','l','d','}'
]

class Elevator:
    def __init__(self, buttons):
        self.buttons = buttons
        self.current = None

    def press_button(self, button):
        if button in self.buttons:
            self.current = button
            print(f"Elevator now at '{button}' floor/button.")
        else:
            print(f"Button '{button}' does not exist.")

    def display_buttons(self):
        print("Available buttons in order:")
        print(" | ".join(self.buttons))

def main():
    elevator = Elevator(BUTTONS)
    elevator.display_buttons()
    print("Type the button to press, or 'exit' to quit.")
    while True:
        choice = input("Press button: ")
        if choice == "exit":
            break
        elevator.press_button(choice)

if __name__ == "__main__":
    main()