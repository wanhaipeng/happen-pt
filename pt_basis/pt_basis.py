# -*- coding: utf-8 -*-
"""learn pytorch basis."""
import os
import argparse
import torch
import torchvision
import torch.utils.model_zoo as model_zoo
from torchsummaryX import summary

def parse_args():
  """ argument parser.
  """
  parser = argparse.ArgumentParser(description="pt_basis")
  parser.add_argument('-t', '--type', type=str, required=True,
                      help="test type")
  args = parser.parse_args()
  return args

def classification_autograd():
  """ check inception_v3 graph and fix parameters.
  """
  inception_v3 = torchvision.models.inception_v3(pretrained=True).eval()
  # init input 3x224x224
  img = torch.rand(1, 3, 299, 299)
  # display inception_v3 graph info
  # print(summary(inception_v3, img))
  print("\033[32m", end="")
  for i, param in enumerate(inception_v3.parameters()):
    print("id: {} - type: {} shape: {} norm: {:.6f}".format(i, param.dtype,
        param.shape, torch.norm(param)))
  print("\033[0m", end="")

def check_vision_list():
  """ check torchvision model list.
  """
  print("\033[32m", end="")
  print("pt Classification: ")
  print("pt Detection: ")
  print("pt Segmentation: ")
  print("\033[0m", end="")

if __name__ == '__main__':
  args = parse_args()
  if args.type == "autograd":
    check_vision_list()
    print(100*'-')
    classification_autograd()
    print(100*'-')
  else:
    raise ValueError("not a valid arg: {}".format(args.type))

