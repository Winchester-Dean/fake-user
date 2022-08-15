# https://github.com/Winchester-Dean
# Copyright (C) 2022  Winchester-Dean

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import random
import string

from config import FakeUserConfig

class EmailGenerator(FakeUserConfig):
    """Generate fake email address"""
    def run(self):
        name = "".join(
            random.choices(
                string.ascii_letters,
                k=15
            )
        )

        domen = [
            "mail.ru",
            "yandex.ru",
            "gmail.com",
            "inbox.ru",
            "list.ru",
            "bk.ru",
            "ya.ru",
            "yandex.com",
            "yandex.ua"
        ]

        self.console.print(
            "[bold white]Email:[/] [bold red]{}@{}[/]".format(
                name,
                random.choice(domen)
            )
        )
