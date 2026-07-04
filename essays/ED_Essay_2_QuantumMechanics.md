# Why Those Rules?
### Quantum Mechanics, Derived From the Substrate

*Allen Proxmire*

*Series: Event Density, Part 2. Companion papers: `Paper_011_5_FourPostulatesUnification`, `Paper_003_BornRule`, `Paper_006_5_Schrodinger_Stone`, `Paper_007_HilbertSpace`, `Paper_012_6_Heisenberg`.*

---

Quantum mechanics is the most accurate theory humans have ever written. It predicts the magnetic moment of the electron to twelve decimal places. It built the transistor, the laser, the chip in the device you are reading this on. Nothing in science has been tested harder or passed more cleanly.

And nobody can tell you why its rules are the rules.

That is not an exaggeration, it is the official position. Generations of physicists were trained under a slogan, "shut up and calculate," which is exactly as cynical as it sounds. The rules of quantum mechanics are handed down as **postulates**: assume states live in a certain kind of space, assume measurement works like this, assume probabilities are the square of something called the amplitude. Use them, they work, do not ask where they came from. The asking was considered philosophy, which in physics is close to an insult.

The strangest of these, and the one worth holding in your mind, is the Born rule. To find the probability of a quantum outcome, you take its amplitude and you **square it**. Why square it? Why not the amplitude itself, or its cube? There is no standard answer. It is simply what you must do to match every experiment ever run. A rule with a perfect track record and no reason underneath.

Event Density takes a different stance. It says the rules of quantum mechanics are not arbitrary postulates at all. They are what the substrate *looks like* when you ask, carefully, what a "state" and a "measurement" actually are. The weirdness is not a mystery layered on top of reality. It is the grain of the substrate showing through.

Here is how that goes, rule by rule, in plain language.

## Before anything commits, there are possibilities, and they are weighted

Recall the picture from part one. The world advances by **commitment**: a region that is unsettled, holding several ways it could go, settles into one, irreversibly. The arrow is that act of settling.

So look at a region *before* it commits. It is not in one definite state. It genuinely holds several possibilities at once, and not equally, some are more heavily participated in than others. That weighting, the degree to which each possibility is in play before the settling, is exactly what quantum mechanics calls the **amplitude**.

This is the superposition that students are told to accept as a brute fact. In Event Density it is not brute at all. It is just the honest description of a region that has not committed yet. Of course it holds several possibilities. Committing is what collapses them to one, and it has not happened.

## Why the square: the Born rule

Now ask the natural question. When the region does commit, what is the chance it lands on a given possibility?

You might guess it should just be the weight, the amplitude. It is not, and the reason is not a convention, it is a constraint. These possibilities are not separate piles of probability sitting side by side. They **interfere**. They can add and they can cancel, the way two ripples on a pond can pile into a tall crest or flatten each other to nothing. Anything that can interfere like that has to be described by something with a direction to it, a phase, not just a size. In the substrate that phase is the **polarity** that rides along every channel.

Once your weights carry a phase and can interfere, ask what can turn those weights into honest probabilities, the kind that always add up to one and never go negative, no matter how you slice the possibilities. Given one substrate assumption, about how a weight sets the rate at which a possibility commits, the consistent answer is the **squared size of the amplitude**. I want to be careful with the tier here, because it is easy to oversell. This is not a theorem pulled from nothing, and the companion paper is explicit that it does not ride on the famous Gleason result. It is a conditional reason, with its one assumption named in the open, and granted that assumption the square is the weighting that survives interference and still adds up to one.

So the most mysterious rule in quantum mechanics, the bare unexplained square, turns into a sentence you can actually say out loud: *probability is amplitude squared because that is the only weighting that survives interference and still adds up to one.* That is the difference between a postulate and a reason.

## The space the possibilities live in

String those two facts together, weights that carry a phase, and the requirement that they combine and interfere consistently, and you do not get to pick the arena they live in. You are forced into a specific mathematical home: a complex vector space, with an inner product, the thing physicists call **Hilbert space** and present as the first and most abstract postulate of the subject.

In Event Density that space is not assumed at the start. It is built, from the bottom, out of what the possibilities are and how they must combine. Hilbert space is not where quantum mechanics begins. It is where the substrate's bookkeeping ends up.

## What measurement is

This one is almost too simple, and that is the point.

For a century, "measurement" has been the embarrassment at the heart of quantum mechanics, the place where the smooth math suddenly stops and the wavefunction "collapses" for reasons the theory cannot state. Whole interpretations, many worlds, hidden variables, conscious observers, exist mainly to paper over this one gap: why does looking change things?

In Event Density there is no gap, because measurement is not a special extra process. **Measurement is commitment.** It is the substrate's one fundamental act, the unsettled becoming settled, seen from the outside. The "collapse" is not mysterious and it is not caused by a conscious observer. It is the arrow, doing the only thing the arrow does. The possibilities were real, the commitment picked one, and because commitment is irreversible, it does not come back. That irreversibility is why you never catch a measurement half-undone.

