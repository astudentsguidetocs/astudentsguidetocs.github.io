# Good Code

When I first started to code all of those years ago,
I was inspired by [this video](https://www.youtube.com/watch?v=DBXZWB_dNsw)
about a "prodigy" programmer, Santiago Gonzalez, who went to Mines when
most people around his age would've been starting high school [^ref1].

In this video, both Santiago and Mines professors speak about the necessity
to not just writing code but to write *good code*. And while I agree with them,
I didn't truly understand what good code was for years [^ref2].

The naive understanding is that shorter code equals better code, which is
definitely not true and likely just presented as a simplistic measure in that
video. However, I often see introductory computer science students assume or 
equate that in their own minds, so I think this is important to debunk.

Short code *can* be better, but if you're gunning for a one-line solution that
is just going to be rewritten by someone else in the future, you should rethink it.

This isn't to say that we can't be smart, e.g.:
```python
lst = [1, 2, 3]
count = 0
for el in lst:
    count += el
print(count)
```
versus:
```python
lst = [1, 2, 3]
print(sum(lst)) # better!
```
The second case is better because we're not reinventing the wheel
and it's semantically meaningful and obvious what the code is doing.

**Writing good code is about communicating well**. If other people can
understand it, you're doing the right things. This doesn't just mean what
I've said above; it's everything that comes with it: comments, variable names,
maintainable code, etc. See the *Good Code* and *Design Principles* sections for more.

Good code is also **readable**. I learned to read code before I learned to write it,
thanks to an online course that was more about copy-pasting [^ref3] than truly
writing. But I learned the importance of understanding everything in the code
and recognizing patterns throughout. I can assure you that you will deal with 
many different codebases of varying quality and organization throughout your 
career. Reading and understanding the code quickly will always take some time, 
but you will get better and better at it with practice.

## Good Decisions

Writing good code is good, but when you think on a larger scale of a good
system, there are other considerations. In September 2024, two Google engineers, Paul 
Christopher and Rob Warner, came and gave a tech talk to [Mines ACM](https://acm.mines.edu) [^ref4],
had a really memorable quote:

> The things that are expensive to change are the things that are hardest and most important to get right. Building good systems means making good decisions, not writing good code.

I love this quote. For context, Paul often says in his talks that he spends a lot,
if not the majority of his time (as a senior engineer) deleting and refactoring code.
Thus, making good decisions is important. The more code you add, the more room for error there is.
The worse your design is, the harder everything will be to maintain in the long run [^ref5].

If you make good decisions, your systems and your code will reflect it. You and your
fellow engineers hopefully won't hate working on it. If you make good decisions, your
systems will scale in both capability and maintainability over time.

## Good code just has to make money

There's one alternative perspective I want to share. One of my old bosses used
to say that as long as the product is making money, we don't necessarily
need to worry that much about the code.

I'm too much of an idealist to fully agree with him, but I see his point.
Especially if you're a startup or small company, you can't waste time forever
trying to improve and clean your codebase. You're out there on the frontlines
trying to push out the next feature ASAP so that you can grow and stay afloat.

I disagree with this point mainly because if you're just rushing features out,
eventually your code is going to catch up with you and be a pain to work in.
There's a balance to be found here: can we write good code and make good
decisions the first time so we don't get into these situations anyways? :)

I don't think there's a right or wrong answer here, it depends on the case.
Just weigh your options: does fixing *X* and *Y* in the codebase save us more time
and money in the long run than it would to push a few more features out of the door?


[^ref1]: This is actually how I found out about Mines, and from about 7th grade,
I had dreamed of going and following his footsteps. It's funny to look back on.

[^ref2]: For years, whenever I had asked for help in communities online, I was more
preoccupied making sure my code was "beautiful code" than actually receiving any help.
Not to say good/beautiful code isn't a good thing, but when you're learning, you
have other priorities. Hopefully where you learn from teaches both.

[^ref3]: Not to say it wasn't a good course. It was a Minecraft modding course
for 8-12 year olds. I think there's little chance that you can explain the
intricacies of Java to an 8 year old, so I see why they taught it the way they
did.

[^ref4]: I love these guys - I think I've seen every Paul Christopher talk since
Fall 2021, and he never disappoints. Rob also has come along and delivered really
insightful advice.

[^ref5]: ...and especially in the context of Google, you wouldn't want to end up
in the [Google Graveyard](https://killedbygoogle.com)!
