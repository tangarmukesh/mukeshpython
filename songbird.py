class Songbird:
    def __init__(self,namearg,songarg):
        self.name = namearg
        self.song = songarg
        print(self.name,"is born" )

    def sing(self):
        print(self.name,'sing',self.song)

    def __del__(self):
        print(self.name,"Flew away")
