

import matplotlib.pyplot as plt


# define the data
prog_languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity_scores = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# find the index of the language with the highest popularity score
highest_score_index = popularity_scores.index(max(popularity_scores))

# create the explode list
explode_list = [0] * len(prog_languages)
explode_list[highest_score_index] = 0.1

# create the pie chart with the explode parameter and set the startangle
plt.pie(popularity_scores, labels=prog_languages, explode=explode_list, autopct='%1.1f%%', startangle=140)

# set the title
plt.title("Popularity of Programming Languages")

# show the plot
plt.show() 