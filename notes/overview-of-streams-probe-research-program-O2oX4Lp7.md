> [] # Overview of Streams-Probe Research Program
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
* fix equation 3 in paper 1


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



after much adjusting, we have 
$$\Delta v = \Delta v_{\mathrm{point}} + \int_\sqrt{b ^2 + \frac{y^2 w_\perp^2}{w^2}}^{r_\mathrm{sub}} \frac{2 G \left(M_\mathrm{tot}- M_\mathrm{enc}(r)\right) dr}{r^2 \sqrt{r^2 -r_\mathrm{min}^2}}$$


$$\Delta v =  \int_{r_\mathrm{min}(y)}^{R_\mathrm{tot}} \frac{-2 G M_\mathrm{enc}(r) dr}{r^2 \sqrt{r^2 -r_\mathrm{min}^2(y)}}$$

impact parameter cleaned with 

$$2\arctan\left(\frac{r_0v_y \pm\sqrt{r_0^2(v_x^2 +v_y^2) - (\vec{r}'\cdot \vec{v}')^2}}{r_0v_x  + \vec{r}'\cdot \vec{v}' }\right) < \phi < 2\arctan\left(\frac{r_0v_y \pm\sqrt{r_0^2(v_x^2 +v_y^2) - (v^2T_\mathrm{step} + \vec{r}'\cdot \vec{v}')^2}}{r_0v_x +v^2T_\mathrm{step} + \vec{r}'\cdot \vec{v}' }\right),$$
keeping only the (+) and (-) regions separately (if they exist.)

Then, we can(?) solve analytically:

