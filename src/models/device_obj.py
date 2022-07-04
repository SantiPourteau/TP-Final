class Device():
    def __init__(self, name,host,port):
        """
        Class for the Device the computer will connect to
        
        args:
            - name
            - host: IP address or host
            - port
        """
        self.name = name
        self.host = host
        self.port = port

    def get_name(self):
        return self.name

    def get_host(self):
        return self.host
        
    def get_port(self):
        return self.port
    
        
