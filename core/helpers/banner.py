from __version__ import __version__, __tagline__, __author__, __contact__, __codename__


def print_banner():

    print('''


██████╗ ██████╗  ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
██║  ██║██████╔╝██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
██║  ██║██╔══██╗██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
██████╔╝██║  ██║╚██████╔╝██║     ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                 

                        %s

                             Version: %s
                            Codename: %s
                              Author: %s
                             Contact: %s

''' % (__tagline__, __version__, __codename__, __author__, __contact__))