from typing import Tuple
import torch
from .llm import LLM

import os, glob
from huggingface_hub import snapshot_download
import numpy as np

class Gpt4All(LLM):
    def __init__(self, name, use_cache=True):
        super().__init__(name)
        self.use_cache = use_cache
        