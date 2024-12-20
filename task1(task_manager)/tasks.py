class Task:
  def __init__(self, ID: int, desc: str, deadline: str, priority: int):

    assert ID >= 0
    self.ID = ID
    self.desc = desc
    self.deadline = deadline
    self.priority = priority

  def taskParser(self):
    descComponents =  ()
    descStr = ""
    commasReached = 0
    for i in range(len(self.desc)):
      
      if self.desc[i] != ',':
        descStr+=self.desc[i]
      else:
        descComponents+=(descStr,)
        commasReached+=1
        descStr=""
    descComponents+=(descStr,)
    return descComponents



    



  