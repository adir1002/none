from pip._vendor.colorama import init, Fore

def func(msg,is_warning=False): 
    if(is_warning):
        print('ERRERRERRERRERERERERERE')
    print(msg)



def display(msg,is_warning=False):
    if is_warning:
        print(Fore.LIGHTMAGENTA_EX+ msg)
    else:
        print(Fore.LIGHTRED_EX+msg+Fore.CYAN+'AAAA')
    print(Fore.BLUE+'LOL')


