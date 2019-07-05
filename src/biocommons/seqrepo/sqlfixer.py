
sql_parameter = '%s'

def S_(input):
    output = input.replace("?", sql_parameter)
    return output
