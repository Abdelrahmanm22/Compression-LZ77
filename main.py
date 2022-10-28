#Created by abdelrahman Mohamed Ramadan
#Computer Science Department
#Faculty of Computers and Artificial Intelligence Cairo University

class Tag:
  def __init__(self, Position, Length,NextSympol):
    self.Position = Position
    self.Length = Length
    self.NextSympol=NextSympol

  def printTag(self):
      print("<",self.Position,",",self.Length,",",self.NextSympol,">")




SlidingWindow = "ABAABABAABBBBBBBBBBBBA"
SearchWindow = ""
x=""
list = []
z=0
for i in SlidingWindow:
    x+=i
    Pos=len(SearchWindow)-SearchWindow.find(x)
    # print(Pos,len(x)-1)
    if SearchWindow.find(x) > -1 :
        z=Pos
    else:
        list.append( Tag(z,len(x)-1,i))

        SearchWindow+=x;
        x=""

for obj in list:
    print( obj.printTag())

