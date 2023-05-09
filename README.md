# xray_age
- Predict biological age from frontal CXR image.

## supported file type
- jpeg
- png

## usage
- Download pre-trained model
  - https://riken-share.box.com/s/zezm7z4o8dq2palzsfkxzabtluov54b4

```python
python predict.py path_to_cxr_image
```
## requirements
- Python3 (3.8.5)
- Pytorch (1.4.0)
- Torchvision (0.5.0)
- Fastai (1.0.61)

## Citation
Please cite this paper

- Ieki, H., Ito, K., et al. "Deep learning-based age estimation from chest X-rays indicates cardiovascular prognosis." *Communications Medicine* **2**, 159 (2022). https://doi.org/10.1038/s43856-022-00220-6
