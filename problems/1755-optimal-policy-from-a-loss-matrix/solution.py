import numpy as np

def expected_losses(posterior, loss):
    posterior = np.asarray(posterior, dtype=float)
    loss = np.asarray(loss,dtype=float)
    return posterior@loss

def bayes_policy(posterior, loss):
    losses = expected_losses(posterior,loss)
    return np.argmin(losses,axis=1)

# def covid_table(prevalence, sens, spec, drug_cost, qaly_young=60.0, qaly_old=10.0):
#     #posterior probability after a negative test
#     p_negative = (
#         prevalence * (1-sens)/(prevalence*(1-sens)+(1-prevalence)*spec)

#     )
#     #after a positive test
#     p_positive = (
#         prevalence*sens/(prevalence*sens+(1-prevalence)*(1-spec))
#     )
#     posterior_probs = [p_negative,p_positive]
#     qalys = [qaly_young,qaly_old]

#     rows = []
#     for test in range(2):
#         p_covid = posterior_probs[test]
#         for age in range(2):
#             qaly = qalys[age]
#             posterior = np.array([1-p_covid,p_covid])

#             loss = np.array([
#                 [0.0,drug_cost],
#                 [qaly,drug_cost]
#             ])
#             costs = expected_losses(posterior,loss)
#             action = bayes_policy(posterior,loss)[0]

#             rows.append([
#                 int(test),
#                 int(age),
#                 float(p_covid),
#                 float(costs[0, 0]),
#                 float(costs[0, 1]),
#                 int(action)

#             ])
#     return rows
def covid_table(prevalence, sens, spec, drug_cost,
                qaly_young=60.0, qaly_old=10.0):

    # Posterior probability after a negative test
    p_negative = (
        prevalence * (1 - sens)
        / (prevalence * (1 - sens) + (1 - prevalence) * spec)
    )

    # Posterior probability after a positive test
    p_positive = (
        prevalence * sens
        / (prevalence * sens + (1 - prevalence) * (1 - spec))
    )

    posterior_probs = [p_negative, p_positive]
    qalys = [qaly_young, qaly_old]

    rows = []

    for test in range(2):
        p_covid = posterior_probs[test]

        for age in range(2):
            qaly = qalys[age]

            # Expected losses for:
            # Action 0 = do nothing
            # Action 1 = give drug
            posterior = np.array([[1 - p_covid, p_covid]])

            loss = np.array([
                [0.0, drug_cost],
                [qaly, drug_cost]
            ])

            costs = expected_losses(posterior, loss)
            action = bayes_policy(posterior, loss)[0]

            rows.append([
                int(test),
                int(age),
                float(p_covid),
                float(costs[0, 0]),
                float(costs[0, 1]),
                int(action)
            ])

    return rows
