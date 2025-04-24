# 🚀 TAMM Hackathon 2025 – AI Challenge Repository

This repository contains the code and resources for our submission to the **TAMM Hackathon 2025**, where we tackled **three real-world AI problems** using deep learning and computer vision.

---

## 🧠 Overview of Tasks

### 🔹 Task 1: Pet Face Recognition (PetFaceNet)
We built a **pet facial recognition system** capable of identifying pets from images using a metric-learning approach. Our solution uses a **ResNet-50 backbone**, **ArcFace loss**, and **Nearest Class Mean** for inference. This approach is designed to be scalable and adaptable to new pets with minimal retraining.

**Highlights:**
- Backbone: Modified ResNet-50
- Loss: ArcFace
- Distance Metric: Cosine similarity
- Top-3 Accuracy: **82%**
- Inference Time: ~3 minutes

> 🔗 GitHub: [mapooon/PetFace](https://github.com/mapooon/PetFace?tab=readme-ov-file)  
> 🔗 GitHub: [deepinsight/insightface](https://github.com/deepinsight/insightface)

---

### 🔹 Task 2: ICAO Photo Compliance Classification
We developed a binary classification model to identify whether a face photo complies with **ICAO passport standards**, addressing issues such as head alignment, lighting, and background uniformity.

**Highlights:**
- Model: ResNet-50 with class-weighted binary cross-entropy loss
- Data Augmentation: Horizontal flips
- Training Epochs: 20
- Imbalance Ratio: 1 (compliant) : 21 (non-compliant)
- Evaluation Metric: **F1-Score**

---

### 🔹 Task 3: Vehicle Damage Captioning
This challenge focused on generating **natural language descriptions of vehicle damage** from images. We used a multimodal architecture combining image feature extraction and a text generation transformer.

**Highlights:**
- Feature Extractor: ResNet-based CNN
- Caption Generator: Transformer (few-shot inspired prompting)
- Evaluation Metric: **METEOR Score**
- Sample Output: _"Car image with dent and broken lamp."_

---

## 📊 Evaluation Metrics

| Task | Metric         | Description                                     |
|------|----------------|-------------------------------------------------|
| 1    | Top-3 Accuracy | Correct within 3 predictions                    |
| 2    | F1-Score       | Balances precision and recall for imbalanced classes |
| 3    | METEOR Score   | Measures quality of generated captions         |

---

## 📚 References

1. [PetFace: A Benchmark for Fine-grained Pet Face Recognition](https://arxiv.org/abs/2407.13555)  
2. [PetFace GitHub Repository](https://github.com/mapooon/PetFace?tab=readme-ov-file)  
3. [InsightFace GitHub Repository](https://github.com/deepinsight/insightface)  
4. [Deep Residual Learning for Image Recognition (ResNet)](https://arxiv.org/abs/1512.03385)  
5. [ChatGPT (GPT-4) by OpenAI](https://openai.com/research/gpt-4)  

---

## 👥 Team Members
- **Sarim Hashmi**  
- **Muhammad Umer Sheikh**  
- **Abdelrahman**  
- **Alaa**

---

## 📄 License
This project is open-sourced under the MIT License.
