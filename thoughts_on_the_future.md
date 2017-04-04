# Not Like Me -- Opinions You'll (likely) Hate

## Technical Pitch

Not Like Me is an application designed to create empathy by breaking users out of their self-created social network bubble. Powered by [figure out what algorithm makes sense] Not Like Me follows common news sources and aggregators, and applies the same kinds of algorithms Facebook and others use to put content you're likely to interact with in your news feed--except we reverse the sorting order. In Not Like Me your top posts are the ones you're least likely to "like". Why would we do this?

America is full of people who *do not understand each other*. Just look at the recent presidential election. Even though we're more connected than ever, we are also more able than ever to fall prey to our own confirmation bias. Somewhat ironically, as we have more and more choice over what media we consume we are less deeply informed than ever. Not Like Me uses artificial intelligence and machine learning to intentionally challenge our users to become more empathetic. You must be exposed to challenging viewpoints to expand your worldview. In modern social media it's too easy to create an echo chamber -- this lack of understanding makes compromise and love much harder to spread.

We import your Facebook data to bootstrap our profile of you, then we anonymize your posts before sending them to our database. After that we select from the entire Not Like Me anonymous database of posts to show our users the things they are least likely to have seen. For privacy reasons, we only look at links -- we never request users photos, posts, or other personal data about the user. Our [cool framework] powered front end makes it easy to browse the opinions you'll be most challenged by.

Because we want to create a space of contemplation and reflection -- no posts or comments can be made on Not Like Me. If you want to discuss these topics (and we hope you will!) we encourage you to do so with someone face to face. It's just too easy to be awful to people on the internet.

## Potential Tactics

### User Archetype Classification

Use clustering analysis to create "clusters" or "archetypal" users that represent a broad idea base. For example "Rust Belt Evangelical Christian" or "Bay Area Liberal"


## Pivot -- Exposure

Exposure is a news aggregator designed to show users news they are either likely to avoid, or very unlikely to encounter. The guiding principle of Exposure is that only though understanding the viewpoints of others can we create harmony. We believe in truth-seeking, we also believe that exposure to alternate (sometimes even offensive) idiologies is crucial to personal growth and understanding. Taken with a dose of skepticism, listening to and understanding offensive viewpoints can help you challenge them more effectively. We also believe that having deeper context into the cultural backgrounds, area demographics, and lived experiences of others is incredibly important in seeing their perspective.

Too often we villify each other. When the vilification gets ugly, we hide from each other. When we do this we create echo chambers full of like minded thinkers. Exposure challenges everyone to ask themselves "why do other people feel this way?" Instead of simply saying "I can't believe other people feel this way." Then we ask you to leave an anonymous comment about how the content we showed you made you feel. We use these comments, metadata about where these opinions are popular, and data from the *datausa* API to help give our users more context surrounding the opinion.

Finally, we create a Graph based network of opinion and news articles. Articles can be linked if they make the same argument, or reference the same event, or make opposite arguments. We give users a graphical interface to explore this graph, starting at nodes that offend them. Because nodes have their demographics and popularity displayed, users can find popular counter arguments; more persusaive versions of the same argument; and different interpretations of the same events. Using context data can also help users understand how fringe or mainstream a particular article is;

Exposure is a challenging application, which will sometimes leave users feeling frustrated. Users should


NOTES: http://graphics.wsj.com/blue-feed-red-feed/#/trump


For now we cherry-pick articles and topics based on API availability and source quality, then use user's facebook feed to find out where and who the users doing the sharing are.