$$b^2(\theta) = |\mathbf{\Delta r}|^2 -\frac{(\mathbf{\Delta r} \cdot \mathbf{v})^2}{|\mathbf{v}|^2}  $$, 
with $$\mathbf{\Delta r} = \mathbf{r(\theta)}- \mathbf{r'}$$,

and 
$$\vec{r} = \vec{r}_\mathrm{stream} = R_0(\cos\theta \hat{x} + \sin\theta \hat{y}) $$
$$\frac{1}{2}\frac{db^2(\theta)}{d\theta} = \mathbf{\Delta r}\cdot \mathbf{\dot{r}} -\frac{(\mathbf{\Delta r} \cdot \mathbf{v})(\mathbf{ \dot{r}} \cdot \mathbf{v})}{v^2} = -\mathbf{ \dot{r}}\cdot\left(\mathbf{r'} +\mathbf{v}\frac{\mathbf{\Delta r} \cdot \mathbf{v}}{v^2}   \right) =0  $$
where the last expression uses the fact that $\mathbf{r} \cdot  \mathbf{\dot{r}} = 0$. Rewriting, and taking $v_y =0$, 

$$\left(r_x' -v_x'\frac{\vec{r}'\cdot\vec{v}'}{v'^2}  \right)\sin\theta -r_y'\cos\theta + \left(R\frac{v_x'^2}{v'^2}\right)\cos\theta\sin\theta =0.$$
Tastefully rewriting as 

$$ c_x \sin\theta - c_y \cos\theta + c_1 \cos\theta\sin\theta     $$
(note: $c_1$ has the opposite sign from the more complicated equation before )

and  using the [Weirstrass substition](https://math24.net/weierstrass-substitution.html):

$$ \sin\theta =\frac{2t}{1+t^2}, \ \ \ \cos\theta  =\frac{1-t^2}{1+t^2},$$ 

we find:

$$c_y t^4 + 2 (c_x -c_1)t^3 + 2 (c_x + c_1) t - c_y = 0.$$

For simplicity, rewriting as

$$f(t) = t^4 + b_3t^3 + b_1t - 1 = 0.$$

with $b_3 = \frac{2(c_x -c_1)}{c_y}$, $b_1 = \frac{2(c_x + c_1)}{c_y}$ and employing a [Sturm Chain](https://math.stackexchange.com/questions/3513840/how-to-determine-number-of-roots-and-what-type-for-quartic-equations), we have:

$$ P_0(t) = f(t) = t^4 + b_3t^3 + b_1t - 1 $$ 

$$ P_1(t) = f'(t) = 4t^3 + 3b_3t^2 + b_1 $$ 

$$ P_2(t) = -\mathrm{Rem}(P_0, P_1) = \frac{3b_3}{16}t^2 - \frac{3 b_1}{4} t + \left( \frac{b_1 b_3}{16} + 1\right)$$ 
$$ P_3(t) = -\mathrm{Rem}(P_1, P_2) = 
-\left(\frac{64b_1^2}{b_3^4} - \frac{64}{3b_3^2} + \frac{32 b_1}{3b_3}\right) t + \left(\frac{256b_1^2}{3b_3^4} + \frac{16b_1^2}{3b_3^3} + \frac{16}{b_3}   \right)
$$ 

In principle, we also need to compute $P_4(t)$, but it's an absolute nightmare, and it's constant! So, the sign will be the same at both endpoints and it's meaningless. For each stream, we have 2 regions along the stream corresponding to $t_\mathrm{closest } \in[0,\frac{\mathrm{pal5Age}}{\mathrm{\#Timesteps}}]$ (with time unrelated to the $t$ variable above.) The number of turning points in a region is $V(b)-V(a)$, $V(x)= \sum_i\mathrm{Bool}[P_i(x) > 0]$. Thus, we must evaluate 

$$V(\tan(\frac{\phi_{(+)}(t_\mathrm{max})}{2})) - V(\tan(\frac{\phi_{(+)}(t_\mathrm{min})}{2}))   $$ 

and

$$V(\tan(\frac{\phi_{(-)}(t_\mathrm{max})}{2})) - V(\tan(\frac{\phi_{(-)}(t_\mathrm{min})}{2}))   $$ 

If either of these are nonzero, we keep the subhalo and do a more careful search. 

But, we can refine this further. This above analysis only shows whether there is a *turning point*, not one of these is a minima. We  can do a similar analysis on $f'(t)$ to determine if a turning point of f is a min or a max. Again, we must solve an equation to determine the actual points where $f(t) =0$ or $f'(t)= 0$, but we can assess these regions. Take 

$$\tilde{P}_0 = f'(t) = 4t ^3 + 3 b_3 t^2 + b_1   $$ 

$$\tilde{P}_1 = f''(t) = 12t ^2 + 6 b_3 t$$

$$\tilde{P}_2 = - \mathrm{Rem}(\tilde{P}_0, \tilde{P}_1) = \frac{b_3^2}{2}t -b_1$$

$$\tilde{P}_3 = - \mathrm{Rem}(\tilde{P}_1, \tilde{P}_2) =\frac{-12b_1}{b_3}\left(\frac{4 b_1}{b_3^3} + 1\right),$$
where $\tilde{P}_3$ is a meaningless addition, but can be written simply this time. 




<br> <br> <br>
more elaborate/junk:
$$\left(r_x' -v_x'\frac{\vec{r}'\cdot\vec{v}'}{v'^2}  \right)\sin\theta -\left(r_y' -v_y'\frac{\vec{r}'\cdot\vec{v}'}{v'^2}  \right)\cos\theta = \frac{R(v_y'^2- v_x'^2)\cos\theta\sin\theta}{v'^2} + \frac{2Rv_x' v'_y\cos^2\theta}{v'^2}   -\frac{Rv_x' v'_y}{v'^2}.   $$

Tastefully rewriting as 

$$ c_x \sin\theta - c_y \cos\theta = c_1 \cos\theta\sin\theta + c_2 \cos^2\theta - c_3     $$

and  using the Weirstrass substition:

$$ \sin\theta =\frac{2t}{1+t^2}, \ \ \ \cos\theta  =\frac{1-t^2}{1+t^2},$$ 

we find:

$$ t^4\left(c_y + c_2 + c_3 \right) + t^3\left( 2c_x +2 c_1\right) + t^2\left(2c_3 -2c_2\right) + \left(2c_x -2c_1 \right) + \left( c_3 - c_y\right) $$
One can also rewrite using [Chebysev polynomials](https://www.cfm.brown.edu/people/dobrush/am34/Mathematica/ch5/chebyshev.html), leading to the form 
$$\left(r_x' -v_x'\frac{\vec{r}'\cdot\vec{v}'}{v'^2}  \right)U_1(\theta) -\left(r_y' -v_y'\frac{\vec{r}'\cdot\vec{v}'}{v'^2}  \right)\cos\theta = \frac{R(v_x'^2- v_y'^2)\cos\theta\sin\theta}{v'^2} + \frac{2Rv_x' v'_y\cos^2\theta}{v'^2}   -\frac{Rv_x' v'_y}{v'^2}   $$


Just showing some important math: 
$$ \Delta v_{i, \mathrm{point}} =\left(c_{i,1} -c_{i,2}t_\mathrm{off}\right)\cdot \frac{-2GM}{r_\mathrm{min}^2}  $$
$$r_\mathrm{min}^2 = b^2 - \frac{y^2w_\perp^2}{w^2},\ \ \  t_\mathrm{off} =- \frac{yw_\|}{w^2}$$

Also, I believe the analytical form for any velocity component of a point source is 

$$\Delta v_{i,\mathrm{Point}}= (a_i + b_i t_\mathrm{offset})\left(\frac{-2G M}{r_\mathrm{min}^2 w}\right)$$

with

$$ r_\mathrm{min} = b^2 + \frac{y^2 w_\perp^2}{w^2}, \ \ \ t_\mathrm{offset} = \frac{-yw_\|}{w^2}$$

similarly, 

$$\Delta v_{i,\mathrm{Plummer}}= (a_i + b_i t_\mathrm{offset})\left(\frac{-2G M}{w(r_\mathrm{min}^2 +r_\mathrm{Plummer} ^2) }\right),$$

with 

$$r_\mathrm{Plummer} = 1.62\mathrm{kpc} \sqrt{M/10^8M_\odot}.$$

$$\Delta v_{i,\mathrm{NFW}}= (a_i + b_i t_\mathrm{offset})\left(-8 \pi G \rho_0 R_s^3\right)\left( \mathrm{arcsinh} (x) + 2 a \log(x)   \right),$$

Hypergeometric solution: For a linear spline, we have 

$$\log(m) = \log(m_{i-1}) + \frac{\log(m_i/m_{i-1})}{\log(r_i/r_{i-1})} \log(r/r_{i-1})$$

$$\log(m) = \alpha_i + \beta_i \log(r/r_{i-1}) = \alpha_i +  \log(r^{\beta_i}) $$

$$m(r_{i}<r< r_{i+1})= \alpha_i r^{\beta_i},  $$

$$ \beta_i = \frac{\log(m_{i+1}/m_i)}{\log(r_{i+1}/r_i)},\ \ \ \alpha_i = \frac{m_i}{(r_i)^{\beta_i}}. $$

Now, $I(r)$, the main integral, can be written as 

$$I(r) =  \frac{-2G}{wr_\mathrm{min}^2}\left(\int_{r_\mathrm{min}}^{r_{i=0}}\frac{\alpha_ir^{\beta_i -2}}{\sqrt{r^2-r_\mathrm{min}^2}}dr +
\int_{r_{i=-1}}^{r_\mathrm{halo}}\frac{\alpha_ir^{\beta_i -2}}{\sqrt{r^2-r_\mathrm{min}^2}}dr+ \sum_{[r_{i-1}>r{_\mathrm{min}}] }^{r_i<r_\mathrm{halo}} \int_{r_i}^{r_{i+1}}\frac{\alpha_ir^{\beta_i -2}}{\sqrt{r^2-r_\mathrm{min}^2}}dr  \right)$$

The lower term cancels (unless the hypergeometric function somehow becomes singular at 1), leaving

$$ I(r) =  \frac{-2G}{wr_\mathrm{min}^2}\left(\sum_{r_i > r_\mathrm{min}}^{r_i < r_\mathrm{halo}}
\sqrt{1 - \frac{r_\mathrm{min}^2}{r_i^2}} \times\left(  \frac{\alpha_{i-1} r_i^{\beta_{(i-1)}-1}}{1-\alpha_{i-1}}  \\~_{2}F_1\left[1, \frac{\beta_{i-1}}{2};\frac{\beta_{i-1}+1}{2}; \frac{r_i^2}{r_\mathrm{min}^2}\right]-\frac{\alpha_{i} r^{\beta_i}}{1-\alpha_{i}} \\~_{2}F_1\left[1, \frac{\beta_{i}}{2};\frac{\beta_{i}+1}{2}; \frac{r_i^2}{r_\mathrm{min}^2}\right]\right) \right)... $$

$$... + \frac{-2G}{wr_\mathrm{min}^2} \sqrt{1 - \frac{r_\mathrm{min}^2}{r_\mathrm{halo}^2}}
 \frac{\alpha_\mathrm{max} r_\mathrm{halo}^{(\beta_\mathrm{max}-1)}}{1-\alpha_\mathrm{max}}  \\~_{2}F_1\left[1, \frac{\beta_{\mathrm{max}}}{2};\frac{\beta_\mathrm{max}+1}{2}; \frac{r_\mathrm{halo}^2}{r_\mathrm{min}^2}\right]$$


For a point model, the integral term becomes

$$I_\mathrm{point} = \frac{-2GM}{wr_\mathrm{min}^2 };\ \
r_\mathrm{min} \equiv \sqrt{b^2 + \frac{y^2 w_\perp^2}{w^2}}$$

For a Plummer model, 
$$I_\mathrm{plummer} = \frac{-2GM}{w(r_\mathrm{min}^2 + r_\mathrm{p} ^2) }; \ \ r_\mathrm{p} \equiv 1.62 \mathrm{kpc} \cdot \sqrt{\frac{M}{10^8M_\odot}} $$

For a Shell model, 
$$I_\mathrm{shell} = \frac{-2GM}{wr_\mathrm{min}^2  }\left(1- \frac{\sqrt{R_\mathrm{halo} ^2- r_\mathrm{min}^2}}{R_\mathrm{halo}} \right),$$
Where the size of the halo (or shell) is determined through the truncated mass profile.

For a core model, 
$$I_\mathrm{core} =  \frac{-2GM\sqrt{R_\mathrm{halo}^2 - r_\mathrm{min}^2}}{wR_\mathrm{halo}^3} + I_\mathrm{shell}$$

For an NFW profile 

$$M(r) =4\pi\rho_0R_s^3\left(\log \left(1 + \frac{r}{R_s}\right) - \frac{r}{r+ R_s}\right)   $$
Rewriting in 

$$ x \equiv \frac{r}{r_\mathrm{min}},\ \ \  a \equiv \frac{r_\mathrm{min}}{R_s}$$

$$M(x) =4\pi\rho_0R_s^3\left(\log \left(1 + ax\right) - \frac{ax}{ax+ 1}\right)$$

$$ I_\mathrm{NFW} = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2}\int_1^\infty\frac{\log \left(1 + ax\right) - \frac{ax}{ax+ 1}}{x^2 \sqrt{x^2-1}} dx $$


The indefinite integral can be written as 

$$\begin{align} I_\mathrm{NFW;\ indefinite} = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(-2 a \arctan(\frac{1}{\sqrt{x^2-1}}) - \frac{(2a^2 -1)\log(1+ax)}{\sqrt{1-a^2}} +...\right)\end{align}$$
$$\begin{align}
\left(...+ \frac{\sqrt{x^2-1}\log(1+ax)}{x} -\log(x +\sqrt{x^2 -1}) + \frac{(2a^2-1)\log(-a -x +\sqrt{1-a^2} \sqrt{x^2-1})}{\sqrt{1-a^2}} \right) \end{align}$$

(where the prefactor multiplies both terms- multiline equations aren't working in markdown.)

We want to evaluate this at 1 and infinity. at 1, massive simplicatiations result in, for $a>1$ (?):

$$I_\mathrm{NFW}(x=1) = \frac{-8 \pi^2 G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\frac{2a^2 -1 }{\sqrt{a^2 -1}} - a 
\right)$$

$$I_\mathrm{NFW}(x=\infty) = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( \log\left(\frac{a}{2}\right) + \frac{(2a^2-1)\arctan(\sqrt{a^2-1})}{\sqrt{a^2-1}}
\right)$$

meaning  for a>1

$$I= \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( \log\left(\frac{a}{2}\right) + \frac{(2a^2-1)\left(\arctan(\sqrt{a^2-1})- \pi\right)}{\sqrt{a^2-1}}  + \pi a  \right)$$

this is tenous, but this *might* simplify to 

$$I =  \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( \log\left(\frac{a}{2}\right) - \frac{(2a^2-1)\arctan\left(\frac{1}{\sqrt{a^2-1}}\right) }{\sqrt{a^2-1}}  + \pi a  \right)$$

for $a=1$, the indefinite form of the integral(from 1 to X) is :

$$I(X) =  \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\frac{\pi}{2}  + \frac{1-X}{\sqrt{X^2-1}} + \mathrm{arcsec}(x) - 2 \arctan(X - \sqrt{X^2-1}) + \frac{\sqrt{X^2-1}\log(1+X)}{X}- \log(X + \sqrt{X^2-1})   \right)$$

which simplifies to (**a=1**)
$$I_\mathrm{full} =  \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\pi - \log(2)\right), $$
which agrees with the a>1 form aside from an infinite term in the middle.

for a < 1:
$$I(X) =  \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( a\pi - a \arctan(\frac{1}{\sqrt{X^2-1}}) - 2a\arctan(X- \sqrt{X^2 -1}) + ...\right)$$

$$\left(...+\frac{2a^2}{\sqrt{1-a^2}}\left( \mathrm{arctanh}\left(\frac{1+a}{\sqrt{1-a^2}}\right) -\mathrm{arctanh}\left(\frac{1+ax - a\sqrt{X^2-1}}{\sqrt{1-a^2}}\right)\right)  +\sqrt{1-a^2}\log(1+aX)+...\right)$$

$$\left(... + \frac{\sqrt{X^2-1}\log(1+aX)}{X} - \log(X+ \sqrt{X^2-1}) - \sqrt{1-a^2}\log\left( a + X - \sqrt{1-a^2}\sqrt{X^2-1} \right) \right)$$

$$I(1) = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( \frac{\pi a}{2}\right)$$

$$I(\infty) = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left( a \pi + \log(\frac{a}{2}) + \sqrt{1-a^2}\log\left(\frac{a}{1-\sqrt{1-a^2}}\right)+ \frac{a^2}{\sqrt{1-a^2}}\log\left(\frac{a+1 - \sqrt{1-a^2}}{a+1 + \sqrt{1-a^2}}\right)    \right)$$

At $a\rightarrow1$, assuming the lower limit is actually 0,
$$ I_\mathrm{tot} \rightarrow\frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(a \pi -\log(2) + \frac{\log(1)}{\sqrt{1-a^2}}\right) $$

Trying this again using wolfram alpha, the indefinite integral( for all cases?) is:

$$I(x) = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\frac{\sqrt{x^2-1}}{x}\log(ax + 1) +  \frac{1}{\sqrt{1-a^2}} \log\left(\frac{a x + 1}{\sqrt{1-a^2}\sqrt{x^2-1} - (a + x)}\right) - \log(x + \sqrt{x^2 -1})   \right)$$

Evaluating as $x \rightarrow \infty$: 

$$I(\infty) = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(???
\right)$$

and as $x \rightarrow 1$: 

$$I(1) =_? \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\frac{i\pi}{\sqrt{1-a^2}}\right)$$

$$I_\mathrm{tot} = \frac{-8 \pi G \rho_0 R_s^3}{r_\mathrm{min}^2} \left(\log\left(\frac{a}{2}\right) +\frac{\log\left(\frac{-a}{\sqrt{1-a^2}-1}\right)}{\sqrt{1-a^2}}   \right)$$

The first term is clearly well behaved for all $a$. The second is less apparently so, but let's analyze: For $a<1$

$$\frac{\log\left(\frac{-a}{\sqrt{1-a^2}-1}\right)}{\sqrt{1-a^2}}  = \frac{\log\left(\frac{a}{1 -\sqrt{1-a^2}}\right)}{\sqrt{1-a^2}},  $$ 

which is finite, since $\sqrt{1-a^2} <1$ in this limit. 

For $a>1$, one must be a little more careful in the analysis:

$$\frac{\log\left(\frac{-a}{\sqrt{1-a^2}-1}\right)}{\sqrt{1-a^2}}  = \frac{\log\left(\frac{-a}{i\sqrt{a^2-1}-1}\right)}{i\sqrt{a^2-1}} = \frac{\log\left(\frac{i\sqrt{a^2-1}-1}{a}\right)}{i\sqrt{a^2-1}} = \frac{\mathrm{arctan}(\sqrt{a^2-1})}{\sqrt{a^2-1}}, $$ which is clearly real when $a>1.$  Since $\mathrm{arctan(x)} \rightarrow x$ when $x<<1$, this is finite as $a \rightarrow 1$. In fact, for $a\rightarrow1_{(+)}$, this $=1$. 

for $a \rightarrow 1_{(-)}$, the analysis is longer, but we find 

$$\frac{\log (a)}{\sqrt{a^2-1}} - \frac{\log(\sqrt{a^2-1} -1)}{\sqrt{a^2-1}}= \frac{\sqrt{a^2 -1}}{a^2} -\frac{1}{\sqrt{a^2-1}-1} \rightarrow_{a\rightarrow 1} 1, $$ 
so these agree. This is also verified by wolfram alpha (integrating exactly when $a=1$ gives $1-\log(2)$)

Writing the final form (after many many misteps and a missing $1/w$ from most earlier equations):
$$I_\mathrm{NFW} =\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2}\left(\log\left(\frac{a}{2}\right) +\frac{\mathrm{arctan}(\sqrt{a^2-1})}{\sqrt{a^2-1}}  \right)\ \mathrm{if}\ a\geq 1,  $$
and 
$$I_\mathrm{NFW} =\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2}\left(\log\left(\frac{a}{2}\right) +\frac{\log\left(\frac{a}{1 -\sqrt{1-a^2}}\right)}{\sqrt{1-a^2}}  \right) \ \mathrm{if}\  a < 1 .$$

Ah! But while the infinite form is correct mathematically, numerically it overpredicts gaps. We need to truncate at $R_\mathrm{halo}.$

Thus in full we have, 

$$I_\mathrm{NFW} = I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2}\left(\frac{\sqrt{x^2-1}}{x}\log(ax + 1) - \log(x + \sqrt{x^2 -1})  +\frac{\mathrm{arctan}\left(\frac{\sqrt{a^2-1}\sqrt{x^2-1}}{a+x}\right)}{\sqrt{a^2-1}}  \right)\ \mathrm{if}\ a\geq 1,  $$
 
 
$$I_\mathrm{NFW} =I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2}\left(\frac{\sqrt{x^2-1}}{x}\log(ax + 1) - \log(x + \sqrt{x^2 -1})  +\frac{\log\left(\frac{ax +1}{a + x - \sqrt{1-a^2}\sqrt{x^2-1}}\right)}{\sqrt{1-a^2}}  \right) \ \mathrm{if}\ a < 1. $$

At $a=1$, these converge to 

$$I_\mathrm{NFW} =I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2}\left(\frac{\sqrt{x^2-1}}{x}\log(x + 1) - \log(x + \sqrt{x^2 -1})  +\frac{\sqrt{x^2-1}}{x+1}\right),$$

which converges to previous results (ignoring the shell term) as $x \rightarrow \infty$.

Plugging rewriting with $x \rightarrow\tilde{R} \equiv \frac{R_\mathrm{halo}}{r_\mathrm{min}},$ and remembering that $a =\frac{r_\mathrm{min}}{R_s}$

$$I_\mathrm{NFW} = I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2} \left(\frac{\sqrt{\tilde{R}^2-1}}{\tilde{R}}\log(a\tilde{R} + 1) - \log(\tilde{R} + \sqrt{\tilde{R}^2 -1})  +\frac{\mathrm{arctan}\left(\frac{\sqrt{a^2-1}\sqrt{\tilde{R}^2-1}}{a+\tilde{R}}\right)}{\sqrt{a^2-1}}  \right)\ \mathrm{if}\ a\geq 1,  $$
 
 
$$I_\mathrm{NFW} =I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2} \left(\frac{\sqrt{\tilde{R}^2-1}}{\tilde{R}}\log(a\tilde{R} + 1) - \log(\tilde{R} + \sqrt{\tilde{R}^2 -1})  +\frac{\log\left(\frac{a\tilde{R} +1}{a + \tilde{R} - \sqrt{1-a^2}\sqrt{\tilde{R}^2-1}}\right)}{\sqrt{1-a^2}}  \right) \ \mathrm{if}\ a < 1. $$

