# -*- coding: utf-8 -*-
import sys
import argparse
import torch.nn as nn
import math
import torch.utils.model_zoo as model_zoo
import torch
import torch.nn.functional as F
from torchsummaryX import summary
from tensorboardX import SummaryWriter
sys.path.append('..')
from net import EfficientNet

def parse_args():
  """ argument parser
  """
  parser = argparse.ArgumentParser(description="test efficientnet")
  parser.add_argument('-n', "--name", type=str, default="efficientnet-b0", help="efficient version")
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  args = parse_args()
  input_shape = EfficientNet.get_image_size(args.name)
  images = torch.rand(1, 3, input_shape, input_shape).cuda(device=1)
  model = EfficientNet.from_pretrained(args.name)
  model = model.cuda(device=1)
  print(summary(model, images))
  print(model(images).cpu().detach().numpy().shape)
  with SummaryWriter(logdir="./efficientnet_graph", comment=args.name) as w:
    w.add_graph(model, (images,))
