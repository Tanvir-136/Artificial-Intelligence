from collections import deque

class Statement:
    def __init__(self, subject, predicate, singular=True):
        self.subject = subject
        self.predicate = predicate
        self.singular = singular

class Relation:
    def __init__(self):
        self.map = {}

    def add(self, key, subject, predicate, singular=True):
        self.map[key] = Statement(subject, predicate, singular)

    def print_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is", st.predicate, end="")
        else:
            print(st.subject, "are", st.predicate, end="")

    def print_neg_statement(self, key):
        st = self.map[key]
        if st.singular:
            print(st.subject, "is not", st.predicate, end="")
        else:
            print(st.subject, "are not", st.predicate, end="")

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

class RelationLogic(Relation):
    def __init__(self):
        super().__init__()
        self.operand_val = {}

    def map_operands(self, op, val):
        self.operand_val[op] = val

    # Single operation evaluation
    def eval_op(self, a, b, op):
        if op == '!':
            return 0 if a == 1 else 1
        elif op == '&':
            return 1 if a == 1 and b == 1 else 0
        elif op == '|':
            return 1 if a == 1 or b == 1 else 0
        elif op == '~':  # implies
            return 0 if a == 1 and b == 0 else 1
        elif op == '*':  # iff
            return 1 if (a == b) else 0

    # Evaluate full expression (left to right, no precedence)
    def evaluate_expression(self, exp):
        exp = exp.replace(" ", "").replace(",", "")
        operators = deque()
        operands = deque()
        negative = False

        for ch in exp:
            if ch in ['&', '|', '~', '*']:
                operators.append(ch)
            elif ch == '!':
                negative = True
            else:
                val = self.operand_val[ch]
                if negative:
                    val = self.eval_op(val, 0, '!')
                    negative = False
                operands.append(val)

        # Evaluate left to right
        while operators:
            op = operators.popleft()
            a = operands.popleft()
            b = operands.popleft()
            result = self.eval_op(a, b, op)
            operands.appendleft(result)

        return operands.popleft()

# -----------------------
# Example usage
# -----------------------
relation = RelationLogic()
relation.add("a", "sensei", "student")
relation.add("b", "sensei", "brilliant")

relation.map_operands("a", 1)
relation.map_operands("b", 0)

result = relation.evaluate_expression("a | b & !a ~ b")
print("Result:", result)