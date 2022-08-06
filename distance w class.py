class distance:
  def getdata(self):
    print("Enter first distance: ")
    self.ft1 = input("feet: ")
    self.inch1 = input("inches : ")
    print("\nEnter second distance: ")
    self.ft2 = input("feet: ")
    self.inch2 = input("inches: ")

  def adddata(self):
    self.addft = int(self.ft1) + int(self.ft2)
    self.addin = int(self.inch1) + int(self.inch2)
    if(self.addin >= 12):
      self.addft = self.addft + 1
      self.addin = self.addin - 12

  def putdata(self):
    print("\nAddition of distances: " + str(self.addft) + " feet and " + str(self.addin) + " inch")
  
ob = distance()
ob.getdata()
ob.adddata()
ob.putdata()



'''

HOW I DID : 

class distance:
    def getdata(self):
        a = input("Enter first distance in Feet :")
        b = input("Enter first distance in Inch :")
        c = input("Enter Second distance in Feet :")
        d = input("Enter Second distance in Inch :")

        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)

    def addition(self): 
        addft = (sum (self.a + self.c))
        addin = (sum (self.b + self.d))
        if(addin>12):
            addft += 1
            addin -= 12

    def putdata(self):
        print(f"Addition of Distance: {self.addft} feet {self.addin} inch")

long = distance()
long.getdata()
long.addition()
long.putdata()             

'''