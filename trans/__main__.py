# trans/__main__.py

from trans import cli, __app_name__

def main() :
    cli.App(prog_name=__app_name__)

if __name__ == "__main__" : main()