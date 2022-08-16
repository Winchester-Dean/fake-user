# https://github.com/Winchester-Dean
# Copyright (C) 2022  Winchester-Dean

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import os
import inspect

from typing import List, Callable, Awaitable, Union
from importlib import import_module
from rich.console import Console
from logo import logo

console = Console()

class Main:
    def __init__(
        self,
        directory: str = "generators"
    ):
        self.all_generators: List[Union[Callable, Awaitable]] = []
        
        for file in os.listdir(directory):
            if file.endswith(".py"):
                file = file[:-3]

                generators = import_module(
                    f"{directory}.{file}"
                )

                for classname, classobj in inspect.getmembers(
                    generators,
                    inspect.isclass
                ):
                    if classname.endswith("Generator"):
                        self.all_generators.append((
                            classobj(),
                            classobj.__doc__
                        ))
    
    def run(self):
        for index, module in enumerate(
            self.all_generators
        ):
            instance, doc = module

            console.print(
                "\t\t[bold white]{index}.[/] [bold green]{doc}.[/]".format(
                    index = index + 1,
                    doc = doc
                )
            )

        print()

        while True:
            try:
                while True:
                    choice = console.input(
                        "[bold white]>> [/]"
                    )
                    if choice.isdigit():
                        choice = int(choice) - 1
                        break

                instance = self.all_generators[choice][0]
                instance.run()
            except IndexError as error:
                console.print(
                    "[bold white]Error:[/] [red]{}[/]".format(
                        error
                    )
                )
                exit()
            except ValueError as error:
                console.print(
                    "[bold white]Error:[/] [red]{}[/]".format(
                        error
                    )
                )
                exit()
            except KeyboardInterrupt:
                exit("Bye !")

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    logo()

    console.print("""
[bold magenta]Copyright (C) 2022  https://github.com/Winchester-Dean/fake-user
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.[/]
""")

    Main().run()
