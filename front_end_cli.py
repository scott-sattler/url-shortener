
class Commands:
    cmd_help = 'help'
    cmd_exit = 'exit'


def output(arg: str):
    print(arg)


# f"{'\n'}" requires Python 12
help_txt = 'Commands:\n\t' + \
           '\n\t'.join([attr for attr in dir(Commands) if attr[0] != '_'])
no_cmd = "Command unrecognized."


c = Commands
user_input = None
while True:
    usr_inp = input('> ').lower().lstrip().rstrip()

    match usr_inp:
        case c.cmd_exit:
            break
        case c.cmd_help:
            output(help_txt)

        case _:
            output(no_cmd)
