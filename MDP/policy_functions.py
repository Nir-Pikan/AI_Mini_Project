GAMMA = 0.2
MAX_K = 1000


# run up to max_k iterations to gain a policy for an MDP
def policy_iteration(states, actions, probability, reward):
    """
    :param list states: set of states
    :param list actions: set of actions
    :param function probability: transition function
    :param function reward: reward function
    """
    values = {s: 0 for s in states}
    policy = {s: actions[0] for s in states}
    k = 0

    while k < MAX_K:
        old_policy = policy.copy()
        old_values = values.copy()
        values, policy = policy_evaluation_v3(states, actions, probability, reward)
        # values = policy_evaluation_v2(policy, states, probability, reward)
        # policy = policy_improvement_v2(values, states, actions, probability, reward)

        print(f"Iteration {k}:\n")
        print(f"old_values: {old_values}\n")
        print(f"new_values: {values}\n")
        print(f"old_policy: {old_policy}\n")
        print(f"new_policy: {policy}\n")
        k += 1

        if all(old_policy[s] == policy[s] for s in states):
            break
        # if all(round(old_values[s]) == round(values[s]) for s in states):
        #     break

    return policy


# # evaluate the MDP and current policy to gain new values
# def policy_evaluation(policy, states, probability, reward):
#     values = {s: 0 for s in states}
#
#     while True:
#         old_value = values.copy()
#
#         for s in states:
#             if s != "END":
#                 a = policy[s]
#                 values[s] = reward(s, a) + sum(probability(s, a, s_next) * GAMMA * old_value[s_next]
#                                                for s_next in states)
#
#         if all(old_value[s] == values[s] for s in states):
#             break
#
#     return values
#
#
# # use new values to gain a new policy for the MDP
# def policy_improvement(values, states, actions, probability, reward):
#     policy = {s: actions[0] for s in states}
#
#     for s in states:
#         if s != "END":
#             Q = {}
#             for a in actions:
#                 Q[a] = reward(s, a) + sum(probability(s, a, s_next) * values[s_next] for s_next in states)
#
#             policy[s] = max(Q, key=Q.get)
#
#     return policy


# less redundancy by checking only possible next states
def policy_evaluation_v2(policy, states, probability, reward):
    values = {s: 0 for s in states}
    k = 0

    while k < MAX_K:
        old_value = values.copy()

        for s in states:
            if s != "END":
                next_states = ["END"]
                if s != "Q10":
                    temp = int(s.replace("Q", "")) + 1
                    next_states.append("Q"+str(temp))

                a = policy[s]
                values[s] = round(sum(probability(s, a, s_next) * (reward(s, a) + GAMMA * values[s_next])
                                      for s_next in next_states), 3)

        k += 1
        print(f"{old_value} \n{values}\n======")
        if all(old_value[s] == values[s] for s in states):
            break

    return values


# less redundancy by checking only possible next states
def policy_improvement_v2(values, states, actions, probability, reward):
    policy = {s: actions[0] for s in states}

    for s in states:
        if s != "END":
            next_states = ["END"]
            if s != "Q10":
                temp = int(s.replace("Q", "")) + 1
                next_states.append("Q" + str(temp))

            Q = {}
            for a in actions:
                Q[a] = round(sum(probability(s, a, s_next) * (reward(s, a) + GAMMA * values[s_next])
                                 for s_next in next_states), 3)

            policy[s] = max(Q, key=Q.get)

    return policy


def policy_evaluation_v3(states, actions, probability, reward):
    values = {s: 0 for s in states}
    policy = {s: actions[0] for s in states}
    k = 0

    while k < MAX_K:
        old_value = values.copy()

        for s in states:
            if s != "END":
                next_states = ["END"]
                if s != "Q10":
                    temp = int(s.replace("Q", "")) + 1
                    next_states.append("Q"+str(temp))

                Q = {}
                for a in actions:
                    Q[a] = round(sum(probability(s, a, s_next) * (reward(s, a) + GAMMA * values[s_next])
                                          for s_next in next_states), 3)

                values[s] = Q[max(Q, key=Q.get)]
                policy[s] = max(Q, key=Q.get)

        k += 1
        print(f"{old_value} \n{values}\n======")
        if all(old_value[s] == values[s] for s in states):
            break

    return values, policy


# # less redundancy by checking only possible next states
# def policy_improvement_v3(values, states, actions, probability, reward):
#     policy = {s: actions[0] for s in states}
#
#     for s in states:
#         if s != "END":
#             next_states = ["END"]
#             if s != "Q10":
#                 temp = int(s.replace("Q", "")) + 1
#                 next_states.append("Q" + str(temp))
#
#             Q = {}
#             for a in actions:
#                 Q[a] = round(sum(probability(s, a, s_next) * (reward(s, a) + GAMMA * values[s_next])
#                                  for s_next in next_states), 3)
#
#             policy[s] = max(Q, key=Q.get)
#
#     return policy