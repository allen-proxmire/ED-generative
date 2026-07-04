# One Number and One Knot
### Why There Are Three Forces, and Three Dimensions

*Allen Proxmire*

*Series: Event Density, Part 5. Companion paper: `Paper_MS-II_MatterSectorFromTheArrow`.*

---

Two of the most basic facts about reality are also two of the most arbitrary-looking. There are three forces of the kind that build matter, electromagnetism, the weak force, and the strong force. And there are three dimensions of space. Physics measures both numbers to exquisite precision and explains neither. They sit in the textbooks like the settings on a machine nobody can find the manual for. Why three forces and not two, or seventeen? Why three dimensions and not four, or eleven, as some theories cheerfully propose?

It is easy to stop asking. The numbers are just what we find, and a measured fact does not owe you a reason. But Event Density keeps asking, because its whole bet is that the facts physics leaves bare are the ones with a story underneath. And the story here turns out to be short. Both threes come from the same place: a universe that commits has to be able to count its signals without blurring them, and keep its records without losing them. Three is the number where both of those just barely work.

One number for the forces. One knot for the dimensions. Let me take them in turn.

## The forces, counted

Recall the idea of a channel, from earlier in the series. A channel is a direction a pattern can keep going in, a stable pathway through the substrate. And recall where the forces came from in part four: when several indistinguishable channels of the same kind run together, the substrate has to keep track of how they mix while conserving its bandwidth, and the mathematics of that bookkeeping is exactly the mathematics of a force. One channel gives electromagnetism. Two channels mixing give the weak force's structure. Three give the strong force's. The size of a force is just how many channels it is juggling.

So the real question is not "why three forces" but "why those sizes, one, two, and three, and why nothing bigger." And that has a clean answer, the firmest result in this part of the program after the gauge groups themselves.

Here is the picture. Think of channels as arrows in a space. For two channels to count as genuinely different, as two forces and not one, they have to point in independent directions, so the substrate can tell them apart. Now ask how many arrows you can have all pointing in genuinely independent directions at once. In an ordinary room, three dimensions, you can stand three pencils mutually at right angles, up, forward, and sideways. You cannot add a fourth that is independent of those three. Any fourth pencil has to lie partly along the ones you already have. It is no longer its own direction. It leans.

Channels live in an internal space of the substrate's, an abstract space of amplitudes, and the same arithmetic applies with a sharp edge. If that internal space has some number of dimensions, call it *d*, then you can run exactly *d* channels that stay cleanly distinguishable. Try to add one more and it is forced to overlap with the others, the signals bleed together, and it cannot survive as its own stable force. So the stable forces come in sizes one, two, three, and so on, but only up to *d*, and then they stop.

We observe sizes one, two, and three, and nothing larger. So the substrate's internal space has *d = 3*. And that single number does double duty. It says the allowed sizes run one through three, which is *why the forces are the sizes they are*. And because there are three allowed sizes, it says there are three of them, which is *why there are three forces at all*. Both halves of the mystery, the count and the sizes, fall out of one number.

I want to be careful about the tier here, because it is easy to oversell. This is what the paper calls *structural*, a coherent and defensible reading of the substrate, not a closed derivation. And notice what it does and does not do. It does not derive the number three out of thin air. What it does is *collapse the question*. "Why three forces of sizes one, two, three" becomes the single sharper question, "why is the internal channel-amplitude space three-dimensional." We have not answered that yet. But we have traded a vague mystery with many loose ends for one clean number to chase, and that is real progress.

It also sticks its neck out. If the stable forces are exactly the sizes up to *d*, and *d* is three, then there is no room for a stable fundamental force of size four or larger. Ordinary gauge theory permits such a thing happily. Event Density leaves no slot for it. Find a stable fundamental force bigger than the strong force and this whole argument is wrong. That is a prediction, and it can be killed.

## But which three is that?

There is an honest catch, and the paper flags it hard, so I will too. The three we just found is an *internal* three, the dimension of an abstract amplitude space inside the substrate. It is not obviously the same three as the three dimensions of the room you are sitting in. One is a complex internal bookkeeping space; the other is real physical space you can walk around in. They are different in kind. You are not allowed to just declare them the same number and call it unification. That would be a word game, not physics.

So hold that thought. We have one three from the forces. Now let us get the other three, the spatial one, completely independently, from a different argument entirely. And then, only at the end, we will ask whether they could secretly be the same.

## The dimensions, knotted

Start from what the substrate does for a living. Its defining act, the arrow, is to lay down an irreversible record of which thing committed before which. That ordering is the universe's memory. It is the difference between a world with a past and a world without one.

A record is only worth anything if it holds. If the order could be quietly rearranged by some smooth shuffling, with nothing torn, then it was never really recorded, just penciled in. So the deep requirement is this: the committed order has to be *held*, locked against continuous rearrangement. And now we get to ask a precise question. What is the simplest way to lock an order in place so that no amount of gentle pushing can undo it?

