# Gitiquette

What do you get when you combine "git" and "etiquette"? Gitiquette!
Don't worry, my former boss and coworkers were unimpressed by that joke too.

However, I think it is worth it to mention a couple of conventions in the realm
of Git and GitHub that help everyone out. They're not required, and they are
subjective, but I think they can help you communicate your code.

## Commits

**Commit frequently**: This was a constant battle with a coworker. He would
do the classic entire user story in one commit and push. Maybe in some respects
this is okay, especially if you're in the very early stages of a project, but
once you're making large and intricate changes, it helps to commit frequently.

The idea here is that you're able to rollback to any state, should something
go wrong. For instance, let's say we have just one commit:
`implement entire product page`

versus the following commits (in order from oldest to most recent):
`implement product lists`
`implement product detail view`
`implement cart functionality`
`implement buy page`
`reimplement buy page`

This is an oversimplified example, but it holds up. What if we broke something
in the `reimplement buy page` commit and we somehow can't figure it out? Let's
revert to the last commit: `implement buy page`; this way, we've got solid
foundations to work from and can revert should things go horribly wrong.
Whereas with the first commit, we now have to sift through the weeds with
everything and just work with what we have.

This is also great because once your branch of frequent commits gets
merged in, you get a more linear and understandable history in the commit log.

**Meaningful commit messages**: This is my silly and meaningless pet peeve. I think
commit messages are pretty easy and usually people mess them up [^ref1].

At least in the traditional sense (follow your organization's guide if it's different),
commit messages use this "command" tone, as if you're commanding someone to do the changes
you did. For instance, you would say `Add sign out button to navbar` instead of `added a signout button to the navbar` or `I added a signout button to the navigation`.

Your commits shouldn't be a narrative, and should be concise and as short as possible.
If you follow the last guideline of committing frequently, the commit names should "write
themselves" - what you did is exactly what the commit name should be.

One friend and I found out that you can put emojis (and most any unicode) in commit messages,
but *it doesn't mean you should!* I've seen some repositories where they might categorize features
and bug fixes with certain emojis, but that seems like the only time it should happen.

## Issues & Pull Requests

Taking an issue or a ticket is like raising a child: you have to see it through
and help it grow and put the work in. You shouldn't abandon it. Work hard
at it and do the best job you can with the issue; these are the small
moments that add up to good software over time.

**Give a brief overview of what happened**: In the description of a pull
request, I like to type out some bullet points of what I did. It helps 
to keep me on track but the person reviewing my code can also
look the description at a glance and find what they're looking for in the code.

**Don't delete early**. I am so often hitting "resolve conversation" early,
which is a bad idea. Get verbal or textual confirmation that your reviewer
understands why you're resolving the conversation, or else they will be
looking for where their conversation went *and* still needing to talk to you
about it.

Follow through with your issues. **Talk to your stakeholders** or boss
or whoever it is to truly understand what the ticket or issue is about.
Don't just work in an isolated environment, see the full picture of
where your fix or feature is in the entire system.


[^ref1]: Please don't look at the commit messages for this repository.
Do as I say, not as I do. ;)
