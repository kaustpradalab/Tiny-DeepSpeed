# Copyright (c) 2024 liangyuwang
# Licensed under the Apache License, Version 2.0


import torch
import torch.nn as nn
import triton.language as tl


class Parameter(nn.Parameter):
    def __new__(cls, data=None, requires_grad=True, requires_dist=True):
        t = nn.Parameter.__new__(cls, data, requires_grad)
        t.requires_dist = requires_dist
        return t


def to_tl_type(ty):
    return getattr(tl, str(ty).split(".")[-1])

supported_acc_dtypes = {
    torch.float16: (torch.float32, torch.float16), torch.bfloat16: (torch.float32, torch.bfloat16),
    torch.float32: (torch.float32, ), torch.int8: (torch.int32, )
}
