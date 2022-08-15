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

class DateOfBirthGenerator:
    """Generate fake date of birth"""
    def run(self):
        print(
            "Date of birth: {}.{}.{}".format(
                random.randint(1980, 2000),
                random.randint(1, 12),
                random.randint(1, 30)
            )
        )
