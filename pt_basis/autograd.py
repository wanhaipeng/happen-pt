# -*- coding: utf-8 -*-
"""learn pytorch basis."""

import os
import argparse
import torch
import torchvision

def parse_args():
  """ argument parser.
  """
  parser = argparse.ArgumentParser(description="pt_basis")
  parser.add_argument('-t', '--type', type=str, required=True,
                      help="test type")
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  args = parse_args()

