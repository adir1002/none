def print_hello(name :str,age:str) ->int:
    """
    Greets the user by name
    Parameters:
        name(str) : The name of the user
        Returns:
            str: The greeing
    """
    return 'Hello '+name+ ' ' + str(age)
    

print( print_hello("XXX", 5.988))
