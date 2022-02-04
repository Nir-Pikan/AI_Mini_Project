
def policy_iteration(states, actions, probability, reward):
    """
    :param list states: set of states
    :param list actions: set of actions
    :param function probability: transition function
    :param function reward: reward function
    """
    policy = {s: actions[0] for s in states}

    while True:
        old_policy = policy.copy()
        values = policy_evaluation(policy, states, probability, reward)
        policy = policy_improvement(values, states, actions, probability, reward)

        if all(old_policy[states] == policy[s] for s in states):
            break

        return policy


def policy_evaluation(policy, states, probability, reward):
    values = {s: 0 for s in states}

    while True:
        old_value = values.copy()

        for s in states:
            a = policy[s]
            values[s] = reward(s, a) + sum(probability(s, a, s_next) * old_value[s_next] for s_next in states)

        if all(old_value[s] == values[s] for s in states):
            break

    return values


def policy_improvement(values, states, actions, probability, reward):
    policy = {s: actions[0] for s in states}

    for s in states:
        Q = {}
        for a in actions:
            Q[a] = reward(s, a) + sum(probability(s, a, s_next) * values[s_next] for s_next in states)

        policy[s] = max(Q, key=Q.get)

    return policy
