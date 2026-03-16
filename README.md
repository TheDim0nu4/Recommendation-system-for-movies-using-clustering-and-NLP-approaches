# 🎬 Recommendation-system-for-movies-using-clustering-and-NLP-approaches 

The project focuses on creating a content-based recommendation system for movies. 
The project includes cleaning, analyzing and preparing data about films using NLP approaches like tokenization, stemming, vectorization in order to create clusters. 
For creating recommendations, a console application was made where a user can enter a film that he likes and then get recommendations based on that film.



## 📁 Project Structure

```
Recommendation-system-for-movies-using-clustering-and-NLP-approaches/
│
├── data/
│ ├── raw_data/
│ │ ├── credits.csv
│ │ ├── movies_metadata.csv
│ ├── cluster_labels.csv
│ ├── preprocessed_data.csv
│
├── models/
│ ├── kmeans_model.joblib
│
├── notebooks/
│ ├── data.ipynb
│ ├── modeling.ipynb
│
├── .gitattributes
├── README.md
├── app.py
├── requirements.txt
```

- data/ folder with raw and processed data.
- models/ folder with trained model.
- notebooks/ folder with jupyter notebooks.
- .gitattributes configures Git LFS to store the large dataset file credits.csv used in the project.
- README.md provides project overview and instructions.
- app.py consol application for getting recommendations.
- requirements.txt specifies Python dependencies.



## 📊 Dataset 

The dataset used is a publicly available dataset from Kaggle called 'The Movies Dataset'. The dataset contains metadata for 45,000 movies. 
It consists of movies released on or before July 2017. Data points include title, posters, backdrops, budget, revenue, release dates, languages, description, production countries, 
and companies from movies_metadata.csv, as well as information about cast and crew from credits.csv. <br>

Source: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset 



## 🛠️ Data processing 

Before creating clusters, we need to explore and preprocess our data. <br>

It includes: <br>
1. Basic exploration and preprocessing (check and clean data) <br>
2. Text data preprocessing (tokenization, removing stop words, stemming) <br>
3. Analysis of the data (histograms, bar plots, scatter plots) <br>
4. Vectorization of the data (TfidfVectorizer and CountVectorizer) <br>
5. Reduction of dimensionality (PCA) <br>
6. Saving the preprocessed data <br>

Code and explanation are available in data.ipynb.



## 🤖 Modeling 

In this step, we are going to apply a clustering algorithm on our preprocessed data. In this project, we used one of the most common algorithms — KMeans, 
because it needs only one parameter and works well with large data. <br>

It includes: <br>
1. Getting the optimal number of clusters (elbow method and silhouette score) <br>
2. Training the model with the optimal k <br>
3. Exploring and visualizing the clusters (bar plot, UMAP) <br>
4. Saving the model and necessary data for the recommendation system <br>

Code and explanation are available in modeling.ipynb.



## ⭐ Creating recommendations

The recommendation system works as follows: the user enters a movie they like (this can be done using the console application app.py). 
Then the cluster of this movie is found, along with other movies that belong to the same cluster. 
After that, based on Euclidean distance, the movies closest to the user’s movie in this cluster are selected.



## 🛠️ Tools Used

- Python (Pandas, Numpy, nltk, Matplotlib, Scikit-learn, UMAP, Joblib)
- Jupyter Notebook



## ⚡ Installation

1. Clone the repository: <br>

   `git clone https://github.com/TheDim0nu4/Recommendation-system-for-movies-using-clustering-and-NLP-approaches.git` <br>
   `cd Recommendation-system-for-movies-using-clustering-and-NLP-approaches` <br>


   
## 🧠 Running Jupyter Notebooks (Conda)

1. Create a Conda environment: <br>

   `conda create -n movie_rec_env python=3.11` <br>

2. Activate the environment: <br>

   `conda activate movie_rec_env` <br>

3. Install project dependencies: <br>

   `python -m pip install -r requirements.txt` <br>

4. Select the environment kernel in Jupyter: <br>

   - Open the notebooks and select the kernel corresponding to the created Conda environment (movie_rec_env).
   - After selecting the kernel, you can run the notebook cells and start working with the project.



## ▶️ Running Console Application

- `python app.py`



## ✍️ Author

The project was carried out by Dmytro Skrypchenko.




