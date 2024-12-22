# Using supervised learning to solve minesweeper

I first encountered Minesweeper in my introductory AI class, where the challenge was to design an AI that could consistently achieve a specific success rate by the end of the quarter. While many approaches relied on deterministic rules and straightforward probability calculations to determine which cell to uncover next, I wanted to go beyond these conventional strategies.

Instead of sticking to basic probabilistic guessing, I chose to explore the potential of machine learning. This decision allowed me to tackle the problem from a unique perspective, leveraging the ability of neural networks to recognize complex patterns and make informed predictions in situations where traditional rules falter. My journey into this project opened the door to exciting possibilities for solving Minesweeper using advanced AI techniques.

## What Is Supervised Learning?

Supervised learning is a type of machine learning where a model is trained using labeled data. The data consists of input-output pairs where the model learns to map inputs to the correct outputs. For example, in this project, the input is a representation of a board state, and the output is a label indicating probabilities of mines in specific cells. The goal is for the model to generalize its learning to make accurate predictions on unseen data.

## Supervised learning typically follows these steps:

1. Dataset Preparation: Collect and preprocess data to create labeled examples.
2. Model Design: Define a model architecture suitable for the problem.
3. Training: Use the labeled data to optimize the model’s parameters.
4. Evaluation: Test the model on unseen data to measure its performance.

## Dataset Creation

To achieve this, I created a dataset of 250,000 board states. These board states were extracted from scenarios where simple game rules no longer provide clear solutions, such as:

- Situations where rules like 1-1 or 1-2-1 are required.
- Patterns that require probabilistic reasoning rather than direct logic.

The boards were generated programmatically to represent diverse and complex configurations. Each board was accompanied by a corresponding label file containing the ground truth about the presence or absence of mines in each cell.
How the Dataset Was Generated

## Board Representation:
The boards are stored in text files where each cell is encoded as:
- 0 for unopened cells.
- 1 for flagged cells.
- Numbers starting from 2 to represent the number of adjacent mines.

### Labels:
Each board has a corresponding label file that marks cells with 1 if they contain a mine and 0 otherwise.

### Scenarios:
    Scenarios were carefully designed to represent cases where decision-making involves probability or pattern recognition, ensuring the model learns from non-trivial examples.

Data Volume:
    A total of 250,000 board-label pairs were created to provide sufficient training examples for the model.

## Model Overview

The project uses a convolutional neural network (CNN) implemented in TensorFlow/Keras. The model architecture includes:

- Convolutional Layers: To detect patterns in the board, such as clusters of mines.
- Pooling Layers: To reduce spatial dimensions and focus on prominent features.
- Dense Layers: To combine extracted features for final predictions.
- Reshape Layers: To handle the input and output formats specific to the board representation.

The model was trained with the dataset, using 70% of the data for training, 20% for validation, and 10% for testing.

## Results

- The model was trained to predict the probability of mines in cells with 75% certainty.
- Evaluation metrics such as binary accuracy and loss were used to assess performance.
- Visualizations such as loss curves and heatmaps of predicted probabilities were generated to interpret results.


<table align="center">
  <tr>
    <td><img src="src/Accuracy.png" alt="Accuracy"></td>
    <td><img src="src/Loss.png" alt="Loss"></td>
  </tr>
</table>


## Heatmap Visualization

The project includes a function to visualize the model's predictions as a heatmap, showing the probability of mines in each cell. This provides an intuitive way to analyze the model’s reasoning and evaluate its effectiveness.
Conclusion

This project demonstrates how supervised learning and CNNs can tackle complex probabilistic scenarios in board games. By generating a large dataset of challenging board states, the model successfully learned to make predictions where human reasoning might struggle. This approach can be extended to other domains requiring probabilistic reasoning or advanced pattern detection.

<table align="center">
  <tr>
    <td><img src="src/Heatmap.png" alt="Accuracy"></td>
    <td><img src="src/Heatmap binary.png" alt="Loss"></td>
  </tr>
</table>

## Conclusion

The supervised learning approach to solving Minesweeper showed promising results. The model could correctly identify bomb placements in complex scenarios, as evident from the heatmap visualizations. However, its practical usability was limited. While supervised learning is effective for mapping inputs to outputs in isolated states, it falls short in capturing the full complexity of Minesweeper gameplay.

A critical limitation of this approach is the lack of an interactive agent that can make dynamic decisions while playing the game. With only 250,000 static board states, the model could not fully grasp the intricate dependencies and evolving patterns that Minesweeper demands.

To address these limitations, I implemented a Deep Q-Network (DQN) model, a reinforcement learning approach. Unlike supervised learning, DQN allows an agent to actively play the game, learn from its actions, and optimize its strategy through trial and error. This approach captures the dynamic nature of Minesweeper far better than static datasets.

You can check out the code and implementation details for my DQN model here: [Minesweeper Deep Q-Learning on GitHub](https://github.com/TanveenBal/Minesweeper-Deep-Q-Learning).

Found something wrong in my code or have questions? Feel free to contact me:
- Email: [tanveenbal@gmail.com](tanveenbal@gmail.com)
- LinkedIn: [tanveenbal](https://www.linkedin.com/in/tanveenbal/)