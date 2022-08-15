# https://github.com/Winchester-Dean
# Copyright (C) 2022  Winchester-Dean

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import datetime

from config import FakeUserConfig

class ProfileGenerator(FakeUserConfig):
    """Generate fake profile"""
    def run(self):
        profile = self.fake.profile()
        job = profile["job"]
        company = profile["company"]
        ssn = profile["ssn"]
        residence = profile["residence"]
        username = profile["username"]
        name = profile["name"]
        sex = profile["sex"]
        address = profile["address"]
        mail = profile["mail"]
        birthdate = profile["birthdate"]

        print(
            "Profile:\n"
            f"Job: {job}\n"
            f"Company: {company}\n"
            f"Ssn: {ssn}\n"
            f"Residence: {residence}\n"
            f"Username: {username}\n"
            f"Name: {name}\n"
            f"Sex: {sex}\n"
            f"Address: {address}\n"
            f"Email: {mail}\n"
            f"Date of birth: {birthdate}"
        )
