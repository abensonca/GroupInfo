# Overview of Streams-Probe Research Program(public)
## Brief Overview
* Stellar streams (long thin streams of stars)are an exciting new test of dark matter
* "Gaps" are created in the stream when subhalos(particularly dense clumps of dark matter) "flyby" and perturb the streams gravitationally.
* Perturbations are noticeable because streams are so "cold"(velocity is very uniform; this has to do with their formation process), but very few gaps form  ($\mathcal{O}(1-2)$ per stream)
* Lots of numerical work has been done to understand gaps  for single flybies and idealized streams, but what's needed is a systematic test. By predicting all the gaps in all streams based on all known sources(and including other flyby information), we can perform an exciting new test that (I'm almost positive) hasn't been done before
    * This is a *statistical* test, and can only be useful in the aggregate: if CDM predicts 2.1 gaps in Pal-5,  WDM  predicts 1.8 gaps, and we see 2 gaps, which model is right? 
* With all this,the goal is to either rule out CDM(or it's competitors), or at least constrain things a bit more.
    * Should be very easy to make a no go theorem for MOND, ruling out all past, present, and future modified gravity models that don't have rich substructure(to my knowledge, these are sparse or nonexistent.)


## Paper I: Cold Dark Matter
### Goal
* Back in 2016, Dennis Erkal (and collaborators) made estimates of the number of gaps we'd see in famous streams based on a simplified model.
    * This built on a number of previous papers, by himself, Yoon (in 2011) and others.
* Erkal modeled subhalos with a  "Plummer Model",  a simplified mass profile that is both integrable and computationally softened. However, it is "cored", and underpredictes the number and size of real gaps:
$$\vec{F}_\mathrm{plummer} = \frac{GM}{r^2 +r_p^2}  $$
* This allowed for a qualitative undertanding of the 3 phases of gap formation(compression, expansion, cautics), and initial estimates of gaps in streams such as Pal-5 and GD-1. However, (as I was told), the authors felt that this work wasn't powerful enough for actual constraints, and the program was abandoned.
    * (To my knowledge), this specific approach has sat since then.
* Our paper not only repeats all the work above, it also:
    1. Generating tidally stripped NFW subhalos in Galacticus (increase gap predictions by a factor of 1.5-4)
    2. Track each subhalo individually through it's formation process (up to subsampling), rather than using an analytic distribution.
    3. Numerically solve relevant equations that were approximated, and extended beyond their domain of validity.
* This formed the foundation for a much numerical tool, increased the number of gaps predicted, and avoided the (unphysical) minimum gap size of 7º of their paper.
* To speed up computations, for subhalos with $ r_subhalo < b$, we can treat the subhalos as point masses, and thus get the analytical equations:
$$ \Delta v_{x,\mathrm{point}} = \frac{2GM(b w^2 \cos(\alpha) +y w_\perp w_\| \sin(\alpha))}{w(b^2w^2 + y^2w_\perp^2)}$$
$$ \Delta v_{y,\mathrm{point}} = \frac{-2GM w_\perp^2 y}{w(b^2w^2 + y^2w_\perp^2)}$$


### Progress Check
* 2 modifications to paper 1? Empty shells (need to get radius right) and point masses (with minor softening). Put in countTable and *maybe* graphs?
* Regenerate data for apocenter and pericenter(it's 100% wrong.)
* Paper is submitted(!!), and is just awaiting reviewer comments.
* May attempt a more thorough rewrite when comments come back. 
* Add point mass and shell profile to count table, histogram of gap sizes with all models, and plot of gap counts with all models.
* Redo the pericenter and apocenter data(it's eggregiously wrong.)


## Paper II: Warm Dark Matter
### Goal
* Follows the same roadmap as paper I, but with Warm Dark Matter subhalos. 
* Due to Galacticus's modularity, it's easy to "swap in" a WDM subhalo population.
    * There is much less additional work exploring how a WDM population creates gaps.
* For large masses, WDM has the same subhalo shape(profile) and population(mass function) as CDM
    * But, below a "cutoff mass" that changes with how heavy the WDM particles are, WDM predicts basically no subhalos. 
* By probing this region using streams, we can try to look and see if these "light" subhalos(roughly $10^5\odot < M_\mathrm{subhalo} < 10^7M_\odot$) are there. 
* In addition to figures like the previous paper, we will bin the gaps by the individual tree, to make an initial estimate of $N(M_\mathrm{particle})$, the number of (Pal-5 like) streams we would need to rule in or out a specific mass of warm dark matter(or CDM) at a 95% CI or $3\sigma$.
* To speed up calculations, we used the shell theorem further, only numerically integrating flybies when a stream-point is touching the subhalo, that is, when 
$$ r^2_\mathrm{subhalo} \geq b^2 + \frac{y^2 w_\perp^2}{w^2},  $$
between
$$ \frac{- \frac{yw_\|}{w} -\sqrt{r^2_\mathrm{subhalo} - b^2 - \frac{y^2 w_\perp^2}{w}} }{w} \leq t \leq  \frac{- \frac{yw_\|}{w} +\sqrt{r^2_\mathrm{subhalo} - b^2 - \frac{y^2 w_\perp^2}{w}} }{w},   $$
which can be derived by applying the quadratic formula to the impact parameter formula(I think). 
Calling these (-) and (+) solutions $t_\mathrm{lower}$ and $t_\mathrm{upper}$ respectively, we can then fully integrate *any* (spherical) mass profile as a point mass, outside of a finite region. That is, 
$$\Delta v_{y} =\Delta v_{y, \mathrm{point}}  + \int_{t_\mathrm{lower}}^{t_\mathrm{upper}} \frac{-G M_\mathrm{enc}(r)(y + w_\| t)}{((y+w_\| t)^2 + (w_\perp t)^2 + b^2)^{3/2}} - \int_{t_\mathrm{lower}}^{t_\mathrm{upper}} \frac{-G M_\mathrm{point}(y + w_\| t)}{((y+w_\| t)^2 + (w_\perp t)^2 + b^2)^{3/2}},  $$
and similarly for $\Delta v_x$. The point formula can be found in the Paper I section, and the (quite involved, but carefully checked) finite forms can be found below.
![Screenshot 2024-08-13 at 9.20.47 PM](https://hackmd.io/_uploads/Hyl8W2K50.png)
![Screenshot 2024-08-13 at 9.21.01 PM](https://hackmd.io/_uploads/r1rU-hKqR.png)


### To do
* One or two final bugs need to be caught.
* rename f in the paper(maybe to $\tilde{\rho}(\rho)$ or something?). Probably for paper 1 too.
* Describe the filters we employed in galacticus(math not written out yet.)
* Then, the plots need to be finalized, and we think carefully about the "# of pal5s(WDM mass)" prediction, and how to tastefully nod towards the future( can I do this more now? Can I edit the introduction to the paper now? Can/should I read up on WDM now, and just rewrite the first paper? Alongside unit tests, this document, paper 2 calculations, and slides for group meeting, all of this is a high priority (oof).)
* Finally, then we finish this up(paper draft written up until results sections)
    * Then edit it alongside Andrew,
    * Send out locally for feedback,
    * Submit,
    * Handle  reviewer comments



## Paper III: SIDM
### Goal
* This follows the same framework as papers I and II, but for and SIDM subhalo population.
* Main computation improvment is that impact parameter is no longer calculated as the minimum of a linspace of $\phi$ values along the stream. Instead: 
$$ \vec{B}(\phi) = \vec{r}(\phi) - \frac{\vec{r}(\phi)\cdot \vec{v_0'}}{v_0'^2}- \left(\vec{r}'_0 - \frac{\vec{r'_0}\cdot \vec{v_0'}}{v_0'^2}\right)$$
$$ b = \left|\vec{B}(\phi_\mathrm{min})\right|,$$
$$r_0\sin(2\phi)+ \frac{2c_y\cos(\phi)}{\cos^2(\theta)}= 2 \sin(\phi)(c_x + c_z \tan(\theta))$$
$$c_x = r'_x \cos^2(\theta) - \frac{1}{2}r'_z \sin(2\theta) ,\ \ \ \  c_y = r'_y$$ 
$$ c_z= r_z'\sin^2(\theta) - \frac{1}{2}r_x'\sin(2\theta)$$
such that stream is in x-y plane. Since our (nonbaryonic) subhalo population is isotropic, this fixes 2 rotational degreed of freedom, and we can use the third to rotate such that $$ \vec{v}'_0 = \begin{bmatrix}
           \sqrt{v'^2_{0,x} + v'^2_{0,y}} \\
           0 \\
           v'_{0,z}
         \end{bmatrix},  \ \ \cos(\theta) \equiv \frac{v'_{0,z}}{\sqrt{v'^2_{0,x} + v'^2_{0,y}}}, \vec{r}'_0 ==???$$
where $\vec{v}_0'$ is the initial subhalo velocity in the impulse approximation and galactic frame, $\vec{r}_0'$ is the initial subhalo positon in the galactic frame. 
* coordinate system needs to be improved, but otherwise, this formula can be transformed into a 4th order complex polynomial, and thus has four turning points. We compute the zeros of the function above, and set 
$$ b = min(b(\phi_{0,i}))$$

### To Do
* Once Galacticus's SIDM feature is all set up, generating data involves:
    * Run sanity checks with small populations to familiarize myself with the code.
    * Read up on SIDM to understand the field we're working in.
    * Debug model if necessary(if my code has unit tests presumably the only place problems could occur is in SIDM mass profile or the subhalo population itself)
    * Generate full dataset. Perhaps generating data for 1 tree, then 40, then 400, then 4000 or something(loosely following the "increase in factors of 2" advice.)
* For heavy refactoring: 
    1. Learn how to use "timit" module 
    1. Figure out(or explore) using lambda for filters. Just feels like the right thing to do(I hesistate to say pythonic, but it is)
    2. Change deltaV to 2 separate arrays
    3B. Explore changing Deltav integrals into $a\int_{t_l}^{t_u}\frac{G M}{r^3} dt + b\int_{t_l}^{t_u}\frac{G M \times  t}{r^3} dt$, and see if this speeds things up
    4. Port in all 8 separate MPI files rather than combining
    4B. (and see if it makes sense to only read in nonMain/isolated subhhalos. Like make main and isolated the first datasets I read in, then magicIndices the undesirable indices away.)
    1. Port out data into new dataset(under 'Outputs'?) rather than 'Outputs/Output#/nodeData'.Weight by *output time* attr not (i-1))
    5b. Try to figure out this filelock business. Start with test data, only like 1 tree and like 100 timesteps, and go up from there. 
    1. fix the stupid unecessary transposes in 'doRotations.'
    1. Add documentation to all the x and y velocity kicks to make sure the signs stay right.
    1. Ugh  deprecation warning on the regex? 
    1. Modify all subhalos to be in second axis? (ie saved as [:, np.newaxis]). Maybe use third axis for position/massProfile internal dimension.  
    1. https://materialsproject.github.io/fireworks/ ? 
    1. Fix bug where pytest said "no tests ran" under successful conditions? Probably in the documentation or that coding video I watched. 
    1. make rotations using from_euler?
    1. get rid of sys.argv[2] from NFW.py arguments
    1. rename(refactor name of) NFW.py and move most functions to a repository
    1. rm combineGalacticus.pbs( double check with andrew that this will still be in my git history if I don't somehow 'git drop'(git rebase -i drop) all 200+ commits with this file saved.
    1. only use 1000 timesteps, get rid of for loop and '0', '1000' etc folder in log files. Delete all log files where this exists currently.  
    1. Move all paper 1 files into a /CDM/ directory. Get delete/mv statements to work from submitMaster.pbs(and think if there's a better way to do this. Maybe use a separate master file for each paper?)
    1. Auto delete log files everytime I regenerate stuff. Maybe think about how to reorganize log files? 
    1. get aliases for the most commonly used folders?
    1. delete erkal/plummer/nfw code once we're done with paper 1  comments.
    1. need to make a modify.xml file for SIDM.
    1. make clever way for job names to change automatically? (ie so I don't have to change the name of "postprocessing" every time). 
    1. Make model and optional keyword in accel?  
    1. Delete some unnecessary datasets in paper 3, like the million of velocity variables? And,  don’t bother merging .hdf5 files.( could already be on this list.)
    1. Can I turn ‘StellarStreams2’ back into stellar streams? Could take some work to fix symlinks, hard links etc
    1. Make uniform names for ‘treeNumber’ and ‘rotations.’ Doesn’t matter which way I go.
    1. change “boolean array”(in deltapsi- which also needs to be renamed) and the equivalent in getCount to be the same. It doesn’t matter which 
weight probably doesn’t have to be in ‘countDict’ in getCount()
    1. In paper 3 refactoring, track all the nonsense about rotations and stream length as early as possible so I can forget it.
    1. Can I count gaps in post processing? Get them at f=.9  and gap size =.1, then I can clean this further in the graphing. I’d have this for every model and it would simplify everything greatly. (It'll be interesting to see how much each of these takes out, and how different things are from the "rough cut.")
    1.Rename delta psi
    1. Delete log files and stuff after use? Idk if I do it when I rerun or what, but I should do something about tis.
    1. definitely rename every file like “submit.pbs”
    1. automate this main submit cycle? 
    1. alias for transferring graphs and files back? Would need to be on my local machine(maybe for logging in to clusters too)






* Compare number of gaps created by SIDM, CDM, and (certain masses of ) WDM. We(or at least I) will have to think a little bit about how to compare between each model pairwise. But a problem to face when we get there. 
* Getting the data out involves:
    * Write up results(plots will certainly include the run of the mill selection for SIDM, then perhaps figures comparing SIDM to both WDM and CDM. What are the relevant "knobs" to tune SIDM models?)
    * Edit with Andrew
    * Send out for local comments
    * Submit
    * Address reviewer comments if given feedback.

## Paper IV: Elliptical Streams and Baryons
### Goal
* The first 3 papers apply this semi-analytical to multiple dark matter candidates, but they do not improve the underlying model much. This is fine, but ultimately this all must be take na bit further.
* This model has been idealized by assuming flat rotation curves, no baryons, circular stream orbit, and a lack of consideration of edge effect(I'm not sure if any paper has treated gaps sourced at the edges of streams.)
    * Other improvements we defer are:
        * nonzero stream width(ie stream warmth- currently only considered through $\Delta v$ filtering),
        * gap infall via stream warmth model of gaps
        * curved flyby orbits and a relaxation of the impulse approximation(for larger, slower subhalos)
        * and perturber triaxiality. 
    * These will be doled out through the next several papers. 
* Here though, baryons are relatively easy to include. Some monte carlo fitting is necessary to get this physics right in galacticus, but then rotation curves will be generated dynamically for each tree's host halo, and this will also have some effect on the subhalo population. 
* Some streams are incredibly eccentric(Pal-5 would have a Keplerian eccentricity of 0.5). This not only affects where the stream is(generically, subhalo population changes with radius), but also gap growth. 
* Inclusion of baryons limits the Milky Way rotational symmetry to 1-dimensional(about the z axis), so this paper moves towards realistic modeling of specific streams in the sky.
* 7 parameters are necessary to spatially locate the stream, beyond rotation curves: $[c_x, c_y, c_z]$ govern the orientation of the stream-orbital plane relative to the x axis with (first) pericenter in the x axis. Then, $, E,\  L_z,\  \&\ \theta_\mathrm{min, max}(t)$ govern the shape of the orbit itself. 
    * $\vec{c}$ and  $\theta_\mathrm{max}(t)$ will come out of observations. 
    * E and $L_z$ can be determined from a knowledge of the potential, and the orbit's pericenter and apocenter:
    $$ L_z = r_p r_a \sqrt{\frac{2(V(r_p) - V(r_a))}{r_a - r_p}};\ \ \ E = \frac{L_z^2}{2r_p^2} + V(r_p)$$
* (assuming the usual $V(r\rightarrow\infty) = 0$)
* For keplerian (point source) potentials, noncircular orbits are stricly elliptical:
$$ r(\theta) = \frac{r_0}{1+e \cos(\theta)}.$$
* For general rotation curves, there is no exact form, but for $e <<1$,  these noncircular orbits  can be approximated as $$\frac{r_0}{1+e \cos(\gamma\theta)},$$
* Generically, they must be derived numerically from the well known orbit equation: $$\frac{d^2 u}{d\theta^2} + u(θ) = \frac{\partial_u \Phi_\mathrm{gravity}}{L_z^2}$$
* Gaps will distort as the stream stretches along it's orbit. Edge effects will occur because streams are not modeled as full circles. A more full part of the galactic subhalo population will be sampled as the stream traverses from pericenter to apocenter.
*Following the logic of paper III, we calculate the angle along the stream where b is minimized, we  solve:
$$r(\theta) r'(\theta)\left(1 - \frac{v^2_r}{v^2}\right) - r'(\theta)\left(\cos(\theta)c_x +\sin(\theta) c_y - \frac{v_r \vec{v}\cdot\vec{c}}{v^2}\right)  - r(\theta)^2 \frac{v_r v'_r}{v^2} + r(\theta)\left(c_x \sin(\theta) - c_y \cos(\theta) - \frac{v'_r \vec{v}\cdot\vec{c}}{v^2}   \right) = 0, $$
$$ \vec{c} = \vec{r}' - \frac{(\vec{r}' \cdot \vec{v})\vec{v}}{v^2},\ \ \  v_r = \vec{v} \cdot\begin{bmatrix}
            \cos(\theta) \\
           \sin(\theta) \\
           0
         \end{bmatrix},$$
numerically, using our single rotational degree of freedom to set the (initial) pericenter in the $+\hat{x}$ direction. For a keplerian elliptical orbit($r(\theta)$ governs the orbit), this is a 6th order equation. For small perturbations from a spherical orbit in any central potential, this will be a transcendental equation of order $4 + 2\gamma$, and it's zeros are solved numerically. As in paper III, we compute the impact parameter of each 0, but we also include $b(\theta_\mathrm{min})$ and  $b(\theta_\mathrm{max})$ due to finite edge effects. Generically, not all 6+ zeroes will occur in the finite arc the stream occupies.
* note!! Need to "pitch yaw roll" r and v here. 
* Since $\Delta r(\theta)$ is no longer analytically solvable, we now have to move the numerical analysis up one level, and say 
$$ \int_{lower}^\theta r(\theta')^2 d\theta'  + \frac{(4 - \gamma ^2)\Delta v_y}{\gamma^2}\int_{lower}^\theta r(\theta')^3 d\theta'  + \frac{4\Delta v_y}{\gamma^2}\int_{lower}^\theta r(\theta')^3\sin(\gamma \theta') d\theta' +-\frac{2\Delta v_x    }{\gamma^2}\int_{lower}^\theta r(\theta')^3\cos(\gamma \theta') d\theta'= L_z t_\mathrm{age\ of\ gap}   $$


### To Do
* Find $\vec{c}$ and $\theta_\mathrm{min, max}|_\mathrm{z=0}$ from observational data.
* Finish coding changes to 
    * i)the impact parameter(need to abandon 2 phase approach and include endpoints. Decide if I filter by local minima/maxima. Sanity checks) 
    * ii)Rotating subhalo population?
    * iii) Orbital parameters
    * iv) numerically optimizing $\dot{\theta}$
    * v) Pull common functions into a new file with NFW.py so all code is up to date. 
    * vi) Modify stream_kick.F90 and stream_impact.F90(math to come- i had it all worked out months ago but I forgot it.) This will slow things down greatly when we apply to multiple streams(unless we get creative, or rerun galacticus for each stream.) But, because galacticus.exe runs nearly as fast without the filters(it still has to calculate everything whether it saves it or not), if we skip the merging(or find some way to speed it up by allocating more memory, which is unlikely), then we can perform the more stringent version of the stream_kick and stream_impact cleanings(for just one stream) as soon as we load the files in. If we do this before we merge the datasets, it will probably be fairly manageable data-wise. Need to think whether it's better to clean each dataset as it's read in or just the whole MPI file after reading in each dataset. The uncleaned .hdf5 files are ~10x bigger, so if we run 8 cores, I suppose things run almost as quickly. Certainly *some* subhalos can still be removed in galacticus, at least when we have 4 streams(when we have many many more, who knows.)
More general refactorings: 
    1. Try out Cython or pypy to see if this speeds code up? 
    1. See if I can expand the terminal in vscode so I can see several thousand jobs as they’re running.
        2B. Learn how to check when a file was created in VScode(like timestamp)
        2C. Look at whether the (base) part of the cluster says venv or not and what that means
    1. Think more carefully about what y values to use. Maybe we can get away with less? To test if gaps can move away from the center, do a really small linspace and see if we keep more gaps
    1. In paper 4, refine the b meshgrid with successive iterations to find where interpolation stabilizes? Should I do first order, or third? Also? Verify against circular case and brute force.
    1. Paper 4: how many more subhalos to account for finite stream length? Avg length of stream /360? Add factor of ~20% to be safe?(we’re on the ultra low end here)
* We'll need baryons soon
* Run some test simulations to ensure all this is working properly. Perhaps compare gaps created to circular case for a few subhalos.
    * then generate data with 1000 timesteps, 20k trees and 80 rotations about the z axis for CDM, certain WDM models, and SIDM.
* Plot density of the stream as a function of angle without gaps(ie, how does overdensity change?)
    * Plot evolution of one (or a few) gaps compared to circular streams(easy to import old code/use it instead.)
    * Histogram of gamma values by main tree? 
    * Plot basic subhalo parameters(w, r, basic mass, bound mass) compared to circular situation(probably just for CDM if CDM-WDM parameters look pretty similar)
    * Plot gap size for CDM, WDM(maybe current limit, something incredibly low like 4kev, and *maybe* something higher like 15 or 20 kev), and SIDM(not sure how models vary.)(decide on datasets soon-ish. this isn't that far away(if I can keep the damn bugs at bay. Praying unit tests will save me.))
    * Same thing for gap sizes for each model. 
    * count table just like in paper 2(for models listed above). Maybe want circular and ellpitical as 2 separate columns in the same table. 
    * Perhaps bin a histogram for number of gaps in a single tree like in paper 2(most of these should be very easy to code up.)
    * I don't really want to do any "3 phases of gap growth" forensics, but I can if we think it's necessary.
    
    * Use the new method of plotting to plot all timesteps simultaneously(likely already fixed in paper 3). 
    
* Write this all up, edit the paper, send it out for local comments/code credit, submit, and handle reviewer comments.

## Paper V: Strengthening test power and applying to multiple streams
### Goal
* The goal of this paper is to include more test, specifically gap size, line of sight velocity, and behavior about the z axis(it's commonly said that velocity kicks cause the orbital plane to shift, and cause oscillations about this new plane)
* The idea is, if we carefully marginalize over all the other tests, this can tell use far more information than just gap size can. For instance, maybe light, slow moving subhalos(ie $M\sim 10^5 M_\odot$, $v \sim 50 km/s$) have an identical gap size to a faster, further away $10^8 M_\odot$ subhalo, but different line of sight velocity. While speculative would allow us to develop a "fingerprint" of gap creaters, and, if we can identify what gaps come from low mass subhalos, this could place much stricter constraints on WDM models(who lack these subhalos.)
* Moreover, it's possible that additional information is slim between different mass tidally stripped subhalos. However, perhaps a cored SIDM model, large molecular clouds, or "non-flyby" perturbers such as other dwarf galaxies and the bar have very different features. 
* There's no way to know until we perform this experiment(and catch up on the literature of what's been done), but, if we believe dark matter is very hard to constrain, the power of a stellar stream test likely depends on incredibly minute details.
* Finally, we have only worked on Pal-5 up until this point, largely for ease as much as anything else. We have tested how gap predictions change with radius(getting data for Pal-5's pericenter and apocenter as well), but our stream model was too idealized to really justify repeat work. However, the only way this test succeeds is if we apply it to *all* streams, so generalizing what's been done is a crucial step. 
$$ F(r)= \ddot{r} - r \dot{\theta}^2 - r \dot{\phi}^2 \sin^2(\theta)\newline$$ 
$$r \ddot{\theta} + 2 \dot{r}\dot{\theta} - r\dot{\phi}^2 \sin(\theta)\cos(\theta) = 0$$
$$r\ddot{\phi}\sin(\theta)  + 2r \dot{\theta}\dot{\phi}\sin(\theta) + 2 \dot{r}\dot{\theta}\sin(\theta)= 0 $$
$$ \theta \approx \frac{\pi}{2} + \Delta\theta,\ \ \  \dot{\phi} \approx \omega + \Delta\dot{\phi},\ \ \   r \approx r_0 + \Delta r$$
* All of this leads to the incredibly dissapointing result that 
$$\Delta z(y,t) = \frac{\Delta v_z(y)T}{\gamma} \sin(\gamma t/T)$$  
* at first order. However, it is unphysical to expect that these fluctuations continue indefinitely without any damping. The most likely source is the inherent velocity dispersion. I haven't had time to think through this much, but 2 likely forms (that may be equivalent) are something like 

$$\Delta z(y,t) = \frac{\Delta v_z(y) T}{\gamma} \sin(\gamma t/T)e^{-\lambda t},$$
or 

$$v_z(y,t) = \Delta v_z(y)  \cos(\gamma t/T) + \lambda f(y).$$
In this idea the timescale $\lambda$ is somehow dependant on the intrinsic velocity dispersion. In the second, I'm building on Tong's notes for statistically random fluctuations(and a class I took on the statistical physics of the stock market), where f has the form 
$$ \left< f(y)\right> \equiv 0,$$
$$\left< f(y_1) f(y_2)\right> \sim  v_\mathrm{disp}^2\delta(y_1 -y_2),$$
where y is (one of the many terrible) parameterizations of stream position. I should probably change this to L at some point. But, am I completely crazy, or does this not dampen ocillations? 



* Armed with this equation(in theory), we can now compute that 
$$v_\mathrm{line\ of\ sight} = \Delta v_z \cos(\gamma t /T) \cos(\beta_z) + \left(\frac{2r_0\Delta v_y(y)}{\gamma v_y}\right)\cos(\beta_r) +\frac{L_z}{r(\theta)+\Delta r(\theta)} \cos(\beta_\theta) $$
$$v_\mathrm{line\ of\ sight} = \Delta \dot{z}(t)\cos(\beta_z) +\Delta \dot{r}(t)\cos(\beta_r) +\Delta\dot{\theta}(t) \cos(\beta_\theta) $$
* lots of questions here: is the z equation (modulo units) right? Or is $\dot{\phi}$ supposed to be the depending variable in Sin()?  Is y included in the line of sight velocity? We have to dampen this, right? Or do we really believe the z oscillations persist forever(there is no air resistance after all.) Do the other velocity equations get damped? We can use $\theta(t)$(in the old notation that needs to change. We should be smart in papers 1 and 2 about how we use theta and phi) to get y velocity. Are we assuming it's at a maximum, or do we have to normalize with a 1/2 to account for the randomness in the period of z-oscillation. Ofc we have to bring in the complications of paper 4 here. Is there redshifting to compare to experiments? How, **quantitatively** can we codify the z oscillations? is the whole z oscillation in phase? 
* And, how do we pull in gap size? Is my idea from before right?
* Which other streams are we picking? We definitely need GD-1, but we should think reasonably carefully about which other two to pick. Maybe 2 more from erkal's 2016 paper? Ultimately I'm just so incredibly behind on the literature, I just need to catch up and I won't have so many gaps. 
 



### To Do
* Really ensure the z(t) equation is right. 
* Solve the coupled differential equations to second order. Maybe not necessary, but good to be thorough(and I'm kinda curious). 
* Refine Line of sight velocity equation. $\beta_i$ should be pretty easy to calculate, but I'm not *positive* that the overall equation is correct, and we need to think whether it needs some sort of damping term. 
    * $\beta_i$ may change with y(depending on whether $|\vec{r}_\mathrm{stream} - \vec{r}_\mathrm{earth}| >> l_\mathrm{stream}$ or not).
    * If all $\Delta \vec{r}$ components really do vary over time, we might have to marginalize over all phase. This current work is(by design) a little more abstracted, but, by the time we actually compare to data, this needs to be done well.
    * Once this is all figured out, I need to code everything up. If I refactor how I calculate $\Delta v$, I can get these integrals "for free" because they're the same as the x integrals. Perhaps this would be a good time to switch to the $\int dr$ formula in "the void"(or maybe not.)
    * Need to track $\Delta r(t)$ and $\Delta z(t)$. Should be able to add in 2 more functions after getDeltaTheta(), but could be some nuance here(work it out in latex first- maybe $\Delta r(t)$ and $\Delta z(t)$ depend on f somehow, even to first order.)
    * Decide whether to calculate v_los in postprocessing or graphing code **before** I run a large sample. Maybe I want to move *all* the deltaPsi and count stuff into postprocessing? No, unless I track every dataset for every graph(which is liable to change), this wouldn't work. Still, it feels like this workflow can be simplified somehow. Maybe I put all datasets into a list, so I don't have to iterate so much. Yeah, like one big array that goes through the count stuff and that's it. Is there a way to bin for multiple graphs as the same time?  
    * Can bin gap size by tree(and number of gaps) in the graphing code.  Treenumber and rotationnumber, the same for the binning in paper 2, are already tracked.
    
* After deciding on other streams, find the orbital parameters for them. Again, this should be fairly simple if I can figure out how to do it for pal-5.
    * Also, need to think how all these equations are modified for elliptical streams.
    
* Once we include the x-y plane code, test, and rerun for our standard sample size, the other challenge is to properly marginalize all of these variables on eachother.
* The stream parameters inputted in paper 4 are modular, so extending to other streams just requires rerunning the postprocessing(not galacticus.exe) with these other stream orbits. 
    * Given how quick the postprocessing runs now, this should be simple. 
* Decide whether to use the same datasets(ie WDM masses) as paper 4 or not. 
* Then write the paper, edit, local comments, submit, and reviewer comments.


## Paper VIA-VIB: Basic math for other perturbers
### Goal
* Depending on how much this math can be reworked from known results, maybe this can all be written in a paper(ideal.) However, it seems likely that 2 papers are necessary for perturbers(between relaxing impulse approximation, non-linear orbits, multipole expansion, coupled equations, even reworking the whole code(maybe) so that different gap contributors can "interact"(needs to happen at some point, just a question of when.))
* But, gaps are also created by the LMG, the milky way bar, LMCs, and I believe at least one other source.
    * I need to read up on all of these, and honestly so much of the literature. The closer we get to experiments, the more glaring this blind spot becomes. 
* To model these new perturbers(and perhaps model subhalos better), we must make a number of changes: 
    * First, we must relax the impulse approximation to allow for interactions on astronomical timescales. While I haven't worked out the math for this yet, I think we stop integrating the velocity kick entirely. 
    * Second, we must not assume sphericality, and expand all perturbers in a multipole series. I'm working out the basic math for this, and then we can figure all what's what. Pretty much every gap source rotates as well, so we'll have to keep this in mind/ take account. Do we have semi-analytic results for *sub*halo triaxiality? Or just host halos?(I assume the most massive thing in a system can't be stripped by much.)
    * Third, for extreme perturbations, such as the bar, I think we have to couple the orbital changes(caused by te velocity kick) *back* into the $r(t)$ (or just r) of the velocity kick. Maybe this is where switching to $\int dr$ would be more valuable, but that would change a lot of the math I've worked out, and the value remains to be seen. 

![Screenshot 2024-08-13 at 7.06.37 PM](https://hackmd.io/_uploads/SJ_d-5FqR.png)
![Screenshot 2024-08-13 at 7.06.44 PM](https://hackmd.io/_uploads/ry_dZ9tc0.png)
![Screenshot 2024-08-13 at 7.06.54 PM](https://hackmd.io/_uploads/SkOOW5FcA.png)

$$\frac{d^2u}{d\theta^2} + \gamma^2 u(t) \approx \frac{-2 u(t)^2}{L_z}\sum_{l=0}^{3\mathrm{ish}}\int_{ \sim11\mathrm{Gyr}}^{t}\frac{Gm_{l;\ \mathrm{bar}}  Y_{lm}(\theta(t'), \phi(t')) \hat{R}_\mathrm{g c}\cdot \hat{y}}{R^{2+l}_\mathrm{g c}(t')}dt' $$ 

### To Do
* Work out the basic multipole expansion examples I have in my head. 
    * See why expanding in the force doesn't give the $Y_{lm}$ series. Maybe I need to actually expand $1/r^3$ rather than being cute?
* Look at papers (like Amarisco 2016). 
    * Try to remember what that last gap contributor was (I'm sure there are more, but this is the type of thing where we write a paper claiming to include all sources, then the community "gently" reminds us of our shortcomings. Saying something incorrect is probably the fastest way to crowdsource information haha.)  
* Figure  out how to handle rotations(and in principle sphericalization for subhalos? Would this all just be handled in galacticus?)
    * Rotations should be easy to treat(when I write this all out correctly, there should be a vector indice to "dot" into.)
    * Figure out what the extra datasets to track in galacticus are. Again, this is incredibly granular, but that's the job if we're gonna get where we're trying to go. 
* Putting in non-straight orbits shouldn't be *too* too bad, but I think we have to be tasteful about when we apply this and when we don't(or if a gradient is possible.) Again, if we weren't going to have some panache, there's absolutely no reason not to just "N-body" this to hell.
* The bar definitely feels like it would be in the second paper. Again, as andrew has said the analytical form(ie multipole expansion?) of this potential is well known. But, if we have to couple the equations of motion beyond first order, that's gonna be fucking hard. *And*, to do that right, we have to start tracking all gap contributors by tree number chronologically, rather than in isolation. That wasn't supposed to happen until paper 7, but, if we're moving i)*Stream Infall*, and ii) *Tidal Heating* up to the plate, that paper might start bursting at the seams. 
    * We could probably get away with i)Triaxial subhalos, ii) GMCs, iib)whatever that other GMC-like gap generator is, and iii)*maybe* the LMC in a first paper( that doesn't treat each contributor as interaction.) 
    * Then, in the second paper, doing these extra changes for the bar(and applying them to other sources as well) feels like a nice evolution. And, like anything, we just have to "do it", write a paper, and make a ton of mistakes. So, I kind of like the idea of having 2 parts to this paper, to give us room to adjust whatver wasn't working the first time(maybe this needs to come after, like maybe we publish 6A, 7A, 6B-C, 7B[if necessary]). IDK, that makes sense to me, but I could see a reader getting fed up with these apple-eqsue jumps(Iphone X being the  9th Iphone).
* More to say on all this, and math. 
* And we have to figure out if my idea for tracking the LMC is right, whether we'll track other dwarf galaxies, where to find GMC data(easy, but we probably want to wait until we're close to it's current- very YAGNI[you aren't gonna need it]), figure out if bar info is in milky way spheroid, etc. Think a little bit about the andromeda galaxy(maybe later.)


## Paper VIC: Inherent anisotropies
### Goal
* Trying to model the inherent inhomogeneities in the stream really( I think) entails a full model of stream formation. Again, I have absolutely no idea what's been done already, but my naive, first pass idea is this:
    * What would cause the density of the stream to vary? Well, lets start at the source. I'm *sure* dwarf galaxies and globular clusters have some width $\sigma$ to the matter distribution(ie a given region is not likely to be the average density of the whole dwarf galaxy. If all NFW halos have subhalos, and these subhalos can host matter clumps [up to some point- I know there's that whole "missing satellite problem". I sure hope we find out who stole them all!], then it's obvious that certain regions would be more dense. I don't really know how to put that in a pseudo-gaussian form, but my gut feels that it's possible)
    * This could some sense of whether tidal forces "come up empty" or not in a given chunk of time. The problem, however, is that we have no idea what the progenitors are for most streams.
    * Breaking this project up into 2 parts(at least mentally as a first pass), for the first piece, we model a stream with a known progenitor, like say Pal-5. As Palomar 5(I think that's the right name for the progenitor) moves on a presumably known orbit, the tidal forces it feels change with radius. These tidal forces are (presumably) knowable, and have some radius dependance(depending on host halo $M(r)$ I'm sure). Thus, we can calculate i) A radius-dependant variable dripping rate $A\left(r(t)\right)$, and ii) Statistical fluctionations on this of the form $B(\sigma)$. Forgiving(for now) the terrible notation/ variable choices, we would find something like 
    
$$\frac{d\rho_0}{dt} \sim A(r_0(t)) \times B(\sigma),$$
where $r_0$ is not a constant, but signifies an unperturbed orbit(your standard non-circular orbit in flat(ish) rotation curves.)
* To be hyper aggressive, we could even modulate in Palomar 5's triaxiality, and any known angular density fluctuations, for something like 
    
$$\frac{d\rho_0}{dt} \sim A\big(r_0(t), \theta_\mathrm{int}(t), \phi_\mathrm{int}(t)\big) \times B\big(\sigma[\theta_\mathrm{int}(t), \phi_\mathrm{int}(t)]\big),$$
(using '[ ]' to clarify a mess of dependent variables, not any sort of of special functionality.) 
* Then, some simple 1-3 parameter model could be tuned up(again, I imagine and hope some of this has already been done), and tested against streams with known progenitors. A second "prong" of this step would be to do the same thing with Globular-Cluster-progenitors, but I know very little about those. 
* For the second step, we then modulate over the ratio of expected dwarf galaxy vs globular clusters of hosts(maybe as some complicated function of radius or L), the likely mass of each progenitor(presumably there's a range), to statistically pretend we know what every progenitor is
    * I realized, at least for dwarf galaxies, there should be some dark matter stripped along with the stream. I have absolutely no idea why that would be relevant, but there could be some value in realizing that streams are (potentially) heavier than they look. 
### To do
* *If* this model is actually right(it likely isn't), then I think the plan would be to see what's known in the literature, model whatever gaps we need to fill in, and then get the gap population. The $d\rho/dt$ model definitely needs to be better too, but then I guess we make a bunch of predictions, maybe for more streams than we've seen before. Maybe we test this model against some known progenitors(and data)to see how we do, and, even if we don't increase the number of streams we apply the full model to, we could still apply this piece of things. 
    * Again, do these gaps look different somehow from flybys? Is there a different signature from GCs vs globular clusters? Will we have to figure out what $\Delta L$ is between the progenitor and the stream itelf? If we could(and this is crazy ambitious) genuinely tell a GC gap from a Dwarf galaxy from the other sources, we would maybe have insight well beyond just dark matter substructure(which is of course the goal, but those direct detection experiments still explored indirect detection and other constraints when they thought they had a signal.) 
    * Presumably gaps will be much more uniform than for flybies(if the 3d model really does go like $\delta b / b$.) This, again, suggests our  test may be more powerful for substructure the smaller it gets(on some level/relative basis, the way an ant is techically "stronger" than a human), which is exciting. Again, I'm making this all up as we go, but if we can get a "fingerprint" for each gap contributor, our power goes up significantly( I don't *think* this is the case, but in principle if no DM models gave the correct subhalo gap population, that could place constraints on the milky way halo mass. Again, that feels circuar(because we'd have to assume a model), but sometimes there's something there in these moments.)
* To plot, we would want some running contribution of gaps for a few favorite streams, histograms on the type of behavior globular clusters and dwarf galaxies create, and probably some other things.
    * Wait *would* there be a dark matter halo around progenitors of mass $\sim 10^4 M_\odot?$ In CDM sure, but in WDM models, we wouldn't have substructure at that scale right? This must tie into the missing satellite problem somehow, but I have no idea how that was resolved(if it was).
* After all these graphs, as usual, we write, edit, send for local comments, submit, then deal with reviewer comments. 
    * I would probably end up reading a bit about the progenitors to write the introduction well(and model I'm sure)- I have so  much reading to get to before this, but it wouldn't hurt to get a jump start on this eventually. 



## Paper VII: warm, wide streams
### Goal 
* Okay, so papers I-VI[a-c] all make huge steps forward, but they treat steams as 1 dimension, basically without size or velocity dispersion. We (probably) want to fix that. 
* The most obvious piece of this would be to treat streams as 3d. We would then treat each stream as a collection of mxmxn points (m along the cross section, n along the length), and observe how each event modifies these points. We're bordering on an n-body simulation, but with all the speed, elegance, and statistical power of something semi-analytic.
* A "front of the envelope" estimate(ie so back of the envelope we've flipped it back around) suggests that 3d effects are of order $\delta b/b$, that is, stream width divided by impact parameter. This suggests that these effects may only be noticeable in subhalos with a small impact parameter(corresponding to a small subhalo radius), leading us towards the many, small gaps/interactions with low mass subhalos(if they exist!)
* This whole framework may be futile, but, assuming for the minute that there is value, let's work out some math. The "0th order" equations(ie circular streams, simple rotation curves, spherical host potential, small kicks) are something like:
$$ \delta\dot{\theta}(\delta r, \delta z) = \delta r \bigg[\frac{- \dot{\theta}(y, t)}{r_0} + \frac{-(4 - \gamma^2) + 4\cos\gamma\theta}{v_y\gamma^2 }\frac{d \delta v_y}{dr} -\frac{2 \sin\gamma\theta}{v_y\gamma}\frac{d \delta v_x}{dr}\bigg]  $$

$$+\delta z \bigg[ \frac{-(4 - \gamma^2) + 4\cos\gamma\theta}{v_y\gamma^2 }\frac{d \delta v_y}{dz} -\frac{2 \sin\gamma\theta}{v_y\gamma}\frac{d \delta v_x}{dz}\bigg],  $$

$$\delta v_y = \left( b_x \mathrm{sign}(b_x) \delta r + b_z \mathrm{sign}(b_z) \delta z\right) \left[\int_{-\infty}^\infty\frac{G M'(r) (y + w_\| t)}{r^4} dt -3\int_{-\infty}^\infty\frac{G M(r) (y + w_\| t)}{r^5} dt\right]$$

$$\delta v_x = \left[\int_{-\infty}^\infty\frac{G M'(r) (b_x + w_x t)}{r^4} dt -3\int_{-\infty}^\infty\frac{G M(r) (b_x + w_x t)}{r^5} dt + \int_{-\infty}^\infty\frac{G M(r)}{r^3} dt\right] \times$$ $$ \left( b_x \mathrm{sign}(b_x) \delta r + b_z \mathrm{sign}(b_z) \delta z\right),$$ $$ r = \sqrt{(y + w_\| t)^2 + w_\perp^2 t^2 + b^2} $$
* The signs of some terms may be wrong, and, the $\delta r / r_0$ term is probably negligible in all but the most pathological cases. I suppose, what other changes in papers I-VI(really IV-VI) do we have to take into account?
    * For more realistic orbits(perturber dependent), we would change r(t) (but the equations above would stay the same)
    * there may be some interesting connections if we rewrite this in the $\int dr$ form, and there feels like some connection to the $\frac{dv_y}{dy}$ formalism. Again, turning this into a stupid $\int dy$  integral could bear fruit.
    * For  
* Put in tidal heating, infall, the spur, 3d continuity equation, stream-material being lost, etc in here(if desired). This may turn paper 7 into 7a and 7b (hopefully no 7c though- I want to graduate!)

### To do
* The math is already worked out(in broad strokes), and can be done analytically with no extra computation time. This is crucial, because otherwise semianalytical work would take $\sim20 \mathrm{x}$ longer to run, and be borderline infeasible(remember, we must, in the end, post process 120+ streams!). (include equations here)
* If not done by now(perhaps this would be necessary for 6B), the code needs to be rewritten to treat each stream as an instantiation of a class. Then, we can treat streams as collections of say, 5x5x100 points (100 being along the stream's length), and evolve each of these separately over the lifetime of the stream.
* Postprocessing would have to be broken up by tree, rather than by timestep, but this feels feasible. 
* Coding up this model feels quite easy, but the challenging part feels to be pulling out usable data. This could(optimistically) be a goldmine for new data signatures to add in, but understanding that takes a lot of thought. 
* Stream infall, governed by the warmth(inherent velocity dispersion) of the stream, could also be implemented at this time, as the two go hand in hand. 
* Look at overdone f>1 regions as well?
* At the very least, regenerating gap statistics must be done, but I think the goal is to work towards a final prediction on CDM, rather than qualitative features of this model.
* Once graphs are generated, as always, write, edit, local comments, submit, edit.

## The void
### Overview
* Here is where all the other (half baked) ideas we have are. The final goal is to make no go theorems for mond, and to see if we can fully rule out(or in) any dark matter candidates. However, there is both a myriad of side projects that could be formed here, but also improvements that may be necessary to make this model  work. Again, streams provide effectively the only new test that we *know* can probe dark matter, but margins are thin. I suspect every trick in the book will be necessary to make this model actually work. Here are some of the possibilities 
### Ideas
1. Compare to n-body simulations. 
    * Even if we don't do this for full gap statistics, certainly by paper 8, it would be irresopnsible not to compare back to, say, n-body mockups of realistic streams and perturbers. 
2. Tracking lower mass subhalos. 
    * We only track subhalos down to $\sim 10^5 M_\odot$ at present, but this is a cutoff inhereted from Erkal's work. It's not an unreasonable place to stop, but I suspect *some* usable statistical power can be gleaned from even lower mass subhalos. 
    * Ultimately, high enough mass Warm Dark Matter is effectively cold. However, if we *do* want to discriminate between WDM and CDM at masses $\gtrsim 34 \mathrm{keV}$, the only *hope* is in these lower ranges(because the models are literally indistinguishable above that)
3. Sub-resolution heating
    * Tied into the previous point, one other idea (courtesy of Ana) is to try and simulate tidal heating created by light subhalos. If this approach really can probe down to $4*10^5 M_\odot$ subhalos, we should absolutely include that range. 
4. Better contact with the data
    * I come from the theoretical side of things, and have very little contact with the actual experiments being performed. As I understand it, even if the CATS(Community Atlas of Tidal Streams) does fully standardize how stream-data is reported, there is still certainly missing data for some streams, differing observational bounds, etc. Trying to realistically come in contact with these limits(rather than just providing a range of plausible values, as we have), feels like a necessary transition point.
5. Primordial black holes? 
    * If I'm not wrong, these aren't fully ruled out yet. Once we have a powerful model, it feels trivial to just import some N-body dataset within the "ruled in" parameter space, change the velocity kicks for the mass profile(and certainly other pieces) for those objects, and generate gap predictions. This could be either done at this stage(probably better), or once we start making full predictions on the stream population. 
6. The spur, caustics, etc
    * All of these features(which I don't fully understand) seem to have a bevy of useful information. It seems key to bin over this data as well in the final predictions
7. Redo gap forensic data, explore gaps near the edge of a stream, try to better understand how $v_{y,\mathrm{max}}$ changes for truncated/nfw profiles compared to the simple point mass formula, generate gap predictions for a point mass and spherical shell as comparison, etc
8. See if we can better localize the maximum $\Delta v_{x, y}$ values for a general potential, or tabulate the results (write out equations for those.) Huh! The formula to find the maximum vy value is almost identical to the 3d stream stuff. I'll have to play around with this a little more. 
$$ \Delta v_{y, \mathrm{numerical}} =\int_{t_\mathrm{lower} }^{t_\mathrm{upper}} \frac{G M(r) (y + w_\| t)}{\left((y + w_\| t)^2 + w_\perp^2 t^2 + b^2\right)^{3/2}} dt\Rightarrow  $$
$$\frac{GM_\mathrm{tot} t_\mathrm{max} }{(y^2 + b^2 )^{3/2}}\left( y\int_{-1}^{1} \frac{ \tilde{M}(\tilde{r}(t')) }{\tilde{r}(t')^{3/2}}dt' + w_\| t_\mathrm{max} \int_{-1}^{1} \frac{ \tilde{M}(\tilde{r}(t')) }{\tilde{r}(t')^{3/2}}dt'\right), $$ 
$$ t_\mathrm{max} \equiv \frac{\left| \frac{yw_\|}{w}\right| +\sqrt{r^2_\mathrm{subhalo} - b^2 - \frac{y^2 w_\perp^2}{w}} }{w},\ \ \ \ t'\equiv \frac{t}{t_\mathrm{max}}, \ \ \ \tilde{M}(r) = \frac{M(r)}{M_\mathrm{tot}}$$
$$\tilde{r}(t') = \sqrt{\frac{w^2 t_\mathrm{max}^2}{b^2 + y^2}t'^2 + \frac{2 y w_\| t_\mathrm{max} }{b^2 + t^2} t' + 1}.     $$
The $M(r)$ behavior is complicated, even for an NFW profile. But, otherwise, this would be incredibly simple to tabulate numerically. Further modifications could be made to turn $dt' \rightarrow f(r) dr$ somehow(since t/t' seems like an artificial variable in all this.) Note that we have expanded the domain of integration slightly(specifically by $\frac{2 y w_\|}{w^2}$) to symmeterize, preventing the ratio $t_{upper}/ t_{lower}$ from being another variable to tabulate over.$\tilde{r}(t')$ is only a 2 parameter model of the form $\sqrt{at^2 + b^2 + 1}$, and it's not *too* hard to plug back in from there. 

The $\Delta v_{x,y}$ integrals can also be rewritten to sub out time. Writing $\Delta v_{y} = \int_{r|_{t=-\infty}}^{r|_{t=+\infty}}\frac{-G M(r)\left(y +w_\| t \right)}{r(t)^3}\left(\frac{dr}{dt}\right)^{-1}dr$,

we find 
$$t_\pm(r) = \frac{ -\frac{yw_\|}{w} \pm\sqrt{r^2 - b^2 - \frac{y^2 w_\perp^2}{w}} }{w},\ \ \ \left(\frac{dr}{dt}\right)^{-1} = \frac{dt_\pm}{dr}= \frac{\pm r}{w \sqrt{r^2 - b^2 - \frac{y^2 w_\perp^2}{w}}},$$ where we choose the (-) solution as the subhalo comes in from $r = \infty$ to $r_\mathrm{min} = \sqrt{b^2 + y^2}$, and the (+) solution as it goes back out. After some algebra, we find:


$$ \Delta v_{y} = \int^{\infty}_{ \sqrt{b^2 + y^2}}\frac{-2G M(r)y w_\perp^2}{w^3r^2\sqrt{r^2 -b^2 - \frac{y^2 w_\perp^2}{w}}}dr,$$
and a similar, slightly less elegant formula for $\Delta v_x$
Finally, in this mathematical push, we can find the y value where delta vy will be maximized(relevant for initial cleaning):
$$\frac{d\Delta v_y}{dy}= -G\int_{-\infty}^\infty \left[\frac{\left(M'(r)_\mathrm{enc}r - 3 M(r)_\mathrm{enc}\right)  \left(y + w_\| t\right)^2}{r(t)^5} + \frac{M(r)}{r(t)^3}\right] dt  = 0  $$
I tried to solve this for an NFW profile, and she got quite complicated. I have an irrational belief that the equation is solvable but it's certainly not easy, and is probably utterly useless(given both that M(r) saturates, and that tidally stripped profiles can lean orders of magnitude in either direction.)
Can we turn the dr integral into a dy integral? It's utter nonsense, but there could be something interesting there. I see connections in the math.
8D. I tried to convert the velocity kicks into a $dy$ integral, which is utter nonsense physically, but I've seen techniques like this bare fruit. The program fails because $r(r)$ is singular(very unsuprising). But, 2 results that may(*somehow*) have value are: 
$$t_\pm(y, b, r) \equiv \frac{-yw_\|}{w^2} \pm \frac{\sqrt{r^2 -b^2 - \frac{y^2 w_\perp^2}{w^2}}}{w}  $$

$$\frac{d t_\pm(y)}{dy}= -\frac{1}{w^2}\left(w_\| \pm \frac{y w_\perp^2}{w\sqrt{r^2 -b^2-\frac{y^2w_\perp^2}{w^2}}}\right)   $$
 Maybe this can be saved if we do something even stupider and find like $b(y)$, but I think the limits of integration become gobbledygook too. 
 
8E. I calculated the position and value of $\Delta v_{x, \mathrm{max}}(y)$ (for a point mass).
$$\frac{d\Delta v_x(y)}{dy} = 0 \Rightarrow y = b\left(\frac{-w \pm \sqrt{w^2 \cos\alpha +w w_\| \sin\alpha}}{w_\perp \sin\alpha} \right)$$
$$ \Delta v_\mathrm{max, min} = \frac{GM\left(\cos\alpha -\frac{w_\|}{w} \pm \sqrt{\cos\alpha +\frac{w_\|}{w}\sin\alpha}\right)}{bw\left( 1 + \frac{w_\|}{2w}\sin\alpha \mp \sqrt{\cos\alpha + \frac{w_\|}{w} \sin\alpha}  \right)} $$
These equations are definitely(probably) right, aside form all the ways they might be wrong.
8F. Can we understand f(aka $\frac{d\rho}{d\rho_0})$ in terms of the continuity equation:
$$\frac{d\rho}{dt} = -\nabla\cdot\bf{J}$$
I don't understand this yet but it feels like a really really big breakthrough. 

9. Probe for interaction physics in these overdense interactions? Could gaps be used to track down specific subhalos on specific orbits??
10. Relativistic delays for outside of the milky way. I suppose modelling all galaxies outside of the milky way
11. Putting upper and lower limits on all this. Like I'm really scared that if we only know the mass of the milky way to a factor of 10, that must have a huge impact for the subhalo population. I'd imagine this is worse for the andromeda galaxy(although maybe not because it can be easier to observe outside of our own galaxy.) But, maybe the real limits of this program aren't number of streams observed, but refinements on galactic parameters(which I'm sure would be easier to hone in on if we knew what DM was- a paradox.) We knew this would be hard, but I think the best answer is to output a range for each parameter(hopefully we can do this for a subsample of streams, otherwise the project becomes computationally infeasible), and just monte  carlo through this parameter space to find(95th percentile) lower and upper bounds. We knew this was going to be hard, but I'll link a paper outlining this type of approach later.
12. Understand limits of what gaps to include and not include. For example, a subhalo with a maximum deltavy = .08 has a deep gap going down to f=.03, but it's width is ~.8 degrees, or 1.5 degrees at f = .75. We should think more carefully about what to include and not include(I suppose if we include an infall model, we could keep a much wider range of inital gaps, and just throw out anything that doesn't stay until z=0).
13. How does the spur etc form? ie, how do we account for this in our model? 
15. Tidally stripped dark matter along the stream???(it has to be there right?)
16. Trying to work out the maximum feasible energy transfer in realistic conditions. Idk, it's pretty half baked, but part of me wonders whether there's some usable physics there. 
17. could clean out subhalos in the rotations step if I wanted to. Like once we rotate, we can eliminate a lot of subhalos that won’t get close to the stream. 
Do initial t0 cleaning(is this what I said below? Or is the idea to clean for a specific timestep) (short)
20. Can stream material be lost? How can this affect the continuity equation or be governed by it?is there different math for edge cases? 
21. Q balls and fuzzy dark matter? It seems like these can be treated relatively easily in galacticus no? Is there merit in trying to place constraints on them? What models haven't we considered that are worth thinking about? Does anyone know what the substructure for neutralinos or gravatinos is, and are there revised supersymmetric constraints given the demise of MSSM?

## Paper 8
### Goal
* Papers 1-7 incorporate all the features we currently see as important to this model. However, it is likely(bordering on certain) that something else will come up as we work. ie, at every stage, we introduce new features, often with a "toy model" that we tell ourselves we can fix later if need be. This is the correct workflow, because finalized ideas oftentimes cannot be realized without starting somewhere(and hearing feedback from the community wherever we are naive). So, in an ideal world, this paper isn't necessary- any necessary changes have already been incorporated. However, in a realistic world, this will probably be necessary. By definition, one cannot know what will need to go in here, but here are a few idea pulled from the void above:

* First simulation using andromeda(and perhaps other) galaxies.
* Finish WDM window function patch
* Extend subhalo masses below $10^5 M_\odot$
* Introduce more tests if any major ones missed
* Gather current constraints and data from other sources to use as bayesian priors(likely wouldn't publish this)
* Realistic connection to the obsevable limits of each stream. Ie, to what $f$ value can a given stream be constrained.
* Develop some procedure for blinding final predictions. 
    * This may seem excessive, but there will likely be a high degree of subjectivity in at least a few norm-defying streams. For results of this magnitude, and especially those of a statistical nature(I watched a recording of the unblinding for either LIGO or the g-2 anomaly data), it's both good practice, and helps with optics/response papers that would certainly pop up (if we get something shocking, like ruling out everything except primordial black holes).
* Can dark matter candidacy change stream predictions? I only saw a brief comment about this in a tea-time paper(and I plan on revisiting it, because this sounds crazy), but if we were going to be madlads, in principle we could try to place candidate-dependant constraints on the *total* number of streams per galaxy(ie, the asymptotic # we could ever discover). This would have to be done so so so carefully, but then we would modulate over:
(Gap properties | (gaps per stream | number of streams per galaxy)).
* I suspect indirect detection(ie neutrino signals from a $\chi-$baryon interaction) is an utterly hopeless endeavor, but if there *was* some magic results, this is where they would go. 
* Gap forensics, primordial black holes, fuzzy dark matter, etc(we would want to do a "test batch" of these new models before applying them to all streams)


## Final Push
* Once we have 
    1. Carefully modeled flybies using the improvements in papers I-VII, 
    2. Maximally accounted for the data we can extract (within reason)
    3. Generated gap predictions for all other known contributors(again within reason)
* The only thing left to do is apply this model to all known streams(and generate optimistic and pessimistic ranges for what could be predicted with more streams)
* The hard part will be accounting for the uniqeness of every stream, getting the statistics right, and simply handling this much data. 
* However, the workflow itself would be very simple. To test CDM, we simply run this model with a CDM subhalo population, generate the predicted number of gaps(really a much more complicated set of observables), and compare this to real data, using current constraints as the priors for our model. If CDM is outside of these parameters, we've disproved it. 
* This could be repeated for any dark matter candidate(at least any candidate that is astrophysically unique), but personally the most exciting case is MOND. The idea is, by rerunning this test with *no* dark matter subhalos, we would have a prediction only from the other sources outlined in papers VI. The statistical power per stream will be vastly higher here, so, if "no dark matter gaps" can be ruled out to 95% CI or $3\sigma$, then we have put a no go thereom on any future MOND model. Regardless of success at explaining rotation curves(or any other plausible advantage), hypotheses that are homogeneous, that is don't have substructure or a plausible gap forming mechanism, cannot exist.