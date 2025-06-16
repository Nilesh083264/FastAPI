from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, data): pass


class AddCommand(Command):
    def execute(self, data):
        print("Added", data)


class DeleteCommand(Command):
    def execute(self, data):
        print("Deleted", data)


class UpdateCommand(Command):
    def execute(self, data):
        print("Update", data)


class CommandFactory:
    @staticmethod
    def get_command(action: str) -> Command | None:
        commands = {
            "/add": AddCommand(),
            "/delete": DeleteCommand(),
            "/update": UpdateCommand(),
        }
        return commands.get(action, None)
