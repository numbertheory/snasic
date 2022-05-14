#!/usr/bin/env python3
from snasic.config import Config

args = Config("arguments.yaml")
print(args.filename)
