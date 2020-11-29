class Title:
    def __init__(self, title, cost):
        self.title  = title
        self.cost   = cost
    def __str__(self):
        return f"-= {self.title.upper():5} =- {self.cost:3}|MDL"

##################################
t1   = Title("Programming in Python 3",600)

print(t1)