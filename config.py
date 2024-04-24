class Config:
    input_method = "keyboard"

    def change_input_method(self):
        if self.input_method == "keyboard":
            self.input_method = "microphone"
        else:
            self.input_method = "keyboard"
        return self.input_method