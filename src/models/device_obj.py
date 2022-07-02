class Device():
    def __init__(self, name,host,port):
        self.name = name
        self.host = host
        self.port = 8080
    def get_name(self):
        return self.name
    def get_host(self):
        return self.host
    def get_port(self):
        return self.port
    
        
