# https://github.com/Winchester-Dean
# Copyright (C) 2022  Winchester-Dean

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from faker import Faker
from rich.console import Console

launge = "ru" # ru or en

if launge == "en":
    lang_code = "en_US"
elif launge == "ru":
    lang_code = "ru_RU"
else:
    lang_code = "en_US"

class FakeUserConfig:
    console = Console()
    fake = Faker(lang_code)
