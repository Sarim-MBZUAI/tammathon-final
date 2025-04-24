# ArcFace Training Instructions

To train the model using the cat configuration:

```bash
CUDA_VISIBLE_DEVICES=0 python3 src/train_arcface.py src/configs/cat.py --output outputs/cat/arcface
```

This command uses GPU 0 and saves output to the specified directory.