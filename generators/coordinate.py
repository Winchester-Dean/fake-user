# https://github.com/Winchester-Dean
# Copyright (C) 2022  Winchester-Dean

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from config import FakeUserConfig


class CoordinateGenerator(FakeUserConfig):
    """Generate fake coordinate"""
    def run(self):
        self.console.print(
            "[bold white]Coordinate:[/] [bold red]{}[/]".format(
                self.fake.coordinate()
            )
        )
