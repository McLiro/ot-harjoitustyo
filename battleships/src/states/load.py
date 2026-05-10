from datetime import datetime
import pygame
from db.db import GameDatabase
from sprites.ui import Label, Button
from .base import State
from .game import Game

class Load(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.database = GameDatabase()
        self.save_file_list = self.database.list_saves()
        self.file_number = 0

        self.labels = self.create_labels()
        self.selected_file = self.labels[self.file_number]

        self.load_button = Button(640, 425, 200, 50, "LOAD", pygame.Color('white'),
                                    pygame.Color('whitesmoke'), pygame.Color('black'),
                                    pygame.font.Font(None, 30), True)

        self.previous_button = Button(510, 425, 50, 50, "<", pygame.Color('white'),
                                    pygame.Color('whitesmoke'), pygame.Color('black'),
                                    pygame.font.Font(None, 30), True)

        self.next_button = Button(770, 425, 50, 50, ">", pygame.Color('white'),
                                    pygame.Color('whitesmoke'), pygame.Color('black'),
                                    pygame.font.Font(None, 30), True)

        self.delete_button = Button(640, 485, 100, 50, "DELETE", pygame.Color('red'),
                                    pygame.Color('red2'), pygame.Color('white'),
                                    pygame.font.Font(None, 30), True)

        self.ui_elements = [self.selected_file,
                            self.load_button,
                            self.previous_button,
                            self.next_button,
                            self.delete_button]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.load_button.rect.collidepoint(event.pos):
                    file = self.save_file_list[self.file_number]
                    file_id = file['id']
                    self.next_state = Game(self.game, save_file_id=file_id)
                    self.done = True
                elif self.previous_button.rect.collidepoint(event.pos):
                    self.previous()
                elif self.next_button.rect.collidepoint(event.pos):
                    self.next()
                elif self.delete_button.rect.collidepoint(event.pos):
                    self.delete()

    def create_labels(self):
        labels = []

        for file in self.save_file_list:
            time = datetime.fromisoformat(file['last_played_at'])
            time_str = time.strftime('%B %d, %Y at %I:%M %p')
            label = Label(640, 350, f"ID: {str(file['id'])}, Last played at: {time_str}",
                            pygame.font.Font(None, 30), pygame.Color('white'))
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

    def delete(self):
        file = self.save_file_list[self.file_number]
        file_id = file['id']
        self.database.delete(file_id)

        self.save_file_list = self.database.list_saves()
        self.labels = self.create_labels()

        if len(self.save_file_list) == 0:
            from .menu import Menu
            self.next_state = Menu(self.game)
            self.done = True
            return

        self.file_number -= 1
        self.selected_file = self.labels[self.file_number]
        self.ui_elements[0] = self.selected_file
