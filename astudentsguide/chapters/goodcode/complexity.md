# Complexity

Complexity can mean two things: time complexity, or
literally complexity in a system [^ref1]. I'll
refer to both as such below for clarity. I had
originally planned to just write about complexity,
but I figured time complexity wouldn't hurt to
mention here too.

## Complexity

Senior engineers such as those from Google or my previous
internships seem to all agree that complex systems are
kind of the devil. (I'll speak about a talk from Google
engineers in the next section.)

This has also been a coming-of-age realization in my growth
as an engineer. I used to want to make the absolute *best* systems
made for longevity that were optimized for everything in advance
and covered every imaginable use case.

**It's not a problem until it's a problem**. Often, these projects
went nowhere because we got lost in the sauce of complexity; trying
to cover every base and every little thing slows people down.

We're getting a little more into the business side with this chat,
but that's not a bad thing. You can and should make decisions that 
prevent the scope of the project from quickly growing out of reach, 
because it inevitably will if you don't make some sacrifices.

Complexity, whether by adding another framework, library, more API endpoints,
more features, or whatever it might be, leads to more that sits in you and your 
team's headspace. It will probably come up when you least expect it or want
it to, and it will be inconvenient to fix it.

This isn't to say good systems can't have complex features, but rather
to pick your battles. It would be better to take some time to think upfront 
and make a good decision rather than having to spend hours working around it
or rewriting it in the future. Rewriting things takes time and money,
which are two things we would rather save.

## Time Complexity

One thing that I never really expected from my CS degree
was a talk about complexity. Everyone reading this probably
has at least heard of it, but if not, in an oversimplified
manner: time complexity describes how quickly a program 
will run *in the worst case*. For the purposes of this writing,
I'll make it quick, as I think other points are more important
but this is still worth mentioning:

Time complexity-optimized solutions are nice, especially as they're
the focus of many academia classes, like *Algorithms*, *Theory of Computation*,
*Programming Challenges*, and probably more.

Often, however, I think people in and coming out of academia worry about it too
much or too little; they're always horrified of doing a triple-nested for loop for the
O(n^3) complexity. Or, they might not even think twice about the data structure they're
using for an operation.

I think there's a balance: write the code first and see if you can optimize later.
Or, write it optimized the first time if you can (I wouldn't think of 
that immediately, and I know others may feel the same). This is also why code reviews
exist. In an ideal world, your boss or friendly neighborhood senior engineer is going 
to hopefully catch things if they're a big issue.

It's also important to consider the use case; one time I had written a quadruple-nested
for loop in a research project, and to my surprise, my advisor's reaction was
that he didn't really care. Yes, it was a rather poor complexity, but the dataset we
were working on was small enough to where the difference would be negligible.

TLDR: Time complexity is good to know and have in the back of your mind, but know
your use case.


[^ref1]: Sorry, space complexity, I didn't forget about you, 
just not super relevant here. :)
