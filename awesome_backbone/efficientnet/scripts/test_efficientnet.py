""" test efficientnet accuracy in imagenet-val.
"""

import os
import sys
import torch
import torchvision
import time
import tqdm
import argparse
import numpy as np
from PIL import Image
sys.path.append('..')
from net import EfficientNet

def eval_classify(net, preprocessor):
  """ do classification evaluation

  Parameters
  ----------
  net : torch.Module
    pytorch network
  preprocessor : torchvision.transforms.Compose
    image preprocessoss
  """
  data_path = '/home/haipeng.wan/work/evaluation/data/imagenet-val/image'
  base_path = 'result'
  batch = 1
  if not os.path.exists(base_path):
    os.makedirs(base_path)
  result_path = '{}/{}.txt'.format(base_path, args.name)
  if os.path.exists(result_path):
    os.remove(result_path)
  resultList = []
  with open(result_path, 'w') as f:
    _img_ids = range(1,50001) # imagenet id start from 1
    img_ids_len = len(_img_ids) // batch
    img_ids = (_img_ids[i:i+batch] for i in range(0, len(_img_ids), batch))
    for ids in tqdm.tqdm(img_ids, total=img_ids_len):
      img_path_list = ['{}/ILSVRC2012_val_{:0>8d}.JPEG'.format(data_path,i)
                       for i in list(ids)]
      img = Image.open(img_path_list[0]).convert("RGB")
      input_data = preprocessor(img).unsqueeze(0).cuda(device=0)
      with torch.no_grad():
        # output_data = net(input_data).cpu().detach().numpy()
        output = net(input_data)
      # result = [i for i in np.argsort(-output_data)[:,:5].tolist()]
      result = [torch.topk(output, k=5).indices.squeeze(0).tolist()]
      resultStr = [' '.join(map(str, i)) for i in result]
      resultList += resultStr
    f.write('\n'.join(resultList))


def make_efficientnet():
  """ Constructs a efficientnet.

  efficientnet-b0
  efficientnet-b1
  efficientnet-b2
  efficientnet-b3
  efficientnet-b4
  efficientnet-b5
  efficientnet-b6
  efficientnet-b7
  """
  print("Construct {}".format(args.name))
  model_group = ['efficientnet-b0', 'efficientnet-b1',
                 'efficientnet-b2', 'efficientnet-b3',
                 'efficientnet-b4', 'efficientnet-b5',
                 'efficientnet-b6', 'efficientnet-b7']
  if args.name in model_group:
    model = EfficientNet.from_pretrained(args.name)
    return model
  else:
    raise ValueError("Not a valid name: {}!".format(args.name))

def make_preprocessor(input_size, process_type = 'cls'):
  """ Constructs a preprocessor

  Parameters
  ----------
  input_size : int
    network input resolution
  process_type : str
    network type
  """
  if process_type == "cls":
    normalize = torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                 std=[0.229, 0.224, 0.225])
    processor = torchvision.transforms.Compose([
      torchvision.transforms.Resize(input_size),
      torchvision.transforms.CenterCrop(input_size),
      torchvision.transforms.ToTensor(),
      normalize,])
    return processor
  else:
    raise ValueError("Not a valid type: {}".format(process_type))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="test efficientnet accuracy")
  parser.add_argument('-n', '--name', help='network name', required=True, default="")
  parser.add_argument('-m', '--mode', help='run mode', default="test")
  args = parser.parse_args()
  if args.mode == "test":
    net = make_efficientnet().cuda(device=0).eval()
    input_size = EfficientNet.get_image_size(args.name)
    print("\033[32m" + "input resolution: {}".format(input_size) + "\33[0m")
    preprocessor = make_preprocessor(input_size)
    # do classification
    eval_cls_begin = time.time()
    eval_classify(net, preprocessor)
    eval_cls_end = time.time()
    print("\033[32m" + 40*"#" + "\033[0m")
    print("evaluation cost time: - {:.6f}".format(eval_cls_end - eval_cls_begin))
    print("\033[32m" + 40*"#" + "\033[0m")
  elif args.mode == "eval":
    with open("/home/haipeng.wan/work/evaluation/data/imagenet-val/ground_truth.txt",'r') as f:
      groundtruth = f.readlines()
    with open("../result/{}.txt".format(args.name), 'r') as f:
      result = f.readlines()
    top1, top5 = 0, 0
    for i in range(50000):
      truth = groundtruth[i].strip()
      line = result[i].strip().split(' ')
      if truth in line:
          top5 += 1
      if truth == line[0]:
          top1 += 1
    print("\033[32m" + 40*'='+ "\033[0m")
    print('top5 hit num {} acc: {}'.format(top5, top5/50000.0))
    print('top1 hit num {} acc: {}'.format(top1, top1/50000.0))
    print("\033[32m" + 40*'='+ "\033[0m")
  else:
    raise ValueError("not a valid mode: {}".format(args.mode))
