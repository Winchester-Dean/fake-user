from rich.console import Console

console = Console()

def logo():
    console.print("""[bold white]
          __       _
         / _| __ _| | _____       _   _ ___  ___ _ __
        | |_ / _` | |/ / _ \_____| | | / __|/ _ \ '__|
        |  _| (_| |   <  __/_____| |_| \__ \  __/ |
        |_|  \__,_|_|\_\___|      \__,_|___/\___|_|
[/]""")
