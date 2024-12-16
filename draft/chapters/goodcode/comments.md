# Comments

Recently I was in a coding interview with a "big tech" company.
I had stumbled through the actual coding part and found a decent
recursive solution and was happy with myself, and then I got a random
question from the interviewer: "What do you think about commenting?
What is your policy on commenting code"

I made up some rushed answer about how I like to comment and try
to comment everything, but also there's a balance in commenting
and if the code is self explanatory it's not necessary.

Almost immediately after, he spoke for 2 minutes on how commenting is 
the worst (or so it felt like it, as I nodded along like 😐) and this is
something they would watch out for and work on at the company and how
you should be writing the most glorious code that does not need commenting.

Further, at one of my internships, my boss was actually adamant that
we shouldn't be commenting code (to my coworkers' delight!) and **definitely**
not writing any documentation; again with the idea that the code itself should suffice [^ref1].

However, school harps on you repeatedly to comment your code. From your
first CS class to your software engineering course, you're expected to
follow "good practices" and comment.

What's the deal with commenting?

## It's a balance

I greatly respect my old boss and also that guy in the interview, but
I would politely disagree with them. Like all things in life,
it's a balance!

Yes, I think the popular and rising argument that the code should 
suffice itself **is true**. Don't go around trying to one-line things
into oblivion for the sake of "efficiency" - if it doesn't make any sense
to look at at-a-glance, then you've just wasted everybody's time with regard
to literally anyone and everyone who looks at that code in the future.

But I would much rather write a comment and have to remove it then write
important business logic that makes no sense and have to rework it or try to
understand it. Inevitably, if you're doing complex and useful things, I would
imagine you'll have some code that needs commenting or documenting.

And, like in the last section, if there are architectural/planning decisions,
they definitely should be commented. Or, another scary idea, we could
*write documentation* and put it there. 😱

Your job will inevitably have some "requirements" one way or another,
but ultimately I think as long as you can communicate your design and
thought process whether it's through commented or uncommented code, you
can't go wrong. It's just the necessity to be *willing* to communicate.

[^ref1]: In that internship, I actually stubbornly wrote some code
that contained comments. Wonder if they deleted it yet.
