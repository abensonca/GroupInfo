# Constrained Merger Trees

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `merger trees`

## Conditioned Excursion Sets

We've explored possible solutions using constrained excursion sets using a [Brownian bridge](https://en.wikipedia.org/wiki/Brownian_bridge) approach. But, I think there are some limitations to this that I've not previously fully understood.

Before going into these I think it's worth restating the goal. Ideally, we would like to impose a merger event with given properties (primary and secondary halo masses, time) into our merger tree. In the excursion set approach a merger corresponds to a change in the [supremum](https://en.wikipedia.org/wiki/Infimum_and_supremum) of the excursion (that is, a point where the previous maximum, $\delta_\mathrm{max}$, of the excursion is exceeded). If the previous maximum occured at $(S_0,\delta)$, and is exceeded at $(S_1,\delta+\epsilon)$ (where here $\epsilon$ is a infinetesimal) then we consider that the mass of the trajectory jumps from $M_0=M(S_0)$ to $M_1=M(S_1)$ at time $\delta$, corresponding to a merger with a secondary halo of mass $M_2=M(S_0)-M(S_1)$.

Such a trajectory might look this like:
![](https://i.imgur.com/XCTaRRp.png)
In order to impose such an event in our merger tree - using an excursion set approach - we would need to force _two_ conditions: first that the trajectory first crosses $\delta$ at $S_0$, and second that it then crosses $\delta+\epsilon$ at $S_1$. 

The corresponding trajectories are actually _conditioned Brownian bridges_ (related to [Brownian excursions](https://en.wikipedia.org/wiki/Brownian_excursion)), because we not only require that trajectory to pass through specified start and end points, but also require that it not cross the barrier anywhere between those start and end points.

For example, consider the part of the trajectory between $S_0$ and $S_1$. In order to get a merger of mass $M_2=M(S_0)-M(S_1)$ we require that this trajectory does not cross $\delta$ at any $S$ in the range $[S_0,S_1)$. So, our Brownian bridge must be conditioned to stay below $\delta$ (equivalent to conditioning a bridge to be always negative since we can apply an arbitrary vertical translation). While it's easy to simulate such trajectories ([using the reflection principle](https://stats.stackexchange.com/a/305058)$^\dagger$), what we would need is a model for the distribution $P(\delta|S)$ and its covariance so that we could solve the first crossing problem, and I'm not aware that this is known. _But_, of course, by definition the first crossing distribution here is just $P(\delta|S) = \delta(S-S_1)$ (where I'm re-using $\delta$ here to mean the Dirac $\delta$-function). So, we don't need to solve for any first crossing distribution, and imposing this on our tree is simply a case of sampling from this distribution (i.e. just inserting a halo of mass $M_2$ directly).

A similar situation applies for the region $0 < S < S_0$. Here, we would like to know the first crossing distribution for smaller values of $\delta$, so that we can construct a mass history for the merger tree which is consistent with first crossing at $(\delta,S_0)$. This is again a conditioned Brownian bridge, conditioned to stay below $\delta$. But, in this case we _do_ need to know the distribution function and covariance of the set of all such excursions for $0 < S < S_0$.

The problems with this approach then are:
1. We need to use conditioned Brownian bridges, but I'm not aware of a result for the distribution function and covariance that we would need to solve the excursion set first-crossing problem for these:
2. Even if we could solve this, in practice when constructing merger trees we modify the branching rate function by multiplying by an empirical function $G()$ to give us a better match to N-body simulations. I don't think it is clear that this same empirical correction function would be the relevant one for the subset of excursions corresponding to the conditioned Brownian bridge.

---

$^\dagger$ I think this could be done in the "excursion set simulator" merger tree builder that I experimented with. In that we just generate a trajectory from the excursion set, and look for first-crossings to build a mass history. It seemed to work moderately well (i.e. as well as other methods). You could build in reflection to this by simply looking for steps which exceed the barrier and performing the relevant reflection to force the trajectory back below the barrier. Although, this approach did need to subsample trajectories to get the correct mass-weighting, and it's not immediately obvious to me how that would be included in this case.

### What is the Brownian bridge approach good for?

Since we've developed this (unconditioned) Brownian bridge technology, what is it good for? The trajectory $(\delta,S)$ is the overdensity at some point in the density field when smoothed on a scale corresponding to a variance $S$. The Brownian bridge therefore allows us to construct the excursion set which is conditioned to have some specified overdensity when smoothed on some scale. Translated into physical terms, we can fix the overdensity on a certain mass scale - that is we can fix the environment on a certain mass scale, and construct excursions on larger mass scales that are consistent with that environment.

So, for example, suppose we care about regions which are highly overdense, e.g. $\delta\approx 12$ on, for example, scales corresponding to $10^{12}\mathrm{M}_\odot$. This could allow us, for example, to explore regions which might contain halos which  host the high-mass SMBHs seen at $z\approx 6$. Using the Brownian bridge we can then generate merger trees, rooted at $z=0$, which would be consistent with this high-overdensity region at $z\approx 6$.

Note that I'm being purposely careful with language here - because the halo mass at this time $\delta$ depends on the first-crossing point, we could have a halo more massive than $10^{12}\mathrm{M}_\odot$ - we don't put a constraint on halo mass, just on the overdensity of the environment. This relates back to the classic cloud-in-cloud problem where the region could also be sufficiently overdense to collapse on some larger scale. However, my intuition is that, for extreme cases (i.e. very overdense regions, corresponding to $M \gg M_*(\delta)$) then it is most likely that you _would_ get a distribution of halo masses at $z=6$ that is sharply peaked close to $10^{12}\mathrm{M}_\odot$.

## Semi-refined approach

Back to the original problem. We would like to impose a merger of a given mass halo, $M_2$ with the main branch of our tree at a given time, $t_2$. As we've seen above, inserting the actual merger is trivial, since the PDF is a $\delta$-function. But, we need to build the main branch of the tree back to $t_2$ first, and assign the appropriate weight to the tree such that the distribution of trees is consistent with that we would obtain with a simple brute-force down-sampling approach.

To be more specific, suppose that we want to ensure that $M_1$ (the mass of the main branch) at $t_2$ has the same distribution as obtained from the brute-force downsampling approach. I think that this can be obtained by simply building the main branch (from $z=0$) back to $t_2$ and then assigning a probability:
$$
p(M_1|M_2,t_2) = \left\{ \begin{array}{ll} R(M_1|M_1+M_2,t_2) & \hbox{if } M_1 \ge 2 M_2, \\ 0 & \hbox{if } M_1 < 2 M_2, \end{array} \right.
$$
where $R(M_1|M_0,t)$ is the merger rate function for a halo of mass $M_0$ at time $t$ to experience a merger event with a primary progenitor of mass $M_1$. Note that the probability assigned to the tree is zero if $M_1 < 2 M_2$ since in such cases the tree can not have a merger in which the secondary has a mass $M_2$.

A slightly-more-refined-than-brute-force, "semi-refined" approach then would be as follows:
1. Generate a formation history for the main branch from $z=0$ back to $t_2$.
2. If $M_1$ (the mass of the main branch at $t_2$) is less than $2 M_2$ then discard the tree and go back to step 1. (In fact, we can reject the tree early if at any step in constructing the branch the mass drops below $2 M_2$.)
3. Once a suitable $M_1$ is generated, insert a merger with a halo of mass $M_2$, and multiply the weight of the tree by the probability $p(M_1|M_2,t_2)$ defined above.

The distribution of $M_1$ at $t_2$ should then match that obtained from the brute-force down-sampling approach. 

This approach still involves some brute-forcing, but I expect that (in the specific case we care about - the LMC-MW merger) we will reject very few cases in step 2 above because the typical Milky Way progenitor mass at $t_2$ will be much larger than $M_\mathrm{LMC}$.

I suggest that we try this approach and validate it against the brute-force down-sampling approach by comparing distributions of $M_1$ and time $t_2$.

### Marginalizing over LMC properties

In practice there is some distribution over $(M_2,t_2)$ constrained by observations. If we know that PDF (at least to some approximation), we can in principle just sample from it each time we start growing a tree. I think it is important that when a tree is rejected (for having $M_1 < 2 M_2$ at $t_2$) we need to resample from the distribution of $(M_2,t_2)$. This is because the distribution of $M_1$ will depend both on the "prior" distribution over $(M_2,t_2)$, but also on the "likelihood" of a consistent with each $(M_2,t_2)$.

### Including negative constraints

For a realistic LMC-MW history we probably want to additionally assert that there are no other LMC-like mergers. This is a negative assertion, so I think can be trivially imposed by cutting off the merger rate function for masses above those that would correspond to such a merger.

### Galacticus implementation

To impose these constraints we need some controller object which is aware of all of the parts needed to achieve them. In the case of just the positive constraint (imposing a merger at the desired time) such a controller would need to:
1. Choose an appropriate mass and time for the merger event.
2. If on the main branch, limit the step size such that it does not exceed time $t_2$.
3. At time $t_2$, decide whether to keep the tree:
    1.  If it is to be kept, insert the merger, and apply the appropriate weight.
    2.  If it is to be rejected, prune the tree back to $z=0$, draw a new mass and time for the merger.
4.  Once the merger is inserted, continue building the tree as normal.

If we want to include some negative constraints then we would additionally need to modify the branching rate distribution.

The above then involves the following classes in Galacticus:
* [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass)
    * Choose ($M_2,t_2$);
    * Decide whether to accept/reject the Milky Way progenitor at $t_2$;
    * Insert the LMC halo at $t_2$;
* [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass)
    * Maximum allowed timestep (to limit to $t_2$);
    * Branching rates (to allow negative constraints to be applied);

The [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) class is sufficiently flexible to do the above. The [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) could also be made to do this, but there is the problem that it needs to be aware of ($M_2,t_2$) so that it can impose the appropriate step-size and truncations in the branching rates.

A solution might be to extend the functionality of the [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) class such that, at each step, it provides the [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) object to the [`mergerTreeBuilder`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuilderClass). Then, for example, the [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) could accept a user-defined [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) object as usual, but use the decorator pattern to wrap this inside another object that imposes a maximum timestep to not exceed $\delta_2$, if on the main branch at $t > t_2$. That is:
* If on main branch and $t > t_2$ return a [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) which provides a timestep of $\Delta w^\prime_\mathrm{max} = \hbox{min}(w_2-w,\Delta w_\mathrm{max})$;
* otherwise return a [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) which provides a timestep of $\Delta w_\mathrm{max}$.

A similar approach could be used for the negative assertion imposition perhaps.

In this way, the logic associated with the condition(s) to be applied are kept local within a single [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass)  object.

### Notes on inserting a target halo

I think that, in the new constrained runs, the reason they drop to very low mass very quickly is just a consequence of us sampling from the full range, 0 to M, for the branching masses and then marking whatever mass halo is returned as the "main branch". Most progenitors are very low mass, so this will almost inevitably lead to the first step in the tree jumping to a low mass branch. So, I don't think this approach is going to work well.

Thinking more about this (and remembering some of my prior thinking on it), I think that the problem with interpreting these results is that we fix a point (S2,δ2) on the trajectory, but this does not guarantee that we get a halo at that point. We solve the first crossing distribution, and build a tree based on that, so we have a trajectory that passes through (S2,δ2), but typically will first cross much earlier (i.e. att S < S2).

So maybe our approach is valid, but the interpretation of the condition approached is more complicated/less relevant. It's still unclear to me exactly which branch through the tree this should be applied to.

A different approach would be to use the excursion set simulator tree builder. I think this could be modified to generate a trajectory from the Brownian bridge and then use the reflection principle to create a trajectory that first crosses at (S2,δ2). Then build the rest of the tree as normal. The challenge there is that trajectories need to be weighted to convert from volume to mass sampling. It's not really clear to me how to do that?

Alternatively, we could keep the current approach but slightly modified. First, reatin the sampling from the full range, 0 to M, but always use the most massive progenitor as the main branch. In this attached sketch I've shown a single trajectory from the Brownian bridge (frmo the green to the red point) as the solid blue line. It should be the case that our conditioned solver means that this trajectory must first cross δ2 (corresponding to the upper horizontal dashed line) at some S=Sf (corresponding to the orange dot) between S1 and S2 - and then the trajectory moves above the δ2 line, so we never get a halo at (S2,δ2).

![](https://i.imgur.com/j1MQqIz.png)


But, I think we can apply the reflection principle here - we take the parts of the trajectory above δ2 and reflect them through that line, giving the dot-dashed blue lines. This is then an equally probable trajectory as the original. In particular, that implies that the trajectory for S < Sf corresponding to the first crossing (orange point) is a valid trajectory, correctly sampled from the distribution function of all trajectories in this Brownian bridge.

So, suppose we build our tree main branch back to time δ2, where it has a mass Sf < S2. Through the construction above we can now insert a progenitor at this time corresponding to S2 (i.e. at δ2 the trajectory jumps from Sf to S2). That progenitor will either be a halo on the main branch, or a halo that merges with the main branch, depending on whether M(Sf) > 2 M(S2). But, either way, we have now placed a halo at (S2,δ2) precisely, with a valid main branch at δ < δ2. 

It seems like this does a lot of what we want it to do. The only thing that I think is still slightly problematic is that this requires that the (S2,δ2) progenitor be either on the main branch, or merges directly with it - it doesn't allow for cases where that progenitor first merged with some other progenitor in a side branch. But, maybe this isn't a big deal.

For practically implementing this in Galacticus - I think we have most of what's needed - the conditioned branching rates are already all implemented. The remaining thing would be to identify when the main branch reaches δ2 and then insert the required halo directly. This is probably best done via the `mergerTreeBuildController` class - it could probably just check if the last-inserted halo is a) on the main branch, and b) exists at δ > δ2 while its parent exists at δ < δ2 (such that this represents the step straddling δ2). Then, it would replace that halo (and any sibling) with the required target progenitor (plus a second progenitor to hold the remainder of the mass). 

I think a good first step would be to go back to the case where we always follow the main branch (so remove the edits in the `mergerTreeBuilderCole2000` class), run the constrained case again, and check that the main branch mass at δ2 is always such that S < S2. If it is, then I think that shows our constrained trajectories are working as expected, and we can figure out the `mergerTreeBuilderController` to insert the target halo.

## "Intelligent" Brute Force Approach (18-July-2025)

This approach is implemented in Galacticus since 19-December-2024 via the `mergerTreeBuilderConstrained` class. This uses the classic brute force approach (i.e. generate a merger tree, check if it meets our required constraints, and reject it if it doesn't), but does so more efficiently - particularly when multiple constraints are applied.

In summary this approach:
* Breaks the process of building a merger tree into an aribtrary number of phases. 
* Typically, in each phase, we apply a single constraint, once that constraint is met, we move to the next phase which will apply the next constraint, and so on.

This approach has two advantages:
1. For each constraint we build "just enough" tree to be able to check the constraint. For example, suppose we are constraining MW trees to have an LMC - typically this is a constraint to have a progenitor of a certain mass infalling at a certain redshift. We then need only build the tree with mass resolution just enough to resolve potential LMCs, and back to just a sufficiently high redshift to find potential LMCs. This is cheap to do (low resolution, and only building to a relatively low redshift). If the tree does not have an LMC we reject it and try again. If it does have an LMC, we move to the next phase. This makes it very fast to satisfy our first constraint.
2. For the next constraint, we start from the previous "just enough" tree, and grow it further (in both mass resolution and redshift) to test if it meets this next constraint. If it does, we accept the tree, if it does not, we restore to the "just enough" tree from the prior phase (so, in our example above, if we are now trying to add a GSE merger, we don't need to go through the process of finding a tree with an LMC again) and try again.

Some caveats:
1. We always need a final phase that builds out the remainder of the tree (to whatever mass resolution and redshift we want) - this is straightforward.
2. The approach works for constraints that are "non-overlapping" in a window of mass resolution and redshift, so that we can test each constraint independently. I think it can probably work (although less efficiently) even for overlapping constraints, but this needs more careful though.
3. We have to be careful about the weights assigned to trees. In the example above, it's possible that not all MW+LMC trees are equally likely to have a GSE merger. This would naturally be accounted for in the classic brute force approach (where we remake the "LMC" part of the tree on each trial), but in this approach, once we've generated the LMC part of the tree it is kept fixed until we find a GSE merger, _even if_ this particular MW+LMC tree is very unlikely to have a GSE merger. To address this, the weight of each tree is divided by the number of attempts that it took to meet each constraint at each phase.  This effectively gives us a Monte Carlo estimate of the relative likelihood of each MW+LMW tree to have a GSE merger, for example. This is something we should probably test to verify that it works reliably.

An example of this approach can be found in the `testSuite/parameters/constraintMilkyWay.xml` file, which implements the example above.

In that file we start tree building with:
```
  <mergerTreeConstructor value="build"/>
  <mergerTreeBuilder value="constrained">
    <!-- A three stage build, which builds: 1) LMC; 2) GSE; 3) everything else -->
```
which selects the `constrained` tree builder. As noted, it uses three phases. For each phase we specify a tree builder (to build the "just enough" tree) and a filter (to test if the tree meets the constraint). For the first phase:
```
    <!-- Stage 1: LMC -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="massTimeWindow">
	<massMinimum value="1.2e11"/>
	<timeMinimum value="11.6"  />
      </mergerTreeBuildController>
    </mergerTreeBuilder>
    <mergerTreeFilter value="anyNode">
      <!-- Label as LMC -->
      <label            value="LMC"/>
      <labelDescription value="Label indicating if this node is on the LMC branch."/>
      <labelBranch      value="true"/>
       <!-- Apply all LMC conditions -->
      <galacticFilter value="all">
	<!-- Consider the main branch (i.e. Milky Way halo) of the tree only -->
	<galacticFilter value="mainBranch"/>
	<!-- Consider only halos infalling at the right time. -->
	<galacticFilter value="intervalPass">
          <nodePropertyExtractor value="time"/>
          <thresholdLow  value="11.6"/>
          <thresholdHigh value="12.0"/>
 	</galacticFilter>
	<!-- Consider only halos with a rank-2 child with a mass above 1.0e11 -->
	<galacticFilter value="childNode">
          <childRank value="2"/>
          <galacticFilter value="intervalPass">
            <nodePropertyExtractor value="massBasic"/>
            <thresholdLow  value="1.2e11"/>
            <thresholdHigh value="1.4e11"/>
          </galacticFilter>
	</galacticFilter>
      </galacticFilter>
    </mergerTreeFilter>
```
builds a tree to just enough mass resolution and redshift to allow testing for an LMC, then looks for mergers with halos in the right mass and redshift range to be an LMC (and then labels that branch fot the tree as "LMC").

In the second phase we have:
```
    <!-- Stage 2: GSE -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="massTimeWindow">
	<massMinimum value="1.3e11"/>
	<timeMinimum value="2.8"   />
      </mergerTreeBuildController>
    </mergerTreeBuilder>
    <mergerTreeFilter value="anyNode">
      <!-- Label as GSE -->
      <label            value="GSE"/>
      <labelDescription value="Label indicating if this node is on the GSE branch."/>
      <labelBranch      value="true"/>
      <!-- Apply all GSE conditions -->
      <galacticFilter value="all">
	<!-- Consider the main branch (i.e. Milky Way halo) of the tree only -->
	<galacticFilter value="mainBranch"/>
	<!-- Consider only halos infalling at the right time. -->
	<galacticFilter value="intervalPass">
          <nodePropertyExtractor value="time"/>
          <thresholdLow  value="2.8"/>
          <thresholdHigh value="5.8"/>
 	</galacticFilter>
	<!-- Consider only halos with a rank-2 child with a mass above 1.0e11 -->
	<galacticFilter value="childNode">
          <childRank value="2"/>
          <galacticFilter value="intervalPass">
            <nodePropertyExtractor value="massBasic"/>
            <thresholdLow  value="1.3e11"/>
            <thresholdHigh value="2.5e11"/>
          </galacticFilter>
	</galacticFilter>
      </galacticFilter>
    </mergerTreeFilter>
```
which extends the LMC tree to a mass and redshift to allow us to test for a GSE merger, and then performs that test.

The final stage:
```
    <!-- Stage 3: Finalize -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="uncontrolled"/>
    </mergerTreeBuilder>
    <mergerTreeFilter value="always"/>
```
builds the remainder of the tree.

Some notes/caveats:
1. The filters used to test if a tree meets a constraint are currently quite simple - they just check for halos in a given mass/redshift range. These could be made probabalistic, such that we could input a distribution of masses/redshifts for, e.g., the LMC, and trees would be accepted/rejected stochastically based on that probability distribution. This might be useful given that the constraints on masses/infall times are quite broad.
2. There is currently no method to ensure that these constrained halos are on reasonable orbits. This, in principle, is easy to implement. Currently orbits are assigned by drawing from a cosmological distribution. We could make a new orbit class which checks if the branch is labelled and if, for example, it finds a branch labelled "LMC" it sets some fixed orbital parameters suitable for the LMC, otherwise reverting back to sampling from a cosmological distribution. The difficultly is that constraints on orbital parameters are typically at $z=0$, not at the infall time, which is when Galacticus needs them. Two options:
    1. In some cases at least, other works have traced orbits back to the infall time, so we could use those as constraints.
    2. We could attempt, given the $z=0$ constraints on the orbit, attempt to make an estimate of the properties at infall. In principle, we know the host halo potential as a function of time, so we can just integrate backward in time to get orbital parameters at infall. This wouldn't account for any baryonic contribution to the potential (since we don't know that until we actually evolve the tree forward in time). Also, integrating backward in time when there is a dissipitative force (like dynamical friction) can be unstable - but maybe this isn't a problem here - it would just make the orbital parameters at infall more uncertain, but that's probably realistic.
3. Constraints on other properties and "negative" constraints: after each stage tree build, a `mergerTreeFilter` is applied which returns `true` or `false` depending on if the tree meets some set of criteria. Those criteria can be anything we want, including a "negative" constraint (i.e. the absence of a merger over some redshift interval). Some small caveats to the "anything we want" statement:
    1. We may need to implement specific `mergerTreeFilters` if there are very specific tests needed. Things like mass and redshift ranges are implemented, but more complicated things might need additional work. I don't expect this to be difficult though.
    2. Currently, when the filter is applied the tree is currently in a state where only the masses and redshifts of each halo have been determined - halo concentrations etc. have not yet been determined. So a filter on properties like `Vmax` would be more difficult. We can get around this in some cases by computing these quantities after each stage of build and before the filter is applied. But, some of these are computed using the full tree structure, which we don't yet have at this point. Probably this can be handled by applying a coarse-grained filter in quantities that we do have (mass, redshift), and applying a filter on Vmax etc. after the full tree is finished. This would reduce efficiency, but maybe not by too much.