At $a=1$, these converge to 

$$I_\mathrm{NFW} =I_\mathrm{shell} +\frac{-8 \pi G \rho_0 R_s^3}{wr_\mathrm{min}^2} \left(\frac{\sqrt{\tilde{R}^2-1}}{\tilde{R}}\log(\tilde{R} + 1) - \log(\tilde{R} + \sqrt{\tilde{R}^2 -1}) +\frac{\sqrt{\tilde{R}^2-1}}{\tilde{R}+1}\right),$$

which converges to previous results (ignoring the shell term) as $x \rightarrow \infty$.




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

Rewriting the math one more time (from a fresh start):
$$\vec{d} = \vec{r} - \frac{R_v \vec{v}}{v^2} - \vec{c}$$
$$\frac{db^2}{d\theta} =\vec{d}\cdot\frac{d\vec{d}}{d\theta} = \vec{d}\cdot\vec{d}'=  0 \Rightarrow$$

$$\frac{R'_v (\vec{c}\cdot\vec{v} - R_v)}{v^2} - \vec{c}\cdot\vec{r}' = 0,$$
where 
$$\vec{c} = \vec{r}_\mathrm{sub} - \frac{(\vec{r}_\mathrm{sub} \cdot \vec{v})\vec{v}}{v^2},$$

$$\vec{r} = \vec{r}_\mathrm{stream} = R_0(\cos\theta \hat{x} + \sin\theta \hat{y})$$

is 13kpc, but varied in the x-y plane for the angle of closest approach. Finally, 

$$R_v \equiv \vec{r}\cdot\vec{v} = R_0(v_x \cos\theta + v_y \sin\theta),$$

$$R'_v = \vec{r}'\cdot\vec{v} = R_0(-v_x \sin\theta + v_y \cos\theta).$$


this isn't right, but a first pass at when $\partial_yf(y,t)=0$:

$$ y = \frac{-1 \pm \sqrt{1+2\left(r_\mathrm{min}\hat{w}_\perp(\hat{w}_\perp^2f(t) - \hat{w}_\|\hat{w}_x)\right)^2}}{2(\hat{w}_\perp^2f(t) - \hat{w}_\|\hat{w}_x)},$$
where $\hat{w}$ is normalized to 1(projection), and 

$$f(t) \equiv \frac{\frac{v_yt}{r_\mathrm{stream}}- \sqrt{2}\sin(\frac{\sqrt{2}v_yt}{r_\mathrm{stream}})}{1-\cos(\frac{\sqrt{2}v_yt}{r_\mathrm{stream}})}, $$ assuming $\gamma=2$,  and this can be multiplied out to avoid the singular point in the denominator. Up to a factor of 2, this *almost* looks, like we're just subtracting out the first terms of the taylro series. Maybe we are?



### To Do
* Once Galacticus's SIDM feature is all set up, generating data involves:
    * Run sanity checks with small populations to familiarize myself with the code.
    * Read up on SIDM to understand the field we're working in.
    * Debug model if necessary(if my code has unit tests presumably the only place problems could occur is in SIDM mass profile or the subhalo population itself)
    * Generate full dataset. Perhaps generating data for 1 tree, then 40, then 400, then 4000 or something(loosely following the "increase in factors of 2" advice.)








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
$$ \int_{\theta(t_\mathrm{impact})}^{\theta(t_\mathrm{present})} r(\theta')^2 d\theta'  + \frac{(4 - \gamma ^2)\Delta v_y}{\gamma^2}\int_{\theta(t_\mathrm{impact})}^{\theta(t_\mathrm{present})} r(\theta')^3 d\theta'  + \frac{4\Delta v_y}{\gamma^2}\int_{\theta(t_\mathrm{impact})}^{\theta(t_\mathrm{present})} r(\theta')^3\sin(\gamma \theta') d\theta' +-\frac{2\Delta v_x    }{\gamma^2}\int_{\theta(t_\mathrm{impact})}^{\theta(t_\mathrm{present})} r(\theta')^3\cos(\gamma \theta') d\theta'= L_z t_\mathrm{age\ of\ gap}   $$

To modify the filter files (assuming they work correctly), for stream_Impact.f90, we find 
$$t_\mathrm{closest; min} = \frac{-r_\mathrm{apo}v_0 - \vec{r}_0'\cdot \vec{v}}{|v|^2}$$
$$t_\mathrm{closest; max} = \frac{-r_\mathrm{apo}v_0 + \vec{r}_0'\cdot \vec{v}}{|v|^2}$$
For the stream_kick.f90 file,
$$\Delta v_\mathrm{max} = \frac{G M_\mathrm{sub}}{w_\mathrm{min}b_\mathrm{min}} = \frac{G M_\mathrm{sub}}{w_\mathrm{min, peri}b_\mathrm{apo}} = \frac{G M_\mathrm{sub}}{|v - L_{z}/r_\mathrm{peri}|(r_\mathrm{min} - r_\mathrm{apo})}) $$

with 
$$L_z = r_p r_a \sqrt{\frac{2(V(r_p) - V(r_a))}{r_a - r_p}}$$ as calculated above, and 
$$r_\mathrm{min} = r'_0 + \frac{v (\vec{r}'_0 \cdot \vec{v})}{v^2}.$$
 if $v < L_z/r_\mathrm{peri}$ or $r_\mathrm{min} < r_\mathrm{apo},$ then the subhalo passes.  

b


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
    1. Try out Cython or pypy to see if this speeds code up? Jax is the main thing. torch quad?https://stackoverflow.com/questions/65269540/how-can-i-speed-up-scipy-integrate-quad two ideas to speed up integrals
    1. terminix iPhone app
    
* We'll need baryons soon
* Run some test simulations to ensure all this is working properly. Perhaps compare gaps created to circular case for a few subhalos.
    * then generate data with 1000 timesteps, 20k trees and 80 rotations about the z axis for CDM, certain WDM models, and SIDM.
    * Paper 4: how many more subhalos to account for finite stream length? Avg length of stream /360? Add factor of ~20% to be safe?(we’re on the ultra low end here)
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

## Paper V: A Full Test (and Applying to Multiple Streams)
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

$$\Delta z(y,t) = \frac{\Delta v_z(y) v_y }{r_0} \sin(\frac{v_y t}{ r_0})e^{-\lambda t},$$
or 

$$v_z(y,t) = \Delta v_z(y)  \cos(\frac{v_y t}{ r_0}) + \lambda f(y).$$
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
* I don't think we actually want line of sight velocity, since I *think* we have proper motions for pal- 5 (and many milky way streams. We can certainly pick some streams with proper motions, in anticipation that *all* (most?) galactic streams will have proper motions and spectroscopic velocities post gaia 4-5, euclid, and roman. And I mean *Via*? We'll be able to ask the streams what they had for lunch that day.)
* In terms of properly modulating the different data factors, I think what at *want* to do is group things by specific impact? Right, we *want* to keep the correlations between the velocities and size of a given gap. And, I was going to average over all phases for the z-plane oscillations (which would be the right thing to do if we knew nothing, and I'm sure there's a few different statistical approaches one could take.) But, given that we *do* know what the phase of the z oscillations is(as much as we know anything else- we're modeling this for discrete events rather than trying to reverse engineer things). Right, so since gaps are completely uncorrelated (or are they? There's some theory dependence to this, right?)
* About 40% of streams have radial velocity data
* should we predict velocity angle in paper 5?
 



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


## Paper VIA-VIB: Other Perturbers
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

* We have to decide if we're just sticking to the milky way or not (and modulate data appropriately. ) But, all of this should be fairly easy to do with analytical models(aside from maybe the bar speed and spiral arms), but the formation is where things are tricky. I talked a bit to kyle kremer about this, but that's one of the big danger points right now in this project. Right, 

* Caan we get the behavior for leading arm desintigration in pal-5? Need to think more.
    * predict where the arm of pal-5 is?
    * bar is slowing with time
* for lmc, does “angle difference” change with time? Do streams revert back to pointing along stream?
* do we need dynamical friction as  a feature of paper 6?


## Paper VIC: Formation (/ Morphology?)
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
* model dependent stream formation? Do we predict number of total streams based on dark matter models?? That would be crazy ambitious(oh # of streams can be a statistic and it affects number of gaps seen. Modulate first over number of streams seen)
    * Run for models of future streams to generate predictions directly? That would be hella blinded and the data would already be done. The “5 post optimization” notebook in cats
    * compare different mechanisms to particle fanning code?
    * Look for new paper by price whelan and  tavangar about modeling overdensityies with some algorithm(using Jax and numpyro). That’s might be the key for us. “Off track and nongaussian features.”- that’s all the weird shit we’re looking for, but how to characterize it?
* black hole modification for paper 6C globular clusters
    
### To do
* *If* this model is actually right(it likely isn't), then I think the plan would be to see what's known in the literature, model whatever gaps we need to fill in, and then get the gap population. The $d\rho/dt$ model definitely needs to be better too, but then I guess we make a bunch of predictions, maybe for more streams than we've seen before. Maybe we test this model against some known progenitors(and data)to see how we do, and, even if we don't increase the number of streams we apply the full model to, we could still apply this piece of things. 
    * Again, do these gaps look different somehow from flybys? Is there a different signature from GCs vs globular clusters? Will we have to figure out what $\Delta L$ is between the progenitor and the stream itelf? If we could(and this is crazy ambitious) genuinely tell a GC gap from a Dwarf galaxy from the other sources, we would maybe have insight well beyond just dark matter substructure(which is of course the goal, but those direct detection experiments still explored indirect detection and other constraints when they thought they had a signal.) 
    * Presumably gaps will be much more uniform than for flybies(if the 3d model really does go like $\delta b / b$.) This, again, suggests our  test may be more powerful for substructure the smaller it gets(on some level/relative basis, the way an ant is techically "stronger" than a human), which is exciting. Again, I'm making this all up as we go, but if we can get a "fingerprint" for each gap contributor, our power goes up significantly( I don't *think* this is the case, but in principle if no DM models gave the correct subhalo gap population, that could place constraints on the milky way halo mass. Again, that feels circuar(because we'd have to assume a model), but sometimes there's something there in these moments.)
* To plot, we would want some running contribution of gaps for a few favorite streams, histograms on the type of behavior globular clusters and dwarf galaxies create, and probably some other things.
    * Wait *would* there be a dark matter halo around progenitors of mass $\sim 10^4 M_\odot?$ In CDM sure, but in WDM models, we wouldn't have substructure at that scale right? This must tie into the missing satellite problem somehow, but I have no idea how that was resolved(if it was).
* After all these graphs, as usual, we write, edit, send for local comments, submit, then deal with reviewer comments. 
    * I would probably end up reading a bit about the progenitors to write the introduction well(and model I'm sure)- I have so  much reading to get to before this, but it wouldn't hurt to get a jump start on this eventually. 



## Paper VII: Warm, Wide Streams (/Stream Morphology?)
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
* Do random walks of warm particles lead to the creation of (false) gaps?
* How many destroyed streams do we predict? Can we get this out of our model? We can’t work backwards right?
* going past linear regime above 1e7? can we do based on delta values? should this be sooner?
* could the unobservable regions in theoretically connected streams be gaps???
* morphology? is that what were after?

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
$$t_\pm(r) = \frac{ -\frac{yw_\|}{w} \pm\sqrt{r^2 - b^2 - \frac{y^2 w_\perp^2}{w^2}} }{w},\ \ \ \left(\frac{dr}{dt}\right)^{-1} = \frac{dt_\pm}{dr}= \frac{\pm r}{w \sqrt{r^2 - b^2 - \frac{y^2 w_\perp^2}{w^2}}},$$ where we choose the (-) solution as the subhalo comes in from $r = \infty$ to $r_\mathrm{min} = \sqrt{b^2 + y^2}$, and the (+) solution as it goes back out. After some algebra, we find:


$$ \Delta v_{y} = \int^{\infty}_{ \sqrt{b^2 + y^2}}\frac{-2G M(r)y w_\perp^2}{w^3r^2\sqrt{r^2 -b^2 - \frac{y^2 w_\perp^2}{w^2}}}dr,$$
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
14. Derive NFW thingy? Unrelated, and pretty half-baked.  Throw every form of newton's laws at this and do some nogo theorems for less energetically-desirable arrangements? Those *feel* possible(even if we have to calculate the self-energy for each setup numerically.) Right, but if we can prove that NFW/einasto is energetically favorable over certain distributions, that could hem things in. The black hole wars of the 70s (I think it was the 70s) started from relatively meager places(think about schwarzchild's "unphysical" solution in the trenches of '15-'16 WWI, and Einstein's supposed "refutation" of singularies in '44 or '45(or was it '40?) using spherical orbits of points. Honestly even though that paper was utterly wrong, it's kinda the approach I was hoping to take. Maybe this is one of those moments where einstein had good ideas even when he was dead wrong.)
15. Tidally stripped dark matter along the stream???(it has to be there right?)
16. Trying to work out the maximum feasible energy transfer in realistic conditions. Idk, it's pretty half baked, but part of me wonders whether there's some usable physics there. 
17. could clean out subhalos in the rotations step if I wanted to. Like once we rotate, we can eliminate a lot of subhalos that won’t get close to the stream. 
Do initial t0 cleaning(is this what I said below? Or is the idea to clean for a specific timestep) (short)
18. lagrangian for structured water? What's the interaction look like? How do *any* manybodied hamiltonians form(not even the slightest bit related.)
19. Write a review paper about stellars streams? Wildly presumptive now, but could start to make sense by the time we get to the void. 
20. Can stream material be lost? How can this affect the continuity equation or be governed by it?is there different math for edge cases? 
21. Q balls and fuzzy dark matter? It seems like these can be treated relatively easily in galacticus no? Is there merit in trying to place constraints on them? What models haven't we considered that are worth thinking about? Does anyone know what the substructure for neutralinos or gravatinos is, and are there revised supersymmetric constraints given the demise of MSSM?
22. Can we constrain halo shape (and thus subhalo population) through this program? Can (and should) we use helmi streams (or at least results from other winvestigations) to accurately model potentials? What are the systematics on *other* halo shapes in the local(ish) group, and does that quetion matter? Certainly we need a host halo mass for an (effectively) linear scaling in # of subhalos, but otherwise, if stream formation is a (relativley) ineffective tool for constraining host halo shape (ie, people have been thinking about this for a little bit, and we still don't have one final answer), then does this matter? (ie, if it's hard to determine a final halo shape from stream orbits, then the reverse is true as well: roughly modeled host halo shapes are adequate to get (relatively) correct stream orbits and behaviors.)
23. Can the faintest luminous dwarf galaxies (the real ones, not the ones accreted into the milky way) provide some special insight? If these perhaps happen to have less baryonic physics (I don't necessarily know), and they're *already* light, then we've effectively filtered out many of the highest mass subhalos (that we know are there), and these probes *really* hone in on the light subhalos we're questioning. and like yes, we'll have crap, non-6-dimensional photometry on these, but we can also (in principle) make a full catalogue of visible baryonic perturbers, where as the GMC and GC populations in the MW are heavily uncertain because... y'know there's a galactic core between us and whatever is on the other side.
24. What's the conceivable upper limit (in a profile dependant way) on the energy transferred from a flyby(likely have to go beyond impulse approximation)
25. Try to somehow solve the hubble tension? Maybe if we just stare at the problems long enough, answers magically appear.
26. how does the morpheon influence string theory? 
27. look up lagrangian for water and ice!
    * It’s a lattice theory

## Paper Dump

### Papers that are gems
https://iopscience.iop.org/article/10.1086/340957/pdf could be a good starting point for stream formation
https://academic.oup.com/mnras/article/487/2/2685/5491315 lmc perturbation
https://arxiv.org/pdf/2402.06393 same
bar rotates somewhere between 25 and 70 km/s
https://ui.adsabs.harvard.edu/abs/2016MNRAS.460..497H/abstractseems to be *the* paper on the galactic bar
https://arxiv.org/pdf/2011.13141 andrew don't know if you've seen this one, but it speculates on fairly interestiong behavior unique to fuzzy dark matter.

https://sci-hub.se/https://journals.aps.org/prd/abstract/10.1103/PhysRevD.66.032005 may somehow have statistical relevance, but almost certainly not(actually! This could be the final statistical step in accounting for "unkown unknowns.")
* https://arxiv.org/pdf/1804.04384 *may* have statistical value for us. I thin this is in the whole "power spectrum approach" that I'm missing background knowledge on. 
* Hyades stream seems to be a little bit significant. Saggittarius dwarf galaxy apparently perturbs too and needs to be modeled(at least for some streams- for some certainly there is little overlap. We can estimate this with M/b or M/b^2 scaling)
* https://academic.oup.com/mnras/article/517/3/3613/6773470 somehow gaps could support mond?? I'm highly skeptical of this, but I've dedicated absolutely no time to reading this paper. Another one I saw suggests that streams violate the equivalence principle.
* doi.org/10.1093/mnras/stz142 spiral arms paper (haven't read)
* Fardal 2015 seems like the main stream formation paper using a new technique called "particle spray."
* Hendel 2015 suggests that sometimes disrupted globular clusters can form "shells" instead of streams. I don't really know why, but it has to do with one of those (many) astrophysical angles that sound scary to me.
* "eplicyclic overdensities" are a thing.
wang 2012 has a model of bar potential
https://arxiv.org/abs/1610.05918v2 GMCs!
Oh, maybe we have to add in globular clusters too? That could be a bit more to think about. (apparently erkal found they don't do much, so maybe this bit is optional)
https://arxiv.org/pdf/1512.00452 just a paper to cite in our work about tidally disrupted halos. Frankly, I don't think it's really worth exploring beyond that.
https://academic.oup.com/mnras/article/470/1/522/3850227 could actually have value when thinking about backgrounds.
https://iopscience.iop.org/article/10.1088/0004-637X/799/1/28/pdf somehow i feel like something could be here. Something about "fanned morphologies" doesn't sound that boring. 
https://iopscience.iop.org/article/10.3847/0004-637X/824/2/104 we probably want to test this stream with the bar.

kupper A. H. W., MacLeod A., Heggie D. C., 2008, MNRAS, 387, 1248 (starting point for 'epicyclic overdensities'(?))
King I., 1962, AJ, 67, 471 i'll have to read this eventually i think
 https://iopscience.iop.org/article/10.3847/1538-4365/227/2/24 catalog of globular clusters if we want to include these (up to date at the time)
 https://iopscience.iop.org/article/10.3847/1538-4357/834/1/57 catologue of GMCs to import (but we have to flesh out the population in other quadrants, the way it was done in [this](https://arxiv.org/pdf/1809.09640) paper (page 9))
 https://iopscience.iop.org/article/10.3847/1538-4357/833/1/31 if I need a discussion about the pericenter of pal-5? It's still unknown (or it was in 2016 I think) to within a few kpc, but apparently the GMC (or globular cluster? No that wouldn't make sense) population is highly concentrated in this range, so small changes could have big affects. Again, pal-5 kinda sucks. If we have to go through multi paper lines of thought to figure out whether half of *every* stream is missing, this research program is going to be a nightmare! (latest thought I read is that we found the rest of pal-5)
 Gibbons S. L. J., Belokurov V., Evans N. W., 2014, ArXiv e-prints something about modeling stripping and lagrange clouds
 https://arxiv.org/pdf/astro-ph/0307446 original pal-5 paper (I believe). Don't think it's gonna crack this research program open for us, but not bad to have these citations handy.
King 1966 probably matters too. Ugh the oldies.

https://academic.oup.com/mnras/article/461/2/1590/2608506 ugh this is probably something to consider for paper 5 (or some asymptotic extension of it.) Because if we're looking at orbital wiggles from perturbations, we also have to consider this nonsense from a (non-analytic?) triaxial potential. Apparently something about stream widening too?
https://academic.oup.com/mnras/article/452/1/301/1747720 this is apparently the one for stream width (I think I referenced it above somewhere)
https://scholar.google.com/scholar?q=Errani+R.%2C+Penarrubia+J.+and+Tormen+G.+2015+MNRAS+449+L46 didn't read this, but apparently it proves out what I was saying that dark matter profile should be somehow measurable in the stream density. This just proves that everything interesting has been done and we should go home! 
https://arxiv.org/pdf/1202.3665
xHelmi, A., & Koppelman, H. H. 2016, ApJ, 828, L10 just cite - they did gaps too
gan, W. H. W., & Carlberg, R. G. 2014, ApJ, 788, 181 same

https://arxiv.org/pdf/2212.11006 really good paper on stream morphology** I think carlberg or price whelan has a 2024 paper too (https://arxiv.org/pdf/2405.18522)

penarrubia heating https://arxiv.org/pdf/1901.11536

more stuff like mine? https://arxiv.org/pdf/1608.05624 

big read https://arxiv.org/abs/2405.19410

really cool one from Ana (or at  least I hope it is)
https://arxiv.org/pdf/1804.06854

for paper 5 https://arxiv.org/pdf/2307.07402

https://arxiv.org/abs/1410.0360 another epicyclic overdensity paper

https://arxiv.org/pdf/2108.13420 other possible gap source

https://academic.oup.com/mnras/article/523/1/428/7161128 similar to us
 
## Paper VIII: Cleanup (?)
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
* Go from 3d model of the stream to actual model of the member stars
    * specific line of sight velocities of each star?( a la stacy kim and anikka peter 2023)

## Final Push
* Once we have 
    1. Carefully modeled flybies using the improvements in papers I-VII, 
    2. Maximally accounted for the data we can extract (within reason)
    3. Generated gap predictions for all other known contributors(again within reason)
* The only thing left to do is apply this model to all known streams(and generate optimistic and pessimistic ranges for what could be predicted with more streams)
* The hard part will be accounting for the uniqeness of every stream, getting the statistics right, and simply handling this much data. 
* However, the workflow itself would be very simple. To test CDM, we simply run this model with a CDM subhalo population, generate the predicted number of gaps(really a much more complicated set of observables), and compare this to real data, using current constraints as the priors for our model. If CDM is outside of these parameters, we've disproved it. 
* This could be repeated for any dark matter candidate(at least any candidate that is astrophysically unique), but personally the most exciting case is MOND. The idea is, by rerunning this test with *no* dark matter subhalos, we would have a prediction only from the other sources outlined in papers VI. The statistical power per stream will be vastly higher here, so, if "no dark matter gaps" can be ruled out to 95% CI or $3\sigma$, then we have put a no go thereom on any future MOND model. Regardless of success at explaining rotation curves(or any other plausible advantage), hypotheses that are homogeneous, that is don't have substructure or a plausible gap forming mechanism, cannot exist.
* For each stream, we give an expected number of gaps, or single dark matter number, monte carloed over the uncertain parameters such as total mass of the milky way. Then, we add up every gap number and compare to theory. But, how does this single number come about? How do we compare less dense (O(10) stars) streams to GD-1? Length is the most reasonable candidate, but certainly dense streams should count more than diffuse ones, right? And, are # of gaps, gap sizes, z-plane deformations and velocity data *independent* data points? or cross-correlating one prediction. What about spur-like features? Tidal heating? 
    * Tidal heating feels like an independent measurement, right? The first 4 datapoints are all the same event, but tidal heating is, by definition, completely separate events. Still, velocity perturbations can (apparently?) outlast gaps (https://iopscience.iop.org/article/10.1088/0004-637X/803/2/75). 
    * Perhaps it depends what we find. Right, the more we work through the 3d stream fingerprint (that I hope exists, but is still up in the air), and the specific measurements, the easier this all is. Again, I don't think the bones of this will change in the slightest, but every piece will get more nuanced the more we write, calculate and (I) read. 
    * At what size do we predict "destruction events" of streams? Again, I'm not particularly sure what this would look like, (I'm sure the simulated particle fanning models would do a much better job). But, maybe we can motivate other people to this work for us.  




$$\Delta\vec{v} = \int_{-\infty}^\infty \vec{a}(t) dt =\int_{-\infty}^\infty \frac{G M_\mathrm{enc}(r) \vec{r}}{r(t)^3} dt $$

$$ \dot{\theta}(y, t) \approx \frac{v_\mathrm{stream}}{r_\mathrm{stream}}\left(1 + \frac{\Delta v_y(y)}{v_\mathrm{stream}} - 2\frac{\Delta r(y, t)}{r_\mathrm{stream}} \right) $$

$$ \frac{\lambda(y,t)}{\lambda_0}\equiv \left|\frac{d\theta(t)}{d\theta_0}\right|^{-1}$$

$$\frac{d\rho_0}{dt} \sim A(r_0(t)) \times B(\sigma) $$