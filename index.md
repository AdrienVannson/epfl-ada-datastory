---
layout: post
title: "Behind the Scenes of Stardom: Decoding the Patterns in Actors' Careers"
permalink: /
---

How do you envision your career? We, as scientists, will probably spend a substantial portion of our career in the same company in a specific field, like pharma, robotics or data science for the most talented of us. For actors, the journey is more complex, involving potential shifts between diverse movie genres and marked by the inevitable highs and lows inherent to the profession. In our project, we aim at analyzing the trajectory of acting careers. 

Usually, when you seek information about someone's career, you turn to LinkedIn. Would you do the same to stalk your childhood actor crush? Well, good news, we are here to do it for you. From the number of connections (actors they have collaborated with), to the potential genre specialization in movies, and not forgetting the prospect of winning an Oscar, let’s delve into the intricacies of our actors’ careers. 

# Career Characterization

Let's kick off our journey into the fascinating world behind the scenes of stardom with an assessment of our beloved actors' career trajectories. To navigate this cinematic maze, we will need a clever approach to construct and compare their careers. Here's the plan: For each actor, we'll craft their profile sequence, showing the number of movies they've graced each year throughout their career.

If you're eager to peek at the profile sequences of your cherished actor,  you can search for them here. But, brace yourself, you’ve got to be a fan of old-fashioned movies because, at this stage of our analysis, we're only considering actors for whom we have data spanning their entire career. So, our modern-day heartthrobs still in the thick of their cinematic adventures won't make the cut.

{% include career-all-actors-careers.html %}

Now that we've gathered these profile sequences, let's dive into the realm of clustering to uncover trends in acting. Using the Silhouette score, we've identified two major clusters in the profile sequences. Check out the medoids and centroids – do you see what I see?

{% include career-all-actors-clusters.html %}

One cluster is filled with actors who dipped their toes into the film world with only a handful of movies in their early career before bowing out, while the second cluster boasts actors with long, illustrious careers, gracing the screen with numerous movies.

This somewhat validates the harsh reality: carving out a career in acting is no walk in the park. And when we talk about building a career, we mean here, at the very least, consistently landing acting gigs to keep the dough rolling in.

And alas, the distribution of the number of movies per actor in the clusters confirms the somber truth – the first cluster predominantly consists of less successful actors. Indeed, in this cluster, around 14 thousand actors have taken part in fewer than 5 movies.

{% include career-all-actors-distribution.html %}

