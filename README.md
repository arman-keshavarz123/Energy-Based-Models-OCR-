# Energy-Based Models for OCR

A project implementing energy-based models for transcribing variable-length words from images using structured prediction techniques.

## Overview

This project tackles the challenging problem of transcribing text from images where words have different lengths. The solution uses energy-based models with a sliding window CNN architecture and dynamic programming for optimal character-to-position alignment.

## Key Features

- **Variable-length text recognition** from images
- **Energy-based model framework** for structured prediction
- **Sliding window CNN architecture** that processes images of arbitrary width
- **Viterbi algorithm** for finding optimal character alignment paths
- **Custom loss functions** incorporating cross-entropy energies and path optimization

## Technical Approach

- **Model Architecture**: 6-layer CNN with batch normalization and ReLU activations
- **Training Strategy**: Pre-training on single characters, then multi-character training with energy-based loss
- **Energy Framework**: Uses energy functions `E(x, y, z) = C(z) + Σ l_i[z(i)]` and free energy optimization
- **Dynamic Programming**: Viterbi algorithm for finding best character-to-position alignments

## Results

- **Single character accuracy**: 100%
- **Multi-character transcription**: Successfully transcribed "hello"
- **Energy optimization**: Achieved significant reduction in free energy during training
