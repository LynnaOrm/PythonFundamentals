class Call(object):

    def __init__(self, identity, name, phonenumber, time, reason):

        self.id = identity

        self.name = name

        self.phonenumber = phonenumber

        self.time = time

        self.reason = reason

    

    def display(Call):

        print "Caller ID:" +str(self.identity)

        print "caller Name:" +str (self.name)

        print "Caller Number:" +str(self.phonenumber)

        print "Time of call:" +str(self.time)

        print "Call Reason:" +str(self.reason)

    

class Callcenter(Call):

    def __init__(self):

        self.Calls = []

        self.queue = 0



    def addcall(self, Call):

        self.Call.append(Call)

        self.queue += 1

        return self

    

    def removecall(Call):

        self.queue -= 1

        del self.Call[0]

        return self



    def callinfo(Call):

        for i in self.Call:

            i.display()

        return self

    

Timcalls = Call(123456, 'Tim', 6433470, '9:22', 'late video rental')

Jared = Call(7894556, 'Jared', 9425732, '9:29', 'food')

callcenterinfo = Callcenter().addcall(Timcalls).addcall(Jared).callinfo()