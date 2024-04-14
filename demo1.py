import torch
from torchviz import make_dot

model = torch.nn.Transformer(nhead=4, num_encoder_layers=6, num_decoder_layers=6)
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

out = model(src, tgt)

make_dot(out.sum(), params=dict(model.named_parameters()))