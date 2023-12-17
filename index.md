---
layout: post
title: "Behind the Scenes of Stardom: Decoding the Patterns in Actors' Careers"
permalink: /
---

# Abstract

How do you envision your career? We, as scientists, will probably spend a substantial portion of our career in the same company in a specific field, like pharma, robotics or data science for the most talented of us. For actors, the journey is more complex, involving potential shifts between diverse movie genres and marked by the inevitable highs and lows inherent to the profession. In our project, we aim at analyzing the trajectory of acting careers. 

Usually, when you seek information about someone's career, you turn to LinkedIn. Would you do the same to stalk your childhood actor crush? Well, good news, we are here to do it for you. From the number of connections (actors they have collaborated with), to the potential genre specialization in movies, and not forgetting the prospect of winning an Oscar, let’s delve into the intricacies of our actors’ careers. 

{% include graph.html %}

# Career Characterization

Let's kick off our journey into the fascinating world behind the scenes of stardom with an assessment of our beloved actors' career trajectories. To navigate this cinematic maze, we will need a clever approach to construct and compare their careers. Here's the plan: For each actor, we'll craft their profile sequence, showing the number of movies they've graced each year throughout their career.

If you're eager to peek at the profile sequences of your cherished actor,  you can search for them here. But, brace yourself, you’ve got to be a fan of old-fashioned movies because, at this stage of our analysis, we're only considering actors for whom we have data spanning their entire career. So, our modern-day heartthrobs still in the thick of their cinematic adventures won't make the cut.

[Insert here interactive graph where we can see profile sequence of chosen actor in a drop-down list]


Now that we've gathered these profile sequences, let's dive into the realm of clustering to uncover trends in acting. Using the Silhouette score, we've identified two major clusters in the profile sequences. Check out the medoids and centroids – do you see what I see?

{% include career-all-actors-clusters.html %}

One cluster is filled with actors who dipped their toes into the film world with only a handful of movies in their early career before bowing out, while the second cluster boasts actors with long, illustrious careers, gracing the screen with numerous movies.

This somewhat validates the harsh reality: carving out a career in acting is no walk in the park. And when we talk about building a career, we mean here, at the very least, consistently landing acting gigs to keep the dough rolling in.

And alas, the distribution of the number of movies per actor in the clusters confirms the somber truth – the first cluster predominantly consists of less successful actors. Indeed, in this cluster, around 14 thousand actors have taken part in fewer than 5 movies.

[Insert here distribution of number of movies for each cluster]

My heart goes out to these individuals, but tough decisions must be made. We have to trim the cast, shifting our focus to actors with a more extensive career, and uncover underlying trends in those with at least 5 movies (come on, folks, it's not that much).

But, wait a minute. Before doing that, do you also smell something fishy in the air? Ah, yes, it smells like... gender inequality!

Overall, 33.27% of our actors are female. Now, let's dim the lights and break it down by clusters, shall we?
- Cluster 0: 33.15% of females
- Cluster 1: 25.20% of females

So, not only is the overall percentage of female actors lower than their male counterparts, but this gender gap widens in the successful career-building group. To investigate if this difference is statistically significant, we're bringing in our old friend, the t-test. And yep, treating the fraction of females like the mean of a variable indicating female gender, the p-value confirms the sad truth – it's below the significance threshold: Women have it harder.

After a moment of silence, let’s swing back into clustering. Same method, Silhouette score, 4 clusters. Now, let’s analyze the graph.

[Insert here medoids and centroids of clusters]

Hold onto your seats! There are some intriguing differences, my friends.

Cluster 0: Steady Builders
Here, we have our steady career builders. These individuals take their sweet time, adopting a patient and persistent approach to construct their acting legacy. Their journey showcases a gradual but steady increase in movie engagements over an extended period, before gradually dissolving.

Cluster 1: Unsuccessful career-builders
Once again, this is home to the non-successful folks who just couldn't take off. We get it; building a career is no easy feat. A few movies in, and it's a reluctant farewell.

Cluster 2: Prolific Long-Term Performers
Now, brace yourselves for the prolific long-term performers. This elite group features heavyweights, a small number of actors boasting a significant number of movies over almost 50 years. These individuals have held their ground in the movie industry across a considerable period.

Cluster 3: Ephemeral Success with Progressive Fade
Last but not least, we have the actors that burst onto the scene with a strong start, only to experience a progressive decline over approximately 20 years. It's a tale of ephemeral success followed by a gradual decrease in movie engagements. 

Hold on, the plot thickens. Brace yourselves for a stark reality check – gender inequality is alive and kicking. A mere 9% of women in the Prolific Long-Term Performers, 17% in the Steady Builders, 32% for the Unsuccessful Career Builders and 34% for the Ephemeral Success with Progressive Fade. It's indeed a sobering moment for women in the industry. The battle for equal representation rages on.

[Insert fraction of women per cluster in a nice way]

Now that we've got a handle on the typical career trajectories, let's zoom in on the specifics.

First up, we're curious about the age when actors kick off their cinematic journeys. It appears to hover around 30 years old. Now, two burning questions emerge: Is this initiation age different by gender? And does it vary across different clusters?

Breaking it down by gender, we spot some disparities: around 32 for men and 26 for women. Intriguing, right? Let's bring back our trusty tool, the t-test, to confirm the statistical significance. And voila, the p-value makes it official – this difference is indeed statistically significant. But why? Is it because the industry tends to favor younger women?

[Insert distribution by gender]

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

