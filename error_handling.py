from discord.ext import commands

errors={
    "CommandNotFound" : "Command Not Found",
    "MissingRequiredArgument" : "Please pass in all the arguments"
}

def get_error(error):
    
    if isinstance(error, commands.CommandNotFound):
        er="Command Not Found"
    elif isinstance(error, commands.MissingRequiredArgument):
        er="Please pass in all the arguments"
    else:
        er=error
    
    return er
