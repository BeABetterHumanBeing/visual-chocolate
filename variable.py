# This file contains the specs for the smart variables that can have conditional
# constraints on each other.

class Variable(object):

	def __init__(self, amount):
		self.amount = amount
		self.constraints = []

	def get(self):
		return self.amount

	def modify(self, amount):
		self.amount += amount
		if not all([constraint.isSatisfied() for constraint in self.constraints]):
			self.amount -= amount

	def addConstraint(self, constraint):
		self.constraints.append(constraint)

class Constant(Variable):

	def modify(self, amount):
		pass  # Constants do not change.

class Constraint(object):

	def __init__(self, function, variables):
		self.function = function
		self.variables = variables

	def isSatisfied(self):
		return self.function(*self.variables)

def greaterThan(*args):
	return args[0].get() > args[1].get()

def sumToNoMoreThan(*args):
	return args[0].get() >= sum([variable.get() for variable in args[1:]])

# Returns a constraint where the variable must be greater than the given amount.
def mustBeGreaterThan(variable_hi, variable_lo):
	constraint = Constraint(greaterThan, [variable_hi, variable_lo])

	variable_hi.addConstraint(constraint)
	variable_lo.addConstraint(constraint)

def mustSumToNoMoreThan(variable_max, variable_list):
	variables = [variable_max]
	variables.extend(variable_list)

	constraint = Constraint(sumToNoMoreThan, variables)

	variable_max.addConstraint(constraint)
	for variable in variable_list:
		variable.addConstraint(constraint)