import click



from cliente.commands import commands as clients_commands


CLIENTS_TABLE='.clients.csv'
@click.group()
@click.pass_contex
def cli():
    ctx.obj ={}
    ctx.obj['clients_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)
if __name__=='__main__':
    print('conexion')