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

[insert distribution of career lengths by gender]

Once again, let’s check if there are some differences by gender with our trusty friend, the t-test. Computing the p-value, there is indeed a difference. It appears that women also have shorter careers. 

Now, let's dive into the number of active years for actors. We're defining an active year as one where our stars graced the silver screen with their presence.

[insert active years and number of movies plot]

Examining the graph, it's clear that many actors have significantly smaller active years compared to their overall career lengths. Not surprising at all, considering the constant struggle to secure consistent job opportunities in the challenging world of acting. Only a handful have truly hit the jackpot, with active years that closely match their entire career lengths. 

Moreover, there seems to be no apparent correlation between active years and career lengths. Let's solidify this by calculating the Pearson correlation coefficient. The observed correlation coefficient for actors stands at approximately r ≈ 0.59. To put it to the test, we created a null model, randomly sampling values of L and s from the pool of career profiles. Interestingly, the observed correlation is not significantly different from what we could expect by random chance alone. The cinematic journey remains a mysterious and unpredictable ride!

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
