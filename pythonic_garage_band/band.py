from asyncio import MultiLoopChildWatcher
from ssl import MemoryBIO
from tokenize import String



class Band ():

    instances=[]
    
    def __init__(self,name,members) -> None:
       
        self.name=name
        self.members=members
        Band.instances.append(self)
        
        
    def play_solos(self):
        
        solos_list=[]

        for i in self.members:

              solos_list.append(i.play_solo())

        return solos_list

    @classmethod   
    def to_list(self):

        return Band.instances





class Musician :

    
    

    def __init__(self,name) -> None:

        self.name=name
        self.instrument=''
        self.type=''
        
            
       
     
       

    def __str__(self):

        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
       return self.type + ' instance. Name = '+ self.name

   
   





class Guitarist(Musician):

    def __init__(self,name) -> None:
        super().__init__(name)
        self.name=name
        self.instrument='guitar'
        self.type='Guitarist'
        # Band.members.append(self)
       

    def get_instrument(self):

        return f'{self.instrument}'

    def play_solo(self):

        return "face melting guitar solo"







class Bassist(Musician):
    def __init__(self,name) -> None:
        super().__init__(name)
        self.name=name
        self.instrument='bass'
        self.type='Bassist'
        # Band.members.append(self)

    def get_instrument(self):

        return f'{self.instrument}'

    def play_solo(self):

        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self,name) -> None:
        super().__init__(name)
        self.name=name
        self.instrument='drums'
        self.type='Drummer'
        # Band.members.append(self)

    def get_instrument(self):

        return f'{self.instrument}'

    def play_solo(self):

        return "rattle boom crash"





ddd=Band('ibrahim',[Guitarist("Kurt Cobain"),
     Bassist("Krist Novoselic"),
     Drummer("Dave Grohl")])


print(ddd.play_solos()[0])