My heart goes out to these individuals, but tough decisions must be made. We have to trim the cast, shifting our focus to actors with a more extensive career, and uncover underlying trends in those with at least 5 movies (come on, folks, it's not that much).

But, wait a minute. Before doing that, do you also smell something fishy in the air? Ah, yes, it smells like... gender inequality!

Overall, 33.27% of our actors are female. Now, let's dim the lights and break it down by clusters, shall we?
- Cluster 0: 33.15% of females
- Cluster 1: 25.20% of females

So, not only is the overall percentage of female actors lower than their male counterparts, but this gender gap widens in the successful career-building group. To investigate if this difference is statistically significant, we're bringing in our old friend, the t-test. And yep, treating the fraction of females like the mean of a variable indicating female gender, the p-value confirms the sad truth – it's below the significance threshold: Women have it harder.

After a moment of silence, let’s swing back into clustering. Same method, Silhouette score, 4 clusters. Now, let’s analyze the graph.

{% include career-best-actors-clusters.html %}

Hold onto your seats! There are some intriguing differences, my friends.

 - Cluster 0: *Steady Builders*.
Here, we have our steady career builders. These individuals take their sweet time, adopting a patient and persistent approach to construct their acting legacy. Their journey showcases a gradual but steady increase in movie engagements over an extended period, before gradually dissolving.

 - Cluster 1: *Unsuccessful career-builders*.
Once again, this is home to the non-successful folks who just couldn't take off. We get it; building a career is no easy feat. A few movies in, and it's a reluctant farewell.

 - Cluster 2: *Prolific Long-Term Performers*.
Now, brace yourselves for the prolific long-term performers. This elite group features heavyweights, a small number of actors boasting a significant number of movies over almost 50 years. These individuals have held their ground in the movie industry across a considerable period.

 - Cluster 3: *Ephemeral Success with Progressive Fade*.
Last but not least, we have the actors that burst onto the scene with a strong start, only to experience a progressive decline over approximately 20 years. It's a tale of ephemeral success followed by a gradual decrease in movie engagements. 

Hold on, the plot thickens. Brace yourselves for a stark reality check – gender inequality is alive and kicking. A mere 9% of women in the Prolific Long-Term Performers, 17% in the Steady Builders, 32% for the Unsuccessful Career Builders and 34% for the Ephemeral Success with Progressive Fade. It's indeed a sobering moment for women in the industry. The battle for equal representation rages on.

[Insert fraction of women per cluster in a nice way]

Now that we've got a handle on the typical career trajectories, let's zoom in on the specifics.

First up, we're curious about the age when actors kick off their cinematic journeys. It appears to hover around 30 years old. Now, two burning questions emerge: Is this initiation age different by gender? And does it vary across different clusters?

Breaking it down by gender, we spot some disparities: around 32 for men and 26 for women. Intriguing, right? Let's bring back our trusty tool, the t-test, to confirm the statistical significance. And voila, the p-value makes it official – this difference is indeed statistically significant. But why? Is it because the industry tends to favor younger women?

{% include career-age-first-appearance.html %}

Next, let’s break it down by cluster:

[insert plot boxplot distribution per cluster]

So, the unsuccessful career-builders are the last to start, while the Prolific Long-Term Performers are the first to kick off their careers. Is this hinting that starting acting careers early might indeed be a key factor in achieving success?

Now, onto the second factor to be studied: career length.

{% include career-distribution-career-length.html %}

Once again, let’s check if there are some differences by gender with our trusty friend, the t-test. Computing the p-value, there is indeed a difference. It appears that women also have shorter careers.

# Genres Exploration

Speaking of gender differences, can it also be that women are more stereotypically cast in certain movie genres? Let's embrace the cliché: women star in romance movies, while Westerns are supposedly for the rugged men. Well, prepare for a plot twist because, unfortunately, this is not just a cliché; it's the harsh reality. Below, you'll discover the gender breakdown for each genre that we've meticulously analyzed. And here's a fun fact for you: surprisingly, women are quite terrifyingly well-represented in horror films as well.

[insert pie chart of genres by gender] 

This was a small teaser for the continuation of our analysis. In this section, we will delve into how our beloved actors are scattered across the vast landscape of genres. Our preprocessing allowed us to unveil 26 main different genres in our dataset. Now, here's the twist—most movies find themselves embracing more than one genre, as you can see below.

![Distribution of the number of genres per film](/epfl-ada-datastory/images/genres-number-of-genres-distribution.png)

Therefore, for a more detailed picture, let’s start by exploring which of those 26 genres often go hand in hand. For each genre, the heatmap below showcases the probability of being associated with another genre in the corresponding column. The diagonal indicates the likelihood of being the sole genre present in the movie. Interestingly, most genres are frequently linked to the Drama genre, the undisputed champion in our dataset - around 50% of the movies are in the dramatic club.

[insert heatmap co-occurrences]

The mysterious white square in the above figure represents the Science Fiction enthusiasts among us. We've made the daring decision to split the genre into Science and Fiction. Unthinkable 😨! As you can see, the Science genre is practically inseparable from Fiction, but the reverse is not true. So, Sci-Fi fans, don't worry; you're fully included in the Science genre.

Now that we've covered the intricate blend of movie genres, let's dive into the fascinating journey of how actors gracefully navigate through these cinematic genres. Our strategy? We will calculate the proportion of movies each actor has taken on in our chosen genres. To keep things meaningful, though, we had to wave goodbye to actors with fewer than 20 movies. Apologies folks, but serious results demand a bit of tough love.

[une liste déroulante ou on peut voir les proportions de genres pour chaque acteurs si possible]

Ever wonder if actors freely hop between movie genres or if there's some pattern to their cinematic choices? To crack this mystery, we're studying the correlation of their genre proportions. This will help us unveil whether playing a role in a certain genre clashes with taking on a role in another. For instance, can you picture your favorite comedian actor in a serious drama film? It's like asking a cat to bark, right? 

[Mettre un bouton pour arranger les genres comme à gauche]

The figure above lays out the genre compatibilities and incompatibilities from an actor's perspective. It suggests that if you're eyeing a role in fiction or thriller movies, you might have to dabble in a bit of crime. Not feeling the criminal vibes? Comedy and romance may be cozier options! 

By clicking on the button above, you can shuffle the rows and columns of the covariance matrix displayed earlier. This will unveil two distinct types of career profiles.

In the top-left corner, screen maestros effortlessly navigate black-and-white classics, dance through animated whimsy, and weave heartwarming tales of family and romance. Armed with rose-colored lenses, they paint a cinematic world inviting audiences to embrace the lighter side—with comedy, fantasy, romance, and musicals.

Venturing yourself to the intense bottom-right corner is quite courageous! Here, actors command the stage with compelling intensity, diving into drama, war, thriller, horror, and crime. Masters of suspense, they captivate with performances evoking fear, anticipation, and raw emotion.

And right in the middle, the documentary genre, playing the peacemaker between the chill vibes and the heart-pounding suspense. It's the swiss genre, where actors of all genres can gather, as it remains uncorrelated to most of the other genres.

Finally, to squeeze the most juice out of these genre proportions, we tossed our actors into the clustering cocktail of genres. Behold! We shook things up and stumbled upon six different clusters, each with its own unique flair:

0."The Charlie Chaplin Cluster" - Where timeless charm meets classic charisma.
1."Actors of World Cinema" - Crafting diverse tales beyond Hollywood's borders.
2."The Dramaturgist Explorer" - Unearthing the depths of dramatic artistry.
3."The Multigenre Comedian" - Masters of laughter in every cinematic flavor.
4."The Post-War Western Actors” - Saddle up for a ride through the wild, wild roles.
5."Family Friendly Actors" - Bringing smiles to audiences of all ages.

Check them out below!

[image]

Let's delve into the most distinct traits of each cluster, kicking off with the birth years of our beloved actors. Cluster 0 and 4 are like a time capsule, housing performers from the early 20th century. As for the others, they're still in the running for the "living" category. It's crucial to note that the clustering was based solely on genre proportions. This uncovers the intriguing fact that actors from different eras weren't necessarily stepping into the same movie genres. As the movie industry evolved over time, it forced actors to follow the trend.

[image]

Now, let's cast our eyes on the most common ethnicities within the various clusters. Cluster 1, representing the actors of world cinema, is throwing a Bollywood fiesta, mainly hosting actors from the Indian regions. Though, a tiny troupe of Germans seems to have taken a detour and joined the party. Meanwhile, in the other clusters, the majority of our actors proudly wear the American badge or belong to the Jewish community.

[image]

Alright, actors have their pick of various genres, some of which pair up like a dream, while others might not hit the right note. But here's the burning question: To what extent do our actors delve into the diverse world of genres? 

To answer this, we will use the Normalized Hill's Herfindahl Index (NHHI) as suggested into the following article [An Analysis of Actors in Malay Films: Small Worlds, Centralities and Genre Diversity](https://www.mdpi.com/2227-7390/11/5/1252). Typically used in economics the HHI-score measures market concentration - how much a few companies dominate the production of a good or service. In our scenario, we're replacing the different companies producing a good or service with the genres played by an actor. Using the normalized version of this index, we obtain a genre diversity score for each actor, ranging from 0 to 1. The higher the score, the more our actors have explored a myriad of genres.

Let’s first have a look at the genre diversity distribution:

[image]

Our actors seem pretty curious with an average genre diversity score of 89%, which is equivalent to embarking on a journey through 7 distinct genres with equal enthusiasm. However, it appears that some actors are a bit chicken-hearted in this regard. Let's sneak a peek at the actors who have bravely pirouetted into more genres and those who are treading a bit more cautiously.

[image]

What you see above is, therefore, the genre distribution for actors with the highest and lowest genre diversity scores. Now, one might argue "Well, isn't this just a sneaky way of counting how many movies an actor plays a role in?" Nope, our analysis revealed no correlations between this score and the number of movies an actor has made. So, playing in more movies doesn't turn an actor into a genre explorer. 

To wrap up this genre adventure, let's take on an ambitious challenge and attempt to create the typical genre distribution of an actor in the movie industry across different time periods. To embark on this cinematic journey, we create a Markov chain of genre transitions, mapping out how our actors gracefully leap from one genre to another during their genre-hopping escapade.

[image]

And now, for the grand finale, let's release our actors to whimsically wander along the currents of the Markov river, carried away by its cinematic magic. The result? The steady states, showcasing the unique genre distributions at different epochs.

[image]

Post-1930, the era of talking pictures, and actors had to do more than strike a pose – they had to really talk, and not just in whispers. Extended dialogues became the norm. Tough gig! This period also marked the peak of musicals. Actors weren't just speaking; they had to bring the melody. Acting became a full-body job.

Fast forward to the groovy '70s, the age of color TV. Actors ditched the black-and-white film scene entirely. No more monochrome gigs for these trendsetters!

Last but not least, let's dive into the general trend. It appears our thespians are swapping out their cowboy hats and military gear for action sequences, suspenseful thrillers, and horror escapades. Are they riding the wave of the latest trend, or are our actors just craving a bit more adrenaline on set?


# Oscars

Woah, this has been a ride! Now, for the grand finale of our analysis, let's peek into the ultimate proof of success: the Oscars! 

First, let's refresh our memory on the Oscars:

The Academy Awards, commonly known as the Oscars, have honored the film industry's finest performances since 1929. The acting categories, designed for gender equity, include:

- Actor in a Leading Role: Since 1929, this category has celebrated the artistry of male actors in leading roles.
- Actress in a Leading Role: Parallel to the actors, female actresses have been honored for leading roles since the inception of the Oscars.
- Actor in a Supporting Role: Introduced in 1937, this category recognizes the contributions of male actors in supporting roles.
- Actress in a Supporting Role: Also established in 1937, it acknowledges the talent of female actresses in supporting roles.

Each category features five nominees annually, totaling 20 acting nominations each year. Winners are chosen by the Academy of Motion Picture Arts and Sciences' voting members, one for each category.

Now, with our newfound expertise in Oscars, let's dive into the first act of our Oscar journey. We're investigating whether an actor's gender may influence their career trajectory in terms of Oscar nominations and wins.

{% include oscars-analysis-movies-before-first-nomination.html %}

Glancing at the distribution of the number of movies before the first nomination, a subtle trend emerges: female actors often need fewer movies than their male counterparts to secure an Oscar nod. Moreover, formally testing this with the Mann-Whitney U test reveals indeed a statistical difference …

But hold on, before our gentlemen break out the tissues screaming “gender bias”, let's not jump to conclusions. Let's pivot our gaze to the overall number of movies per gender. 

![Number of movies per gender](/epfl-ada-datastory/images/oscars-analysis-total-movies.png)

Interestingly, the data indicates that, on average, male actors appear in more films than their female counterparts, which is further reinforced by a second Mann-Whitney U test. This may contribute to a fiercer competition among male actors for those coveted Oscar nominations, considering the even playing field in annual nomination counts across gender-specific acting categories. 

Next up on our Oscar exploration: the thrilling journey from nomination to victory. Let's take a peek at the distribution of the number of nominations before an actor clinches the coveted Oscar.

![Nominations before first Oscar](/epfl-ada-datastory/images/oscars-analysis-nominations-before-first-oscar.png)

The histogram paints a picture of a comparably paced journey for both male and female actors. A quick U-test reassures us that there's no significant statistical difference between the two genders. But of course, this was expected, given that male and female actors compete in separate categories with an equal number of annual nominations.

On more of a side note, we can notice that this distribution follows a seemingly exponential decay: most actors seem to get just one shot at the golden statue, with very few managing to secure victory after being nominated more than twice.

Next up, after exploring the number of movies before a nomination and the number of nominations before the first Oscar win, let's unravel the narrative with the number of movies before the first Oscar win.

{% include oscars-analysis-movies-before-first-oscar.html %}

So, the median number of movies stands at 17 for male actors and 11 for their female counterparts, suggesting a distinct pace in reaching the pinnacle of their careers. The U-test outcome adds weight to this observation, with a p-value below the 0.05 significance threshold. This pattern aligns with our earlier findings—female actors tend to nab nominations and wins earlier in their careers compared to their male counterparts, who face more competition and a longer journey to that elusive first Oscar victory. 

Furthermore, a noteworthy insight emerges: a significant portion of actors clinch their first Oscar after a relatively modest number of movie appearances. This hints at the industry's inclination to reward promising newcomers, emphasizing the likelihood of actors winning an Oscar for their breakthrough performance rather than a later endeavor. 

And now, for the grand finale of our analysis! Given our earlier revelation that female actors often kick-start their careers earlier than their male counterparts, the burning question emerges: Does this early start translate into clinching that coveted Oscar at a younger age for our talented actresses?

{% include oscars-analysis-age-before-first-oscar.html %}

The histogram paints a vivid picture: male actors reach their Oscar peak roughly a decade later than their female counterparts! And this discovery is further supported by a good old t-test.

This age-related twist unveils a subtle but significant gender bias in the Oscars landscape. The industry seems to favor actresses in their youthfulness and waits until actors reach their seasoned glory to bestow the coveted Oscar. 

But, wait, until now, we have only looked at the aggregate distributions of actor ages and movie counts. However, our data spans almost a century since the inception of the Oscars. Let’s take advantage of that and explore that temporal dimension!

![Evolution of the age at first Oscar](/epfl-ada-datastory/images/oscars-analysis-age-oscar-evolution.png)

While the age distribution for first-time Oscar winners spans wide, a consistent pattern emerges: male actors generally receive their first Oscar at a later age compared to their female counterparts. Over the decades, we can observe a discernible shift toward older winners, irrespective of gender. This shift may mirror a changing industry perspective that values experience and maturity. Such a shift aligns with the idea that roles with the depth and complexity to garner Oscar recognition are increasingly written for older characters.

Outliers like Tatum O'Neal, who remains the youngest ever Oscar winner at age 10, stand in stark contrast to the overall trend. Observing the trend lines, it's apparent that the average age of today's Oscar winners has climbed nearly a decade since the Oscars began. This pattern underscores an evolving industry paradigm that associates the pinnacle of acting achievement with a longer career trajectory.