The thing that needed a whole shelf of interpretations is, in this picture, the most basic event there is.

## How things change in between: Schrödinger

Between commitments, the substrate still evolves. It just evolves *without settling anything*. And evolution that moves the possibilities around without creating or destroying any of them, that keeps the total bookkeeping exactly conserved, has a name in mathematics: it is **unitary**. Unitary evolution is not a third postulate to swallow. It is what "change that has not committed to anything yet" must look like, given the substrate's fixed budget, its **bandwidth**.

And there is a clean piece of standard mathematics, Stone's theorem, that says any smooth, continuous, unitary evolution is generated by a single steady object, which is the form of the **Schrödinger equation**. Let me be exact about what is doing the work. The Schrödinger *form* is carried in, not conjured: it is standard machinery the substrate borrows, not something ED derives from scratch. What Event Density supplies is the identification underneath it, that evolution between commitments has to be norm-preserving and steady under time-translation, hence unitary, given the substrate's fixed bandwidth. So the central equation is not written from nowhere and it is not derived from nothing either: its shape is inherited, and what the arrow forces is that the unsettled possibilities must drift by exactly that kind of smooth, budget-conserving evolution between commitments.

There is a deeper reading here, newer and less settled, that ties this to the rest of Event Density, and I will flag it as the frontier rather than a finished result. The Schrödinger equation is fundamentally about a phase that spreads. And the famous constant in it, Planck's constant, ħ, the size of the quantum, looks in this picture like a measure of **how long that phase survives between commitments**. Commit rarely, and the phase persists, the world stays quantum and coherent. Commit constantly, and the phase is scrambled before it can do anything, and the world looks classical. On this reading, ħ is not a brute number stamped on the universe. It is the substrate's coherence scale, set by how *rarely* it settles. That last step is a hypothesis I am still building, and I want you to hear it as one. It also has the virtue of being able to fail: if coherence is really set by how rarely the substrate commits, then there should be a specific scale at which a specific quantum experiment stops behaving quantum, a place the phase gets scrambled before it can act. Find that experiments stay perfectly coherent past where this says they should not, and the reading is wrong. That is the kind of reason a postulate never gives you.

## Why you cannot pin down everything at once: Heisenberg

The uncertainty principle is the rule that you cannot simultaneously know exactly where something is and exactly how it is moving. Sharpen one and the other blurs. It is usually presented as a strange cosmic limit, almost a prohibition.

In the substrate it is plainer than that. Where a thing is and how it is moving are not two independent facts read off two independent dials. They are two readings drawn from the *same* limited budget, the same finite bandwidth, and they are conjugate, meaning sharpness in one is literally built from spread in the other. Spend your budget making position sharp and there is nothing left to make momentum sharp. The uncertainty is not a wall the universe put up to keep secrets. It is the cost of a finite substrate trying to be definite about two things that are made from one resource.

## One picture, all the rules

Step back and notice what just happened. We did not assemble five separate postulates and tune them to fit. We told one story, the substrate, possibilities before commitment, weighted by participation, carrying a phase, combining consistently, evolving smoothly until something settles, and out of that one story fell, in order: superposition, the Born rule's square, Hilbert space, measurement collapse, the Schrödinger equation, and the uncertainty principle. The rules of quantum mechanics stopped being a list to memorize and became a set of consequences. The weirdness was the substrate, seen edge-on.

## What this is, and what it is not

I have to be straight about the tier of this, because it is easy to oversell and I would rather you trust me than be impressed.

This part of the program does not change a single prediction of quantum mechanics. Event Density reproduces the rules, it does not overturn them. If you were hoping for a video where the famous experiment comes out differently, this is not that video. What this is, instead, is an **explanation of why the rules are the rules**, the reason underneath the postulates, the thing physics spent a hundred years saying you were not allowed to ask for.

A skeptic should weigh that honestly. Reproducing known results, even with a clean reason attached, is not the same as a new prediction, and the new predictions of Event Density live elsewhere in this series, in the matter sector, in gravity, in a specific experiment that should fail at a specific scale. Here, the claim is narrower and, I think, still worth a great deal: that the most successful theory in science does not have to be a black box. Its rules have a reason, and the reason is the arrow.

That is the test I would put to any foundational idea, and it is the one my collaborator on these papers and I keep coming back to. A good theory does not just use the Born rule. It tells you *why Born*. It does not just invoke Heisenberg. It tells you *why Heisenberg*. Anyone can write down a postulate. Earning the reason behind it is the whole job.

Quantum mechanics was never weird because reality is absurd. It was weird because we were handed the rules with the reasons torn off. Put the substrate underneath, put the arrow first, and the reasons grow back.

---

*Next in the series: spin, antimatter, and the Dirac equation, where the same substrate explains why some particles take two full turns to come back to themselves.*
