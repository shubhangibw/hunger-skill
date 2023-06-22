from mycroft import MycroftSkill, intent_file_handler


class Hunger(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hunger.intent')
    def handle_hunger(self, message):
        self.speak_dialog('hunger')


def create_skill():
    return Hunger()

