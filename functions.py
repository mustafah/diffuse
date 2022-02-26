import random


def adapt_seed(params):
    seed = params.seed
    if seed is None:
        random.seed()
        seed = random.randint(0, 2**32)
    else:
        seed = int(seed)

    params.seed = seed

    if params.verbose:
        print(f'Using seed: {seed}')