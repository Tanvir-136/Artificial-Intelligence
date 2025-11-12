from itertools import product 

class Statement:
    def __init__(self, subject, predicate, singular=True):
        self.subject = subject
        self.predicate = predicate
        self.singular = singular

class Relation:
    def __init__(self):
        self.map = {}

    # Add a statement
    def add(self, key, subject, predicate, singular=True):
        self.map[key] = Statement(subject, predicate, singular)

    # Print normal statement
    def print_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is", st.predicate, end="")
        else:
            print(st.subject, "are", st.predicate, end="")

    # Print negated statement
    def print_neg_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is not", st.predicate, end="")
        else:
            print(st.subject, "are not", st.predicate, end="")

    # Build natural language from logic formula
    def build_statement(self, logic):
        logic = logic.replace(" ", "").replace(",", "")
        neg = False
        only_sub = False

        for i in range(len(logic)):
            if logic[i] == '!':
                neg = True
            elif logic[i] == '&':
                print(" and ", end="")
            elif logic[i] == '|':
                print(" or ", end="")
            elif logic[i] == '*':
                print(" if and only if ", end="")
            elif logic[i] == '~':
                print(" implies ", end="")
            elif logic[i] == 'A':
                print("For all ", end=""); only_sub = True
            elif logic[i] == 'E':
                print("For some ", end=""); only_sub = True
            elif logic[i] in ['(', ')']:
                continue
            else:
                if only_sub:
                    print(self.map[logic[i]].subject, end=""); only_sub = False
                elif neg:
                    self.print_neg_statement(logic[i]); neg = False
                else:
                    self.print_statement(logic[i])
        print('.')

    # Truth table function      
    def truth_table(self, expr):
        print("P | Q | output \n ----------")
        for P, Q in product([0,1], repeat=2):
            print(P, Q ,"|", int (expr(P, Q)))

# -----------------------------
# Example usage
# -----------------------------

r = Relation()
r.add("s", "students", "brilliant", singular=False)
r.add("a", "Tanvir", "student")
r.add("b", "Tanvir", "lazy")

r.add("c", "It", "raining")
r.add("d", "Road", "wet")

r.build_statement("c ~ d")   # "It is raining implies Road is wet."
r.build_statement("a & !b")  # "Tanvir is student and Tanvir is not lazy."

# Truth table example using lambda
expr = lambda c, d: (not c) or d    
expr1 = lambda a: not a
r.truth_table(expr)

# # AND
# AND = lambda P, Q: P and Q

# # OR
# OR = lambda P, Q: P or Q

# # NOT
# NOT = lambda P: not P

# # IMPLIES (P → Q)
# IMPLIES = lambda P, Q: (not P) or Q

# # BICONDITIONAL (P ↔ Q)
# IFF = lambda P, Q: P == Q


# or shortcut method
from itertools import product


P_text="tanvir is student"
Q_text="tanvir is hard working"

# 1st sentence
w1=P_text.split()
p1=" ".join(w1[:2])
p2=" ".join(w1[2:])

# 2nd sentence
w2 = Q_text.split()
q1 = " ".join(w2[:2])
q2 = " ".join(w2[2:])

s = p1 + " " + p2 + " and " + q2

print(s)
def truth_table(expr):
    print("P Q | R")
    for P, Q in product([0,1], repeat=2):
        print(P, Q, "|", int(expr(P, Q)))

expr = lambda P, Q: (not P) or Q #implies that
truth_table(expr)
