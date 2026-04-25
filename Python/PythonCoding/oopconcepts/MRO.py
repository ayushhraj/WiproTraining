#method resolution order
from oopconcepts.demoC import C
from oopconcepts.demoA import A

obj = C(10, 20, 'Hi')
A.display(self=obj)
obj.display()
obj.final()
