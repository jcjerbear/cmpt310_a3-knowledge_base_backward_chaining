class Solution:
    def __init__(self):
        self.rulesList = list()
        self.result = False
        self.usedFlags = list()

    def solve(self):
        global goals
        self.createRules()
        self.initGoals()
        self.backwardChaining()
        self.resultOutput()

    def createRules(self):
        self.addRules()

    def addRules(self):
        rulesFile = 'data.txt'
        self.rulesList = open(rulesFile, 'r').read().split('\n')
        self.rulesList = [i.split() for i in self.rulesList]
        # print(self.rulesList)
        '''
        for rule in rulesList:
            rule = rule.split()
            print(rule)
            self.rulesDict.update({rule[0]: rule[1:]})
            print(self.rulesDict)
        '''

    def initGoals(self):
        global goals
        # print("enter initGoals")
        # use '=' instead of append here cause then it wont be list within a list
        goals = self.rulesList[0]
        print("Query:", ''.join(goals))
        print("Adding query into goals...\n")
        # print(goals)
        # delete the query line just so when we scan through the resultList while backChaining
        # it wont loop around this line
        del self.rulesList[0]
        # print(self.rulesList)

    # def appendGoals(self, subGoals):
    #     # subGoals in this case is a list
    #     print("enter appendGoals")
    #     self.goals.append(subGoals)

    def backwardChaining(self):
        global goals
        # if goals=NULL then return true
        print("goals:", ','.join(goals))
        if not goals:
            print("goal is NULL")
            print("This KB is ", end="")
            self.result = True
            return self.result

        # let a=first(goals); goals=rest(goals)
        firstGoal = goals[0]
        print("Current searching head:", firstGoal)
        goals = goals[1:]

        if goals:
            print("Rest of goals:", ','.join(goals))
        elif not goals:
            print("Rest of goals: NULL")

        # print("flag used")

        # for each r belongs to rules where head(r)=a
        for rule in self.rulesList:
            # rule in this case is each list within the rulesList
            # print(rule)
            if(rule[0] == firstGoal):
                # if the head of the rule = firstGoal
                # then we append that specific rule's body to goals
                # print(rule)
                print("Chosen rule we are looking at right now: ", end="")

                if (len(rule)==1):
                    print(''.join(rule))
                    print("Message:", ''.join(rule), "is a FACT")
                    print("Rule body: NULL")
                else:
                    print('ʌ'.join(rule[1:]), "=>", rule[0])
                    print("Rule body:", 'ʌ'.join(rule[1:]))

                print("Append these body atoms into goals...")
                # print("current goals", goals)
                # appendGoals = ''.join(rule[1:])
                # print("appendGoals", appendGoals)
                goals.append(rule[1:])
                # print("appended goals", goals)
                goals = [inner for outer in goals for inner in outer]
                # print("appended goals after join", appendGoals)
                print("goals after append:", ','.join(goals))
                print("")
                # and then we do the recursion
                if(self.backwardChaining()):
                    self.result = True
                    return self.result
                    # return True

        # else the KB is false
        self.result = False
        return self.result
        # return False

    def resultOutput(self):
        if self.result:
            print("True")
        elif not self.result:
            print("False")

goals = list()
if __name__ == '__main__':
    solution = Solution()
    solution.solve()