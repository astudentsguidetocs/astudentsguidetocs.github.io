# Design Patterns

Design patterns might seem like a weird thing to put in a book
with so much soft skill and people-based advice. I agree! But if you're
just starting out in computer science, I think it's helpful to know
that these things exist and are out there (and are made to help you and your team!).

[Refactoring Guru](https://refactoring.guru) is a wonderful resource with both
free and paid resources that can help you learn more about design patterns (and
refactoring, which is another great skill to have).

Design patterns are great because they can improve our ability to maintain
code, explain it, and understand it. It might be a little more advanced, so
don't worry about learning them at the introductory level, but as you get more
intermediate and advanced in the field, give them a try.

Most languages also have books like [Effective Java](https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997)
which explain patterns, paradigms, and other useful things that help you get to that
next level of understanding [^ref1].

## MVC Architecture

Model-View-Controller (MVC) is an architectural sort of design pattern. The **Model** manages 
the data and logic; it may (and probably does) hook up with the database. The **View** manages 
the "frontend" logic; whatever is displayed to the user. The **Controller** lives between the 
two, routing the model data to the view.

MDN has a [great article](https://developer.mozilla.org/en-US/docs/Glossary/MVC) on this and provides this image:

![mvc](../../assets/mvc.png)

There are other patterns such as MVVM (Model-View-ViewModel), and others. Altogether, these
are great things to consider when you're first designing a website or service.

And again, I'm just trying to give a five second overview. Do some more reading on it! :)

## Builder Pattern

One design pattern that might be useful as an example is the Builder Pattern. A friend
and I often joke that this is the best design pattern and we should even do nested
builders (which he *has* done). Either way, it's normally one of the first ones people learn.

The Builder pattern is great if you need to create objects quickly. You leverage returning
the object itself until it's constructed (in which case you call `build()`) and chain calls
together to make an object.

Here's an old Java example from my Minecraft days [^ref2]; this code is meant to
construct an item programmatically that could be given to the player:
```java
public class ItemBuilder {

    private ItemStack itemStack;
    private ItemMeta itemMeta;
    private Material material;
    private int amount;

    public ItemBuilder(Material material, int amount) {
        this.material = material;
        this.amount = amount;

        this.itemStack = new ItemStack(material, amount);
        this.itemMeta = itemStack.getItemMeta();
    }

    public ItemBuilder setDisplayName(String name) {
        itemMeta.setDisplayName(name);
        return this;
    }

/* ... other methods, excluded for brevity ... */

    public ItemStack build() {
        itemStack.setItemMeta(itemMeta);
        return itemStack;
    }
}

// new class calling it:
ItemStack item = new ItemBuilder(Material.DIAMOND_SWORD, 1).setDisplayName("Andúril").build();
```
Instead of something like:
```java
ItemStack item = new ItemStack(Material.DIAMOND_SWORD);
ItemMeta meta = item.getItemMeta();
meta.setDisplayName("Andúril");
```
...while it's only three lines, this gets old *quickly*. Especially with things
I omitted, like item enchantments or lore (text shown when you hover over the item).

Boom! Intro to design patterns. There's more to learn, so check out the links to
Refactoring Guru and Effective Java above. Design patterns are (mostly) language agnostic
too, so don't worry if you're not into Java.


[^ref1]: I asked for this book for my birthday one time. My parents were slightly confused 
and perhaps a twinge disappointed. :)

[^ref2]: This code is over 5 years old, and the APIs have changed *massively* since then.
I'm including this example because it should be pretty clear. This is *not* how you do this
anymore.
