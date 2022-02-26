import gc
import torch
import functions as fn
from types import SimpleNamespace

params = {
    'seed': None,
    # Else
    'verbose': True
}

params = SimpleNamespace(**params)
fn.adapt_seed(params)

gc.collect()
torch.cuda.empty_cache()
