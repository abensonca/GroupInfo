# Conditioning Merger Trees

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `merger trees`

## Test-and-Reject

This is the current approach - simply generate full merger trees, then test them to see if they meet required conditions. If they do not, discard them and try another tree. This is obviously inefficient for strong (or multiple) conditions.

## Conditioning the Branching Rate PDFs

[Notes](https://www.overleaf.com/read/yzcsjyprqvzn) on how we might modify the branching rate PDFs to enforce certain conditions. This seems like the ideal solution, if the math can be made tractable.

## Focused Test-and-Reject

Example: LMC merger onto the Milky Way. In this case, first generate the main branch only of the merger tree back to the earliest time at which an LMC merger is required. Then test for an LMC merger. If one exists, then finish building the remainder of the tree. If no LMC merger exists, destroy the tree back to the latest time at which an LMC merger is required, and try again.

* Probably need some limit on the number of attempts allowed before it gives up an just tries an entirely new tree.
* Would need to added a class which controls:
    * which branches in a tree under construction are followed;
    * tests whether a condition is met;
    * resets the tree walk as necessary to allow construction of the remainder of the tree after the condition is met

Would need to test this by comparing against the original test-and-reject method (both to benchmark speed and to test that the statistical properties of the resulting merger trees are unaffected).