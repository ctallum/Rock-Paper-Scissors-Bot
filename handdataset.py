from __future__ import print_function, division
import os
import torch
import pandas as pd
import imageio
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

class HandDataset(Dataset):
    "Hand position dataset for a game of Rock Paper Scissors"

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.dataset = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        # get image
        img_name = os.path.join(self.root_dir,
                                self.dataset.iloc[idx, 0])
        image = imageio.imread(img_name)
        # get classification
        classification = self.dataset.iloc[idx, 1:]

        sample = {'image': image, 'classification': classification}

        if self.transform:
            sample['image'] = self.transform(sample['image'])

        return sample