The answer is a knot. Specifically, the simplest knot there is, a *link*, two loops threaded through each other like two rings of a chain. You cannot pull the rings of a chain apart, no matter how you wiggle them, without cutting one. The link *holds*. The order it represents cannot be smoothly undone. That is exactly the property the arrow needs.

And here is the beautiful part. A link only holds in three dimensions. Not two, not four. Three, and three alone.

Picture a flat world, two dimensions, everything confined to a tabletop. Two loops drawn on a table cannot even reach around each other. There is no over and under, so there is no linking to be had. The order has nowhere to lock.

Now our world, three dimensions. Two loops can thread through each other, and once they do, you are stuck. There is no continuous, non-crossing motion that takes them apart. The link is topologically protected, which is a precise way of saying the universe cannot cheat its way out of it. We checked this in simulation: try to pull two linked loops apart in 3D while keeping them from passing through each other, and they are driven into a collision, the only way out is to crash, which means cutting. The minimum distance between them gets forced to zero. The link genuinely holds.

Now add a fourth dimension. Suddenly there is an extra direction to move in, and any link falls apart. One loop simply lifts itself a little way into the fourth direction, slides past the other with room to spare, and comes back unlinked, never touching. The same simulation, run in 4D, shows the loops sliding free, never coming close, minimum distance staying wide open. In four dimensions, every knot you tie unties itself. The order will not hold.

So three spatial dimensions by elimination. Two dimensions cannot form the link. Four cannot keep it. Only three both forms and holds it. If the arrow needs a place to lock its committed order down, three dimensions is the only room in the house where the lock works.

The tier, honestly. The *topology* here is rigorous and the simulation only confirms what mathematicians have long known, that this kind of linking is a three-dimensional fact. That half is solid. The half that is a hypothesis, and the paper says so plainly, is the claim that Event Density *does* hold its order by spatial linking in the first place. That is the one open premise. The dimensional argument is airtight given the premise; the premise itself is the next thing to test, a probe that would watch the substrate's chains and see whether their order is in fact held by links. Until that runs, this is a strong, specific, killable story, not a finished theorem. (An earlier version of mine framed it as a braiding of worldlines, and that was wrong, braiding is a two-dimensional phenomenon. The correct picture is the spatial linking of curves, which is the three-dimensional one. I am leaving the correction visible because getting it wrong and fixing it is part of the honest record.)

## Where the two threes might meet

Now we can come back to the catch. We have a three from the forces, the internal amplitude dimension, and a three from space, the only place a link holds. I warned you that you cannot just glue them together because they are both three. So here is the careful version of how they might actually be one.

The channels, the things that carry the forces, are themselves laid down by the arrow and woven into the same web. If the channels are held in place by the very same linking that holds the committed order, then their stable structure is not set by some free internal dial at all. It is set by the three-dimensional linking, the same fact that fixes space. The internal three would *be* the spatial three, not because we identified two axes by fiat, which is the error, but because the arrow's held order and the channels' stable count are the same knot, counted twice.

This is the most speculative thing in the essay, and I am marking it as exactly that. It rests entirely on the open premise, the one about linking, and it is the reason that premise is worth chasing so badly. If it holds, then the number of forces and the number of dimensions are not two coincidences the universe happens to share. They are one structural fact about a world that commits, seen from two sides. Two threes, one knot. But that is a prize still on the table, not in the bank.

## What this is, and what it is not

Let me be square about the register of this whole part, because it matters more here than anywhere.

This essay does not overturn any physics. The number of forces and the number of dimensions are measured facts, and they stay exactly what they are. What Event Density offers is a *reason they might be those numbers*, where standard physics offers none, treating both as inputs you measure and move on. The forces-from-one-number argument is structural, a clean reduction of the question, not a derivation of three. The dimensions-from-linking argument is structural too, with the topology measured and one premise still open. The bridge between the two threes is a hope with a clear test attached. I would rather hand you the map with the unpaved roads drawn in than sell you a finished country.

But it does make claims that can be wrong, which is the whole point of doing it this way. There is no room for a stable fundamental force larger than the strong one. And the entire dimensional story stands or falls on whether the substrate really holds its order by linking. If a future probe shows the order held some other way, or shows links do not do the holding, the argument breaks, cleanly and visibly. A story you can kill is worth more than a fact you just accept.

So here is where we land. The universe has three forces and three dimensions not because someone, somewhere, set two unrelated dials to the same lucky number. It has them because a thing that commits has to do two jobs. It has to keep its signals distinct enough to tell apart, and the most it can carry is three. And it has to keep its records locked so the past cannot be quietly rewritten, and the only place the lock holds is three. One number, and one knot. And there is a real chance, not yet earned but clearly in view, that the number and the knot are the same thing wearing two faces.

---

*Next in the series: with the matter sector mapped, we turn to where Event Density parts ways with the textbook for good, the predictions it makes that nothing else does, and the experiments that could prove it wrong.*
