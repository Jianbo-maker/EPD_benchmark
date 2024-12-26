# EPD-Bench
## Embodied Image Quality Assessment for Robotic Intelligence

COMING SOON
...

Embodied Image Quality Assessment for Robotic Intelligence

![Fig2](https://github.com/user-attachments/assets/9a530bfe-8968-4bd0-bce5-8544100bd7d9)

CMC-Bench: A Benchmark for Visual Signal Compression Using Large Multimodal Models
<img src="https://via.placeholder.com/150" /> <!-- 占位符图片，实际使用时请替换为真实Logo -->

Description
CMC-Bench is a comprehensive benchmark designed to evaluate the performance of large multimodal models (LMMs) in visual signal compression. By leveraging the conversion between multiple modalities, CMC-Bench aims to achieve high compression rates while maintaining good perception quality. This benchmark provides a platform for researchers to compare different LMMs and identify areas for further optimization.

Key Features
Dataset: Curated a high-quality dataset of 1,000 images without compression distortion, including 400 NSIs, 300 SCIs, and 300 AIGIs.
Model Evaluation: Evaluates models across four working modes: Text mode, Pixel mode, Image mode, and Full mode.
Performance Metrics: Measures consistency between distorted and reference images, as well as the perception quality of distorted images.
Leaderboard: Displays the performance of various I2T and T2I models in a radar map and table format.
Installation
To use CMC-Bench, you need to follow these steps:

Clone the repository from GitHub:
bash
git clone https://github.com/your-username/CMC-Bench.git
Navigate to the project directory:
bash
cd CMC-Bench
Ensure you have the necessary dependencies installed. The specific dependencies will be listed in the requirements.txt file.
Usage
To use CMC-Bench, you can follow these general steps:

Prepare your LMMs for evaluation.
Run the evaluation scripts provided in the repository.
Analyze the results using the provided leaderboard and performance metrics.
Examples
Model	Consistency Score	Perception Quality Score
GPT-40 (I2T)	90	85
DIBIR (T2I)	85	90 (Image/Full mode)
RealVis	88	88

Note: The above table is a simplified example. The actual leaderboard in CMC-Bench will provide more detailed and comprehensive results.

References
CMC-Bench Paper
GitHub Repository
Hugging Face Data Release
License
CMC-Bench is licensed under the MIT License. See the LICENSE file for more details.

This README provides a brief overview of CMC-Bench. For more detailed information, please refer to the project's GitHub repository and the associated paper.
