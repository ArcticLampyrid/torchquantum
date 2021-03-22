import numpy as np
import torch.nn as nn


class ArchSampler(object):
    def __init__(self, model: nn.Module):
        self.model = model
        self.arch_space = model.arch_space

    def get_uniform_sample_arch(self):
        sample_arch = []
        for layer_arch_space in self.arch_space:
            layer_arch = np.random.choice(layer_arch_space)
            sample_arch.append(layer_arch)

        return sample_arch

    def get_named_sample_arch(self, name):
        sample_arch = []
        if name == 'smallest':
            for layer_arch_space in self.arch_space:
                layer_arch = layer_arch_space[0]
                sample_arch.append(layer_arch)
        elif name == 'largest':
            for layer_arch_space in self.arch_space:
                layer_arch = layer_arch_space[-1]
                sample_arch.append(layer_arch)
        elif name == 'middle':
            for layer_arch_space in self.arch_space:
                layer_arch = layer_arch_space[len(layer_arch_space) // 2]
                sample_arch.append(layer_arch)
        else:
            raise NotImplementedError(name)
        return sample_arch
