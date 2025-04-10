# PBPnet

[![PyPI Downloads](https://static.pepy.tech/badge/bpnet-lite)](https://pepy.tech/projects/bpnet-lite)

> IMPORTANT: PBPNet is a personal implementation of the original [bpnet-lite](https://github.com/jmschrei/bpnet-lite) by Jacob Schreiber, which in turn is a lightweigth implementation in PyTorch of the original [BPNet](https://github.com/kundajelab/bpnet). Where i've adapted code from others it's properly cited at the top of the corresponding file. PBPNet stands for Polycomb BPNet.

Polycomb BPNet (PBPNet) is a lightweight modification of [BPNet](https://github.com/kundajelab/bpnet). It builds on top of the original [bpnet-lite](https://github.com/jmschrei/bpnet-lite) adding features like a test and validation PyTorch DataLoader (adatped from [Adam He](https://github.com/adamyhe/PersonalBPNet)), concurrent model training and single task metrics.
### Installation

You can install PBPNet with:
```
git clone git@github.com:AndreaMariani-AM/PBPNet.git
cd PBPNet
pip install -e .
```
