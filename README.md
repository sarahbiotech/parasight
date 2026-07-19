# Parasight AI: Parasite Egg Detection Using YOLOv8

## Overview
Parasight AI is a computer vision application designed to automatically detect and classify parasite eggs from microscopic images using a trained **YOLOv8 object detection model**.

The application analyzes microscopy images, identifies parasite eggs, displays detection results, and provides confidence scores and parasite counts.

> ⚠️ This system is developed for research and educational purposes. It is not a replacement for professional laboratory diagnosis.

## Features
- Upload microscopic images for automated analysis.
- Detect parasite eggs using YOLOv8.
- Display detected objects with bounding boxes.
- Provide confidence scores for each detection.
- Count detected parasite types.
- Adjustable confidence threshold for predictions.

## Supported Parasites
The model supports detection of 8 parasite classes:

- Ancylostoma spp.
- Ascaris lumbricoides
- Enterobius vermicularis
- Fasciola hepatica
- Hymenolepis
- Schistosoma
- Taenia spp.
- Trichuris trichiura

## Technologies Used
- Python
- Streamlit
- YOLOv8 (Ultralytics)
- PIL
- NumPy

## Model Information

**Framework:** YOLOv8  
**Task:** Object Detection  
**Dataset Classes:** 8  
**Validation Images:** 168  

## Model Performance

| Metric | Value |
|---|---|
| Precision | 81.1% |
| Recall | 71.1% |
| mAP50 | 80.4% |
| mAP50-95 | 64.5% |

### Class Performance Highlights

| Parasite | Precision | mAP50 |
|---|---|---|
| Ancylostoma spp. | 83.5% | 85.3% |
| Ascaris lumbricoides | 85.4% | 91.4% |
| Enterobius vermicularis | 71.0% | 76.7% |
| Fasciola hepatica | 78.7% | 53.4% |
| Hymenolepis | 77.3% | 84.0% |
| Schistosoma | 86.9% | 71.6% |
| Taenia spp. | 78.8% | 85.1% |
| Trichuris trichiura | 87.4% | 96.1% |

## Workflow
1. User uploads a microscopic image.
2. The YOLOv8 model processes the image.
3. Parasite eggs are detected and classified.
4. Bounding boxes and confidence scores are displayed.
5. The application generates a parasite detection summary.

## Installation

Install required libraries:

```bash
pip install streamlit ultralytics pillow
