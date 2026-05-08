import pygame
from datetime import datetime
from .base import State
from db.db import GameDatabase
from sprites.ui import Label, Button

class Load(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.database = GameDatabase()
        self.save_file_list = self.database.list_saves()
        self.file_number = 0

        self.labels = self.create_labels()
        self.selected_file = self.labels[self.file_number]

        self.load_button = Button(640, 425, 200, 50, "LOAD", pygame.Color('white'), pygame.Color('whitesmoke'), pygame.Color('black'), pygame.font.Font(None, 30), True)
        self.previous_button = Button(510, 425, 50, 50, "<", pygame.Color('white'), pygame.Color('whitesmoke'), pygame.Color('black'), pygame.font.Font(None, 30), True)
        self.next_button = Button(770, 425, 50, 50, ">", pygame.Color('white'), pygame.Color('whitesmoke'), pygame.Color('black'), pygame.font.Font(None, 30), True)



        self.ui_elements = [
            self.selected_file,
            self.load_button,
            self.previous_button,
            self.next_button
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.previous_button.rect.collidepoint(event.pos):
                    self.previous()
                elif self.next_button.rect.collidepoint(event.pos):
                    self.next()
                print(self.selected_file, flush=True)

    def create_labels(self):
        labels = []

        for file in self.save_file_list:
            time = datetime.fromisoformat(file['last_played_at'])
            time_str = time.strftime('%B %d, %Y at %I:%M %p')
            label = Label(640, 350, f"ID: {str(file['id'])}, Last played at: {time_str}", pygame.font.Font(None, 30), pygame.Color('white'))
            labels.append(label)

        return labels
    
    def previous(self):
        self.file_number = (self.file_number + 1) % len(self.save_file_list)

        self.selected_file = self.labels[self.file_number]

        self.ui_elements[0] = self.selected_file

    def next(self):
        self.file_number = (self.file_number - 1) % len(self.save_file_list)

        self.selected_file = self.labels[self.file_number]

        self.ui_elements[0] = self.selected_file