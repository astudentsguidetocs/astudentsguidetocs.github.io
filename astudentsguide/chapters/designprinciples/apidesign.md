# API Design

For beginners: [REST](https://www.redhat.com/en/topics/api/what-is-a-rest-api) 
and [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 
are great acronyms describing how we design APIs and web operations.
API design is one skill I want to get better at, but here are a few 
things I've noticed anyways:

**Design as if you're the one using it**: Often we
design APIs with the idea that we need to handle every
edge case and provide *all* of the options to users.

Remember **YAGNI**: you ain't gonna need it. If you don't
need it, don't add it. Even if hardly anyone ever uses it,
if you have one person using it, they're going to be up in
arms once you delete or change it.

Keep the useful parts of your APIs and frameworks in, and
if you're short on inspiration - imagine how you as a developer
would *want* to call your own API.

**Beware backwards compatibility**: As mentioned, people
will probably be up in arms once you change your APIs. This
is also why we get lovely URLs chained together with /v1/ and /v2/
and what not, so that we can maintain backwards compatibility.

It's okay to maintain backwards compatibility, and necessary if
that's what you're doing, but eventually you should get your users
up-to-date if possible [^ref1].

**Document it well**: There's no excuse not to document APIs well
with new things like [OpenAPI](https://www.openapis.org) or even GPT.
Heck, with the rise of [Cloudflare Workers](https://workers.cloudflare.com), APIs
as a whole are changing.

But a bit of documentation never hurt. This goes for everything in your project
or product.


[^ref1]: You should keep everything you use up-to-date, but obviously
this is a money and time drain and can't always be done. Make an effort though.
