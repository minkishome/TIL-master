# '''
# POP
# DUP
# +
# -
#
# '''
#
# def solution(S):
#     list_word = ['POP', 'DUP', '+', '-']
#     words = S.split()
#     list_ans = []
#     for word in words:
#         if word == 'POP':
#             try:
#                 list_ans.pop()
#             except IndexError:
#                 return -1
#         elif word == 'DUP':
#             try:
#                 list_ans.append(list_ans[-1])
#             except IndexError:
#                 return -1
#         elif word == '+':
#             try:
#                 a = list_ans.pop()
#                 b = list_ans.pop()
#                 list_ans.append(a+b)
#             except IndexError:
#                 return -1
#         elif word == '-':
#             try:
#                 a = list_ans.pop()
#                 b = list_ans.pop()
#                 list_ans.append(a - b)
#             except IndexError:
#                 return -1
#         else: #숫자일때
#             list_ans.append(int(word))
#
#     return list_ans[-1]
#
# # s = "13 DUP 4 POP 5 DUP + DUP + -"
# s = 'DUP 5 6'
# print(solution(s))
# # error 발생시 return -1


# from typing import List, Text
#
#
# class NoAgentFoundException(Exception):
#     pass
#
#
# class Agent(object):
#     def __str__(self):
#         return "<Agent: {}>".format(self._name)
#
#
# class Ticket(object):
#     pass
#
#
# class FinderPolicy(object):
#     def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
#         raise NotImplemented
#
#     def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
#         raise NotImplemented
#
#
# class LeastLoadedAgent(FinderPolicy):
#     def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
#         raise NotImplemented
#
#
# class LeastFlexibleAgent(FinderPolicy):
#     def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
#         raise NotImplemented




from typing import List, Text


class NoAgentFoundException:
    pass


class Agent:
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)

class Ticket:
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions



class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:

        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:


        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        name = ''
        low_loads = 9999999
        for agent in agents:
            if agent.load < low_loads:
                low_loads = agent.load
                name = agent.name
        if name =='':
            return NoAgentFoundException()
        return name


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        need = ticket.restrictions[0]
        flexi = 99999
        print(need)
        for agent in agents:
            print(agent.skills)
            if need in agent.skills:
                if len(agent.skills) > flexi:
                    flexi = len(agent.skills)
                    name = agent.name
        if flexi == 99999:
            return NoAgentFoundException()

        return name
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
print(least_loaded_policy.find(ticket, [agent1, agent2]))

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
print(least_flexible_policy.find(ticket, [agent1, agent2]))


