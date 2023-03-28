# Import spyce and type (python -m spacy download en_core_web_md) to instal the model
# Open the movies.txt file in reading mode to iterate through the file
# Use the nlp model with the film despription
# Create an empty dictionary to store the similarity scores obtained during the iterations
# Use a for lop to iterate through the lines and apply the nlp model to each line 
# add the values obtained calculating the similarity into the empty dictionary
# Sort the similarities stored in the dictionary 
# Use a for loop with the enumerate function to disllay the movies in order
 
import spacy 

def watch_next(film_description):

    nlp = spacy.load('en_core_web_md')

    with open ("movies.txt" , "r+" , encoding= "UTF-8") as read_file:

        lines = read_file.readlines()

        model_sentence = nlp(film_description)

        similarity_scores = {}

        for line in lines:

            sentence = line.strip("\n")
            doc = nlp(sentence)
            similarity_scores[sentence] = round(model_sentence.similarity(doc),3)
        
        sorted_movies = sorted(similarity_scores.items(), key=lambda x: x[1], reverse= True)

        print("The order you should watch the movies based your previous searches is the following: \n")

        for movie,i in enumerate(sorted_movies, start=1):
            print(movie,i,"\n")
   

planet_hulk_description = "Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where hi is sold into slavery and trained as a gladiator"
watch_next(planet_hulk_description)
    



