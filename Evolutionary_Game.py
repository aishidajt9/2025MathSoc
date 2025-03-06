#%%
import matplotlib.pyplot as plt
import random
import statistics as st

#%%
def replicator(x, y): #1: left. 0: right
    if x == 1 and y == 1:
        return [1, 1]
    elif x == 0 and y == 0:
        return [0]
    else:
        return []

#%%
# initial values
initial_prop = 0.3
num_ants = 1000
num_L = int(initial_prop * num_ants // 1)
# creating initial ants
ants = [1 for i in range(num_L)]
ants.extend([0 for i in range(num_ants - num_L)])

prop_hist = [st.mean(ants)]

#%%
for t in range(20):
    # random shuffling ants
    random.shuffle(ants)
    # if number of ants is odd number, then replicate the last one
    if len(ants) % 2 == 1:
        ants.append(ants[-1])
    # gaming with the ant in the next door
    reps = []
    for i in range(0, len(ants), 2):
        reps.extend(replicator(ants[i], ants[i + 1]))
    ants.extend(reps)
    prop = st.mean(ants)
    prop_hist.append(prop)
    # creating next ants by updated prop
    num_L = int(prop * num_ants // 1)
    ants = [1 for i in range(num_L)]
    ants.extend([0 for i in range(num_ants - num_L)])


# %%
plt.plot(prop_hist)
plt.show();

# %%
# initial values
prop_hists = []
for i in range(1, 10, 1):
    initial_prop = i/10
    num_ants = 1000
    num_L = int(initial_prop * num_ants // 1)
    # creating initial ants
    ants = [1 for i in range(num_L)]
    ants.extend([0 for i in range(num_ants - num_L)])

    prop_hist = [st.mean(ants)]

    for t in range(30):
        # random shuffling ants
        random.shuffle(ants)
        # if number of ants is odd number, then replicate the last one
        if len(ants) % 2 == 1:
            ants.append(ants[-1])
        # gaming with the ant in the next door
        reps = []
        for i in range(0, len(ants), 2):
            reps.extend(replicator(ants[i], ants[i + 1]))
        ants.extend(reps)
        prop = st.mean(ants)
        prop_hist.append(prop)
        # creating next ants by updated prop
        num_L = int(prop * num_ants // 1)
        ants = [1 for i in range(num_L)]
        ants.extend([0 for i in range(num_ants - num_L)])
    prop_hists.append(prop_hist)

#%%
for prop_hist in prop_hists:
    plt.plot(prop_hist)
plt.show();

# %%
