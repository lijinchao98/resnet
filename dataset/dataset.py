import torch
from torch.utils.data import Dataset
import numpy as np
import random


class train_Loader(Dataset):

    def __init__(self, curve, label):
        self.all_curve = (np.load(curve)).astype(float)
        self.label = (np.load(label)).astype(float)

    def __getitem__(self, index):
        # 根据index读取pixel的光谱曲线
        pixel_curve = torch.tensor(self.all_curve[index, :])
        label = torch.tensor(self.label[index])

        return pixel_curve, label

    def __len__(self):
        # 返回训练集大小
        return len(self.all_curve)

class test_Loader(Dataset):

    def __init__(self, curve):
        self.all_curve = (np.load(curve)).astype(float)

    def __getitem__(self, index):
        # 根据index读取pixel的光谱曲线
        pixel_curve = torch.tensor(self.all_curve[index, :])

        return pixel_curve

    def __len__(self):
        # 返回训练集大小
        return len(self.all_curve)


if __name__ == "__main__":

    HSI_dataset = test_Loader(r'D:\ZPEAR\gitclone\SUTDF\data\Actual_data\train_data\train_data.npy',
                         r'D:\ZPEAR\gitclone\SUTDF\data\Actual_data\train_data\train_label.npy')

    print("数据个数：", len(HSI_dataset))
    train_loader = torch.utils.data.DataLoader(dataset=HSI_dataset,
                                               batch_size=50,
                                               shuffle=False)
    batch_size = 50
    for pixel_curve, label in train_loader:
        print(pixel_curve.reshape(batch_size, 1, -1).shape)
        print(pixel_curve)
        print(label)
        break
