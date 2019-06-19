#! /usr/bin/env python

import argparse
import os
import numpy as np
import json
from voc import parse_voc_annotation

train_ints, train_labels = parse_voc_annotation("/home/shchang/scratch/cvpr/data/ann/voc/", "/home/shchang/scratch/cvpr/data/img/", 'test', [])
labels=list(train_labels.keys())

with open('/home/shchang/scratch/cvpr/keras-yolo3/config_voc.temp.json') as config_buffer:    
        config = json.loads(config_buffer.read())
        config['model']['labels']=labels

with open('/home/shchang/scratch/cvpr/keras-yolo3/config.json', 'w') as outfile:
     json.dump(config, outfile)                               
