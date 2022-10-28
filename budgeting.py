class Category:
  def __init__ (self, category):
    self.category = category
    self.ledger = []
    
  def __str__ (self):
      title = f"{self.category:*^30}\n"
      items = ""
      total = 0
      for led in self.ledger:
          items += f"{led['description'][:23]:23}" + f"{led['amount']:>7.2f}" 
          total += led['amount']
      out = title + items + "Total: " + str(total)
      return out
  
  def deposit(self, amount, description = ""):
     self.ledger.append({"amount": amount, "description":     
     description})
    

  def withdraw(self, amount, description = ""):
      if self.check_funds(amount) >= 0:
        self.leger.append({"amount": -1 * amount, 
        "description": description})
        self.check_funds -= amount
        return True
      else:
        return False

  def get_balance(self):
      balance = 0.0
      for i in self.leger:
        balance = i["amount"]
      return balance

  def transfer(self, amount, bud_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + bud_category.category)
            bud_category.deposit(amount, "Transfer from " + self.category)
            return True
        return False

  def check_funds(self, amount):
        if self.get_balance >= amount:
            return True
        return False
          
