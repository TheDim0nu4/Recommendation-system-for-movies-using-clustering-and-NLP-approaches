import pandas as pd
import numpy as np




def get_recommendations(film_title, num_of_rec, data):

    neces_data = data[data['cluster'] == data[data['title'] == film_title]['cluster'].iloc[0]].copy()

    film_vector = neces_data[neces_data['title'] == film_title].iloc[:, 2:].values[0]
    neces_data['distance'] = np.sqrt(np.sum((film_vector - neces_data.iloc[:, 2:].values) ** 2, axis=1))

    neces_data.sort_values(by='distance', inplace=True)
    recommendations = neces_data['title'].values[1:num_of_rec + 1]


    return recommendations




def main():

    print("🎥✨ Welcome to the *Movie Recommendation System!* ✨🎥")
    print("------------------------------------------------------")
    print("Based on movie overviews and clustering, we’ll find films similar to your choice.\n")


    films_clusters = pd.read_csv('./data/cluster_labels.csv')
    vectors_overvies = pd.read_csv('./data/preprocessed_data.csv')
    data = pd.concat([films_clusters, vectors_overvies.drop(columns=['title'])], axis=1)
    data.drop(columns=['overview'], inplace=True)


    film_title = input('🎬 Enter the name of a film you like: ').strip()
    while film_title not in data['title'].values:
        print('❌ Sorry, this film is not in our database. Please try another one!')
        film_title = input('🎬 Enter another film title: ').strip()

    num_of_rec = int(input('🔢 How many similar films would you like (1–100)? '))
    while num_of_rec < 1 or num_of_rec > 100:
        print("⚠️ Please enter a number between 1 and 100.")
        num_of_rec = int(input('🔢 How many similar films would you like (1–100)? '))

    print("\n🔍 Finding movies similar to your choice... Please wait 🎞️\n")
    recommendations = get_recommendations(film_title, num_of_rec, data)


    print("🍿 Your personalized movie recommendations 🍿")
    print("=============================================")
    for i, film in enumerate(recommendations, 1):
        print(f" {i}. {film}")
    print("=============================================")
    print("\n💡 Enjoy your movie marathon! 🎬🔥")

    input()




if __name__ == '__main__':
    main()

