import os
from yaml import safe_load
from win10toast import ToastNotifier


class EmailSwitch:
    def __init__(self):
        with open("config.yml") as config:
            self.emails = safe_load(config)
        self.toaster = ToastNotifier()

    def switch(self):
        stream = os.popen("git config user.email")
        current_email = stream.read().strip()
        if current_email == self.emails[0]:
            os.popen(f"git config --global user.email {self.emails[1]}")
            self.toaster.show_toast(
                "Git Email Switch", f"Git email is now {self.emails[1]}"
            )
        else:
            os.popen(f"git config --global user.email {self.emails[0]}")
            self.toaster.show_toast(
                "Git Email Switch", f"Git email is now {self.emails[0]}"
            )


if __name__ == "__main__":
    email_switch = EmailSwitch()
    email_switch.switch()
