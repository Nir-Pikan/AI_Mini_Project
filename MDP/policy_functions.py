GAMMA = 1
MAX_K = 100


# gain a policy for an MDP
def get_policy(states, actions, probability, reward):
    """
    :param list states: set of states
    :param list actions: set of actions
    :param function probability: transition function
    :param function reward: reward function
    """
    values, policy = policy_evaluation(states, actions, probability, reward)

    return policy


# evaluate the MDP using up to MAX_K iterations to calculate values and policy
def policy_evaluation(states, actions, probability, reward):
    values = {s: 0 for s in states}
    policy = {s: actions[0] for s in states}
    k = 0

    while k < MAX_K:
        old_value = values.copy()
        old_policy = policy.copy()

        for s in states:
            if s != "END":
                next_states = ["END"]
                if s != "Q10":
                    temp = int(s.replace("Q", "")) + 1
                    next_states.append("Q" + str(temp))

                Q = {}
                for a in actions:
                    temp_sum = 0
                    for next_s in next_states:
                        temp_sum += probability(s, a, next_s) * (reward(s, a, next_s) + GAMMA * values[next_s])
                        if s == "Q10" and a == "play" and next_s == "END":
                            temp_sum += (1. - probability(s, a, next_s)) * reward(s, a, "Q10_LOSE")

                    Q[a] = round(temp_sum, 3)

                values[s] = Q[max(Q, key=Q.get)]
                policy[s] = max(Q, key=Q.get)
            else:
                policy[s] = None

        k += 1

        # print for each iteration
        print(f"\nIteration {k}:\n")
        print(f"old_values: {old_value}\n")
        print(f"new_values: {values}\n")
        print(f"old_policy: {old_policy}\n")
        print(f"new_policy: {policy}\n")
        if all(old_value[s] == values[s] for s in states):
            break

    return values, policy
