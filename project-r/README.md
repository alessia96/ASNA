This script is used to analyse users' interactions within Reddit's "Feminism" and "Domestic Violence" subreddits. 
The document is organized into sections that include loading necessary libraries, data preprocessing, data exploration, network analysis, and conclusions. 
Here's a summary of each section:
- Abstract: Provides a brief overview of the study's focus, methods, and findings, highlighting the analysis of user dynamics and sentiment patterns in anonymous Reddit discourse.
- Load Necessary Libraries: Checks and loads essential libraries required for the analysis, such as 'tidyverse', 'cowplot', 'sna', and 'igraph'.
- Load Data and Preprocess: Reads preprocessed data from CSV files, filters data related to the selected subreddits, and organizes data subsets for analysis.
- Data Exploration: Summarizes sentiment and emotion distributions across different datasets, including full data, posts, comments, and subreddits. Visualizes these distributions using bar plots.
- Analysis: Initiates analyses by calculating degree centralities of positions in the networks formed by users' comments and posts. Computes the degree of centrality and analyzes the connected users.
- Graph: Generates a network graph of commenters and post authors, depicting relationships between users based on their interactions.
- Conclusions: Summarizes the study's findings and implications, emphasizing that interconnectivity between subreddits is not substantial, though a prevalent negative sentiment suggests candid engagement with authentic information.

Overall, this document combines data analysis, visualization, and network analysis to gain insights into the dynamics of Reddit discussions related to feminism and domestic violence. It seeks to understand sentiment patterns, user connectivity, and how topics are interrelated in the context of anonymous online discourse.
