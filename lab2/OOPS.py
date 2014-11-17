class Disney:
       
       def __init__(self, name, age):
              self.age=age
              self.name=name
       def married(self):
                 print self.name + "of" +str(self.age) + "is sleeping"
       def make_happy(self):
                 print self.name + "of" +str(self.age) + "is making people happy"

class princess(Disney):
       
      def __init__(self, name, age, dress_color, trait):
              Disney.__init__(self, name, age)
              self.dress_color=dress_color
              self.trait=trait 
      def ---(self):
              print "princess "+self.name+ ""
