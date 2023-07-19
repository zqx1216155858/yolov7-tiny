#!/data/users/CHDHPC/2022124001/software/anaconda3/bin/python3
import torch
print(torch.cuda.is_available()) # 检查 cuda 是否可用
print(torch.cuda.device_count()) # 检查可用的 gpu 数量
print(torch.version.cuda) # 查看 cuda 版本

# 下边的代码就是返回服务器上 GPU 的占用情况，这样方便我们选择 GPU 或者节点
import subprocess
ret = subprocess.run('nvidia-smi', shell=True, capture_output=True, timeout=100)
print(ret.stdout.decode('utf8'))