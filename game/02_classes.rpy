# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


init python:
    import datetime, time, os, random, webbrowser
    
    # Obtiene el nombre real del usuario de Windows/PC (Opcional, pero bueno tenerlo a mano)
    pc_user = os.environ.get('USERNAME', 'USER')

    class SearchInputValue(VariableInputValue):
        def __init__(self, variable, action):
            super(SearchInputValue, self).__init__(variable)
            self.action = action
        def enter(self):
            renpy.run(self.action)
            renpy.restart_interaction()

    class CmdInputValue(VariableInputValue):
        def __init__(self, variable, action):
            super(CmdInputValue, self).__init__(variable)
            self.action = action
        def enter(self):
            renpy.run(self.action)
            renpy.restart_interaction()

    class Email:
        def __init__(self, sender, subject, body, mission_id=None, correct_answer=None, options=None):
            self.sender = sender
            self.subject = subject
            self.body = body
            self.mission_id = mission_id
            self.correct_answer = correct_answer
            self.options = options
            self.is_read = False
            self.is_replied = False