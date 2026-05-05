# Halo Triaxiality Random Walk Model

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `triaxiality`

## Goals

Extend the random walk model of [Benson et al. (2020)](http://adsabs.harvard.edu/abs/2020MNRAS.496.3371B) and [Johnson et al. (2021)](http://adsabs.harvard.edu/abs/2021ApJ...908...33J) to predict the distribution of halo triaxialities by using the energy tensor instead of the scalar energy.

The original idea for this was motivated by a statement in Section 3.3 of [Taylor (2011)](https://www.hindawi.com/journals/aa/2011/604898/):

> A physical mechanism which may account for the correlation was outlined in [Moore et al. (2004)](https://ui.adsabs.harvard.edu/abs/2004MNRAS.354..522M/abstract). A system of two halos merging on a radial orbit can be described in terms of a tensorial version of the virial theorem, in which the contributions of kinetic and potential energy must eventually reach an equilibrium component by component. Dissipationless mergers between dark matter halos should roughly conserve the individual tensor components, such that the final merger remnant will remember the original orientation of the infalling pair and will remain more extended along that axis.

However, I can't actually find any discussion of the tensor virial theorem and how it applies to halo shapes in [Moore et al. (2004)](https://ui.adsabs.harvard.edu/abs/2004MNRAS.354..522M/abstract). I've e-mailed James Taylor to see if he remembers where this was discussed.

## Paul's results
This is starting with a mixture of Binney and Tremaine's formulae cited above, and formulae from Chandrasekhar's 1962 paper "The potentials and Superpotentials of homogeneous ellipsoids".  The formulae there are adequate to get the volume functions $A_i$ in the triaxial case, but break down before we can get the potential energy tensor as this paper assumes a homogeneous density, and we are using the NFW distribution 

\begin{equation}\rho=\frac{\rho^*}{\frac{r}{R_s}(1+\frac{r}{R_s})^2}\end{equation}

We set the major axis ?eccentricity? $a_1$ to 1, which is valid since this parameter is just a scale factor in each direction. We also use Chandresaekhar's normalization for the $A_i$ ?volume? parameters, which is to say $[A_i]=1/l^3$.  

Defining the incomplete elliptical integrals 
\begin{equation}
E=\int_0^\phi (1-sin^2\theta sin^2\phi')^{1/2}d\phi'\\
F=\int_0^\phi (1-sin^2\theta  sin^2\phi')^{-1/2}d\phi'\\
sin \theta = \sqrt[]{\frac{1-a_2^2}{1-a_3^2}},\quad    cos\phi = a_3
\end{equation}

We have
$$A_1 = \frac{2}{sin^3\phi sin^2\theta}(F-E)\\
A_2 = \frac{2}{sin^3\phi sin^2\theta cos^2\theta}(E-Fcos^2\theta -\frac{a_3}{a_2}sin^2\theta sin\phi)\\
A_3 = \frac{2}{sin^3\phi cos^2\theta}(\frac{a_2}{a_3}sin\phi-E)$$

From here, if we define $m^2(\vec{x})=\sum_i\frac{x_i^2}{a_i^2}$, we can define the NFW distribution $\rho(m)$ for a triaxial system.
Defining $$\psi(m) = \int_0 ^m \rho(m') 2 m' dm'$$ we have

$$\psi(m)= \int_0^m 2R_s\frac{\rho^*}{(1+\frac{m'}{R_s})^2}dm' = 2\rho^* R_s^2(1-\frac{1}{1+\frac{m}{R_s}})$$
$$W_{ii} = -\pi^2 a_2^2a_3^2Ga_i^2A_i \int_0^{cR_s}(\psi(m)-\psi(cR_s))^2dm$$
$$W_{ii} = -G(2\pi\rho^*a_2a_3a_i)^2 A_i R_s^5(1-\frac{1}{(1+c)^2}-\frac{2ln(1+c)}{1+c})$$
or,
$$W{(i)}=-\gamma\frac{9}{4}\frac{G\tilde{M}^2}{R_s}\begin{pmatrix} A_1 & 0 & 0 \\ 0 & a_2^2A_2 & 0 \\ 0  & 0 &a_3^2A_3 \\ \end{pmatrix}$$
Where $\gamma=(1-\frac{1}{(1+c)^2}-\frac{2ln(1+c)}{1+c})$, $\tilde{M}=\frac{4\pi}{3}a_2a_3\rho^*R_s^3$
Note that a cutoff at $R=cR_s$ is put in by hand for the edge of the halo.  It is unclear (to Paul) if $\tilde{M}$ corresponds at all to the real mass of the halo.  That part is just in the "Formation of Galactic Disks" paper. The tensor is also manifestly diagonal in it's own coordinate system. Now, I think the energy tensor of a halo $E_{ij}=\frac{W_{ij}}{2}$, but I'm still a little fuzzy on the tensor virial theorem. Anyway as best as I can tell, this is the total energy of 2 merging halos when the smaller one is at the virial radius

$$E^{(tot)}= \frac{W^{(1)}}{2}+\big[R\frac{W^{(2)}}{2}R^T +Q(V_{int}+T^{(2)}_{rad})Q^T +\tilde{Q}T^{(2)}_{orb}\tilde{Q}^T\big] (1+\frac{m2}{m1})^{-\gamma} (1 + b)
$$

$W^{(1)}$ and $W^{(2)}$ are as defined below in their own coordinate system. $W^{(2)}$ is then rotated into the $W^{(1)}$ system, which we will take as the overall coordinate system. R is a bit involved, but it is simply the pitch yaw roll matrix defined below. To leading order, the orientation of the two halos are uncorrelated, so the 3 angles will be averaged from a flat, random distribution. Note each halo does not just have different orientations, but also axis ratios($a_i$), and thus form factors $A_i$, different concentrations, characteristic densities($\rho^*$), and characteristic radii $(R_s)$.These parameters will be selected from the same empirically derived distributions, but essentially nothing is the same in the energy tensors besides Newton's constant and the assumption of an NFW distribution. V is simply the interaction potential energy assuming each halo is a point particle at the virial radius. The interaction is of course radial between the two halos, and is defined in the $\hat{x}$ direction in the tensor's own coordinate frame. Then, it is rotated using the J matrix defined below into halo 1's principle coordinate system.  $Q$ and $\tilde{Q}$ are the same matrix in design, but $\tilde{Q}$ rotates from the $\hat{\tilde{x}}$ direction, as V and T are in general along different axes. T is just randomly chosen from a parameter space based on initial velocity distributions and energy gained through previous interactions between the two halos. One thing to note is that angular momentum is not calculated, at least not manifestly, so we will have to do extra work if we want to account for this.  

Because mergers between two large halos are highly energetic, a nontrivial fraction of the second halo will be ejected with energy large enough for escape.  Thus, large mergers are "downweighted" by the mass ratio, as shown above. Gamma and b are purely fine tuned constants describing the effective sum of highly nontrivial intermediate processes. There is no direct physics in them, at least none that we can see.
$$W^{(i)}=-\gamma^{(i)}\frac{9}{4}\frac{G\tilde{M}_{(i)}^2}{R^{(i)}_s}\begin{pmatrix} A^{(i)}_1 & 0 & 0 \\ 0 & (a_2^{(i)})^2A_2^{(i)} & 0 \\ 0  & 0 &(a_3^{(i)})^2A_3^{(i)} \\ \end{pmatrix}$$

$$R = \begin{pmatrix} cos\alpha cos\beta, & cos\alpha sin\beta sin\gamma - sin\alpha cos\gamma, & cos\alpha sin\beta cos\gamma + sin\alpha sin\gamma \\ sin\alpha cos \beta, & sin\alpha sin\beta cos\gamma + cos\alpha cos\gamma, & sin\alpha sin\beta cos\gamma - sin\alpha sin\gamma \\ -sin\beta, & cos\beta sin\gamma, & cos\beta cos\gamma 
\end{pmatrix}
$$

$$V_{i'j'}(r)=V_{xx}(r)=-\frac{GM_1M_2}{c^{(1)}R_s^{(1)}},$$
$M_i = 4\pi a_2 a_3 \rho^*_iR_{s,i}^3(ln(1+c_i)-\frac{c_i}{1+c_i})$

To follow through that derivation we just have to take the nfw distribution, change from $\textbf{x}$ to $\textbf{x'}$, where x' transforms ellpiptically to weight each component equally.  This jacobian gives us the $a_2a_3$ factor, the rest comes from integrating the NFW distribution spherically up to the virial radius. 

Finally, we have to generate $Q$ and $\tilde{Q}$.   $V$ is radial with respect to Halo 1, so we simply have to convert spherical to cartesian coordinates.  This depends on two free parameters $\theta$ and $\phi$ that we simply choose randomly from a flat distribution. 

We associate $\hat{a}_1 = \hat{x}, \hat{a}_2 = \hat{y}, \hat{a}_3 = \hat{z}$ for convenience. 

Thus $$ Q = \begin{pmatrix} sin\theta cos\phi & cos\theta cos\phi & -sin\phi \\ sin\theta sin\phi & cos\theta sin\phi & cos\phi \\ cos\theta & -sin\theta & 0 \end{pmatrix} $$

Now For $\tilde{Q}$.  First we need an orthonormal coordinate system, involving our radial coordinate, namely $(\hat{r}, \hat{a}, \hat{b})$. These, of course, must include cartesian relations in their definitions, so let $\hat{a}=\hat{r} \times \hat{x}=\begin{pmatrix} sin\theta  cos\phi \\ sin\theta sin\phi \\ cos\theta \end{pmatrix}\times \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{1-sin^2\theta cos^2\phi}}\begin{pmatrix} 0\\ cos\theta \\ -sin\theta sin\phi \end{pmatrix}$ 
where the prefactor is to properly normalize.

To make b orthormal, simply let $\hat{b}=\hat{r}\times\hat{a}= \hat{r}\times \hat{r}\times \hat{x}= (\hat{r} \cdot \hat{x}) \hat{r} -\hat{x}= \frac{1}{\sqrt{1-sin^2\theta cos^2\phi}}  \begin{pmatrix} sin^2\theta cos^2\phi -1  \\ sin^2\theta sin\phi cos\phi \\ sin\theta cos\theta cos\phi \end{pmatrix}$ 
where the normalization is necessarily the same.  Then, by definition, $$\tilde{Q} = \begin{pmatrix} <\hat{x}|\hat{r}> & <\hat{x}|\hat{a}> & <\hat{x}|\hat{b}> \\ <\hat{y}|\hat{r}> & <\hat{y}|\hat{a}> & <\hat{y}|\hat{b}> \\ <\hat{z}|\hat{r}> & <\hat{z}|\hat{a}> & <\hat{z}|\hat{b}>\end{pmatrix}$$  

$$\tilde{Q}= \begin{pmatrix} sin\theta cos\phi & 0 & \frac{sin^2\theta cos^2\phi -1}{\sqrt{1-sin^2\theta cos^2\phi}} \\ sin\theta sin\phi & \frac{cos\theta}{\sqrt{1-sin^2\theta cos^2\phi}} & \frac{sin^2\theta sin\phi cos\phi}{\sqrt{1-sin^2\theta cos^2\phi}} \\ cos\theta & \frac{-sin\theta sin\phi}{\sqrt{1-sin^2\theta cos^2\phi}} & \frac{sin\theta cos\theta cos\phi}{\sqrt{1-sin^2\theta cos^2\phi}} \end{pmatrix}$$

If the tangential momentum is t and the direction is governed by a random angle $\epsilon$, $$T_{tan}=\begin{pmatrix} 0 & 0 & 0\\ 0 & tcos^2\epsilon & 0 \\ 0 & 0 & t sin^2\epsilon\end{pmatrix} $$ and transforming, $T_{tan, rotated} = \tilde{Q} T_{tan} \tilde{Q}^T$

Once we compute the energy tensor of a merger, the goal is to extract the triaxiality coefficients, $a_i$. However, the eigenvalues of $E^{(tot)}_{ij}$ depend nontrivially on $A_i$. Instead of solving a horrendous multi level integral equation, it's much simpler to tabulate $\lambda_2(a_2, a_3) = \frac{a_2^2  A_2}{A_1},\quad
\lambda_3(a_2, a_3) = \frac{a_3^2  A_3}{A_1}$ for various values of $a_2, a_3$.  Then, an interpolation can give $a_2$ and $a_3$ to sufficient accuracy. Thanksfully, $\lambda_2 \textrm{ and } \lambda_3$ depend monotonically on $a_2 \textrm{ and } a_3$. Specifically, $\lambda_2 \sim (a_2, \frac{1}{a_3},) \textrm{ while } \lambda_3 \sim (\frac{1}{a_2}, a_3)$  

Now, this adequately represents the merger process itself, but this is not all that happens. Primarily, halo formation is a series of discrete mergers.  But, this is not all. Between mergers timescales bordering on a gigayear can take place. In these intervening times, the halo sphericalizes and accretes. Accretion is simpler to account for, since Andrew's code tabulates the mass difference for us. To update, we write $$E_{ij} = E_{ij} * \frac{[m_{out}/(m_1 + m_2)]^ 2} {(r_{out} / r_f)}$$
This distributes the new matter isotropically, which is a reasonable enough model(infalling matter, we would expect, is uncorrelated to the halo's orientation, especially because it is rotating).


The second effect to consider is sphericalization. As time passes, the halos slowly shifts towards a more perfect sphere. This is unsuprising because a spherical distribution minimizes energy.  However, unlike a viscous fluid or the matter of the earth, one might expect noninteracting dark matter to lack a mechanism of energy transfer. At 0th order this remains true(hence studying triaxiality at all). Beyond this, the velocities of the dm particles are not perfectly correlates, and as the halo rotates about it's internal axis, some particles can't quite "keep up". Then, it's perfectly reasonable that the time constant if sphericalization is based off the period. Denoting $\lambda = (\sum_i \lambda_i) / 3$ as the average, or fully sphericalized eigenvalues, we update: $$ \lambda_i \rightarrow \lambda + (\lambda_i - \lambda)e^{-\alpha \omega \Delta t }  $$
As we can see, this supresses an imbalances between coordinates, but only reaches a truly spherical halo asymptotically. During the formation period, mergers are frequent enough to disallow full sphericalization.  Before we define terms, a quick note that equitorial bulging is neglected here, either because it's infeasable for a dark matter distribution, or simply not a relevant enough effect.

Now, defining terms, $\Delta t$ is the time between mergers. $\alpha\sim1$ is a fine tuning constant, and $\omega$ is the rotational period of the halo. This last parameter comes out of the physics as $$\omega = \Omega(1-1/q),\\
q = (a_2a_3)^{-1/4}, \Omega = \sqrt{\frac{mg}{R_v^3}}$$
q comes from the flattening of the potential(we're averaging over directions 2 and 3), and $\Omega$ is the orbital period of the halo. 


## Useful Links

* Some nice [notes](https://people.ast.cam.ac.uk/~vasily/Lectures/SDSG/sdsg_5_coll.pdf) on the virial theorem (and related stuff) - starting at page 93.
 
* This [paper](https://arxiv.org/pdf/1804.00676.pdf) has a nice description of the triaxial NFW density profile that we'd use to model our halos - page 5, equation 9.
 
* This [paper](http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1962ApJ...136.1037C&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf) has a very complete and detailed discussion of the gravitational properties of triaxial systems. Section IVa defines the potential energy tensor, which is something we'd need to compute. This paper is very dense, but it's not necessary to understand all of it, just the parts relevant to the potential energy tensor.

* SciPy has implementations of various [elliptic integrals](https://docs.scipy.org/doc/scipy/reference/special.html#elliptic-functions-and-integrals) that might be useful for evaluating the $A_i$ quantities.

* Potential energy of a spherical NFW halo. This [paper](https://ui.adsabs.harvard.edu/abs/1998MNRAS.295..319M/abstract) has an analytic expression for this (equation 23). In this $r_{200}$ is the outer radius of the profile, and $c=r_{200}/r_\mathrm{s}$ where $r_\mathrm{s}$ is the scale radius.

* Papers measuring the distribution of halo shapes from N-body simulations:

  * [Despali et al. (2014)](https://ui.adsabs.harvard.edu/abs/2014MNRAS.443.3208D/abstract)
  * [Bonamigo et al. (2015)](https://ui.adsabs.harvard.edu/abs/2015MNRAS.449.3171B/abstract)
  * [Bett et al. (2007)](https://ui.adsabs.harvard.edu/abs/2007MNRAS.376..215B/abstract)

* Papers exploring correlations between halo shapes and formation history/mergers

  * [Lau et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.500.1029L/abstract)
  * [Morinaga & Tomoaki (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.495..502M/abstract)
  * [Drakos et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019MNRAS.487..993D/abstract)
  
 *Paper([here](https://core.ac.uk/download/pdf/83937594.pdf)) discussing the sphericalization timescales from Ana. 

## Questions and Thoughts
   None for now. 
## Potential Energy Tensor for Heterogeneous Density Distribution

In Chadrasekhar's book "Ellipsoidal Figures of Equilibrium" he derives the expression for the Newtonian potential, $\mathfrak{B}$, for an ellipsoidal density distribution. Here are photos of the relevant pages of the book:
![](https://i.imgur.com/JvvvjyF.jpg)
![](https://i.imgur.com/TlMMVW5.jpg)
![](https://i.imgur.com/xbXdEM2.jpg)
![](https://i.imgur.com/fmm3SSc.jpg)


Theorem 12 is the key final result, giving us the Newtonian potential, $\mathfrak{B}$, defined in terms of the coordinate $m^2$.

Earlier in his book he gives the definition of the potential energy tensor $\mathfrak{W}_{ij}$ in terms of the Newtonian potential (equation 18 in the following image):

![](https://i.imgur.com/nV2jFO3.jpg)

The same results (presented slightly more clearly maybe) are in Binney & Tremaine's book "Galactic Dynamics". Here's the relevant pages:

![](https://i.imgur.com/vTOoGtq.jpg)
![](https://i.imgur.com/rj1coJ6.jpg)

## Idealized N-body Simulations

I set up an ran an idealized N-body simulation of two dark matter halos about to merge. Specifically, this was a pair of halos of masses $10^{12}\mathrm{M}_\odot$ and $10^{11}\mathrm{M}_\odot$, initially both spherical, separated by 300kpc, and with relative velocity 100km/s directed along the line connecting their centers.

These were evolved for 20Gyr using the [Gadget](https://wwwmpa.mpa-garching.mpg.de/gadget/) code. I then measured the kinetic and potential energy tensors using [Galacticus](https://github.com/galacticusorg/galacticus) for the system at each timestep, and constructed the total energy tensor by summing these.

The following figure shows the components of the total energy tensor as a function of time (with the gray line showing the total energy - i.e. the trace of the energy tensor) as solid lines. The shaded region around each line indicates the uncertainty in the energy (due to the finite number of particles in the simulation; computed using bootstrap resampling). The dashed lines show the initial value of each component for reference.

![](https://i.imgur.com/tS3NDgI.png)

The total energy is conserved to good accuracy as expected.

The off-diagonal component of the energy tensor are all zero. This is expected as the initial system is aligned along the principal axes of our coordinate system.

The behavior for the on-diagonal elements is of most interest to us. Note that $E_{11}$ and $E_{22}$ are identical because of the symmetry of this simple example. A few key points:

* There is a clear transient behavior where the on-diagonal components fluctuate over the first ~2 Gyr. This seems reasonable as the system is not in equilibrium initially.

* After this transient phase the components of the total energy tensor return to their initial values. This is very important as it's a key assumption of our model (i.e. that the energy tensor is a conserved quantity, at least on certain timescales).

* On longer timescales the on-diagonal components are not conserved - $E_{00}$ increases and $E_{11}$ and $E_{22}$ decrease (as they must to ensure total energy is conserved). This suggests that the halo begins to "sphericalize" over some timescale. Although, it never seems to fully sphericalize, but instead seems to reach some equilibrium.

### Some Improvements

I made a couple improvements to this calculation:

* I shift into the frame where both the linear and angular momentum of the system is zero. Therefore, we ignore any net translation of the system and, if the system had a fixed shape but was simply rotating about an axis, we would be removing the contribution from that rotation (since what we care about here is the shape).
* The tensors are now rotated to the coordinate system aligned with the principal axes of the energy tensor. Specifically, after measuring that tensor I find its eigenvectors, and then apply a rotation to the tensors into the coordinate system defined by those eigenvectors. This ensures that the off-diagonal elements of the energy tensor are zero by construction. Again, this is useful here since what we really care about is the shape, not the orientation.

For the radial merger (shown in the figure above) nothing changes - it was already in the zero linear momentum frame,  had no angular momentum (since it was a radial merger), and was aligned with the coordinate system anyway:

![](https://i.imgur.com/UBYIjit.png)

But, I also now ran a similar model but with the initial velocity vector of the secondary halo making a $45^\circ$ angle to the radial line. So, the angular momentum is non-zero and the system can't stay aligned with the coordinate system axes. The results for this model are:

![](https://i.imgur.com/0AjRtgM.png)

(Note that the noise in the total energy increases slightly - this is because of numerical inaccuracies in the coordinate system transformations. Also note that at around 2Gyr the $E_{00}$ and $E_{11}$ components switch places - this is probably inevitable when the eigenvalues of the energy tensor corresponding to these two axes are very similar - small numerical variations will cause the ordering of the eigenvalues to change, resulting in the axes switching place. I don't think this is a problem for the analysis here, but if it turns out to be a problem we can just look for cases where this happens and change the order of the eigenvectors back to what it "should" be.)

This case is kind of interesting. The $E_{00}$ component is initially lower energy (due to the gravitational binding along that axis between the two halos). The $E_{11}$ component is initially slightly larger energy due to the kinetic energy of the secondary along that axis. After the merger these two components "mix" and are equal - this makes sense physically since the motion of the secondary is to orbit in the $01$ plane. There's also some change in the $E_{22}$ component - similar to the "sphericalization" seen in the radial case.


