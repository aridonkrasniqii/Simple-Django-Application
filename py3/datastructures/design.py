class Connect:

    def __init__(self, hostname):
        self.hostname = hostname

    def __enter__(self):
        print(f'Trying to connect to a server: {self.hostname}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Updates finished! Restarting {self.hostname} ...')


