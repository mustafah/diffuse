import functions as fn

from types import SimpleNamespace

params = SimpleNamespace(**{
    'seed': None,
    # Else
    'verbose': True
})

fn.clean_caches(params)
fn.adapt_seed(params)

