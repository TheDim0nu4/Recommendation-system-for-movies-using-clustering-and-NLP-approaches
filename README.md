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
├── README.md
├── app.py
├── requirements.txt
```

- data/ folder with raw and processed data.
- models/ folder with trained model.
- notebooks/ folder with jupyter notebooks.
- README.md provides project overview and instructions.
- app.py consol application for getting recommendations.
- requirements.txt specifies Python dependencies.



## 📊 Dataset 

The dataset used is a publicly available dataset from Kaggle called 'The Movies Dataset'. The dataset contains metadata for 45,000 movies. 
It consists of movies released on or before July 2017. Data points include title, posters, backdrops, budget, revenue, release dates, languages, description, production countries, 
and companies from movies_metadata.csv, as well as information about cast and crew from credits.csv. <br>

Source: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset 



## 🛠️ Data processing 


