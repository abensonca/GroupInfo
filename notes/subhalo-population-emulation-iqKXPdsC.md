**08/05/23**
- started using hackMD
- created SMF plot for CDM(), WDM(), CDMEmulator() and WDMEmulator() cases for both infall and bound masses

**08/07/23**
- attempted to create radial distribution plot. In my head I had thought that it would be a naturally decaying curve but when I created the plot it looked more like a cluttered scatter plot than anything else. 
- I re-ran normalizing_flows.py to get an updated version of the density plots. The goal is to look at the orbital radius scatter plot and compare it to the plot I made today. 

**08/08/23**
- code used to produce SMF's was not clean or flexible, I cleaned up the code so now It will produce plots of Galacticus and Emulator SMF's for any number of dark matter models simply by specifying which dark matter models to plot within the .sh file. ![](https://hackmd.io/_uploads/H1Jsqtenn.png)


    
    - it seems that for both infall and bound masses, the emulator is supressing the number of subhalos at larger masses relative to Galacticus.

**08/09/23**
- Modified how the Galacticus plots were produced so now there's more of an agreement between the two panels.
![](https://hackmd.io/_uploads/H1gZy6zn2.png)

**08/10/23**
- Fit the model for the $N(M)$ equation provided in the Aquarius paper.

![](https://hackmd.io/_uploads/rkMLLeQ3h.png)


**08/14/23**
- Fixed plot labels so that they include the value of the host mass in solar masses
- sent Andrew density plots for $10^{13} M_{\odot}$ host halo mass

**08/15/23**
- Included an extra plot that shows that SMF modeled by the Aquarius function:

$$ \frac{dN}{dM} = a_0 \bigg( \frac{M}{m_0} \bigg)^n $$

There's currently a bit of a disagreement because only a single realization of the subhalo population is being generated. 

**08/17/23**
* Had meeting with Andrew, will start including more daily scratch work on here.
* Given an array $x$, writing $x$ = [0,1,2,3,4,5] and then writing $x[:3]$ produces the array [0,1,2]. So in general if we want to find the first $N$ elements of an array, we would do $x[:N]$.
![](https://hackmd.io/_uploads/SkgPfy3nh.png)
* Trying to change to index within the for loop doesn't work:
![](https://hackmd.io/_uploads/SkeE7k232.png)
    * We see that it lowers the current index value of $i = 3$ to $i = 2$, but it doesn't carry that value into the next iteration of the for loop.
* changed the for loop in the code to a while loop so now we have: while $n<= \text{num_iterations}$. We made sure to include $n$+=1 within the loop.
    * We defined a new variable "$\text{sample_amount} = 1.5$" and sampling: $\text{sample_amount} \times N$ points. In the case where this isn't enough data points after the clip is applied, we increase the sample amount by 0.5 (so the next time we'll be sampling $2N$ points) and then continue to move onto the next iteration in the loop.
    * We made sure to include the $n$+=1 line after the continue statement so we don't increment the index in the case where we don't sample enough data points.
    
    
# Reading papers on RealNVP

**Background**

* The object we're interested in obtaining is the joint density of a distribution $p(\mathbf{x})$.

* There are two main models that use neural networks to estimate $p(\mathbf{x})$: autoregressive models and normalizing flows.

    * autoregressive models: overall density $p(\mathbf{x})$ can be expressed as a product of conditional densities.
    
    $$ p(\mathbf{x}) = \prod_i p(x_i | x_1, \dots, x_{i - 1}) $$
        NOTE: Each of the densities in the product are one dimensional, and the $x_i$ variable only depends on the $i - 1$ variables that came before it.
    
    * fun fact: the property that $x_i$ needs to depend on $x_1, \dots, x_{i - 1}$ is sometimes referred to as the "autoregressive dependency" or "autoregressive property"
        
    * normalizing flows: $p(\mathbf{x})$ is represented as a continuous, invertible transformation from some base density $\pi_u(\mathbf{u})$. This base density is chosen so that it can be easily sampled from (like a Gaussian in our case) regardless of what the input $\mathbf{u}$ is. If we call the transformation $f$, then what we're saying is:
    
    $$ \mathbf{x} = f(\mathbf{u}), \ \text{where} \ \mathbf{u} \sim \pi_u(\mathbf{u}) $$
    
    then the density we're interested in can be expressed as:
    
    $$ p(\mathbf{x}) = \pi_u(\mathbf{u}) \Bigg| \det \bigg( \frac{\partial f^{-1}}{\partial \mathbf{x}} \bigg) \Bigg| $$
    
**Masked Autoregressive Flow (MAF)**

* If we apply the above general framework of an autoregressive model to our problem, then the overall density $p(\mathbf{x})$ can be parameterized as a product of 1D Gaussians.

$$ p(x_i \mid x_1, \dots, x_{i = 1}) = \mathcal{N} \big(x_i \mid \mu_i, \exp(\alpha_i)^2 \big)$$

* This is how the density is computed. If we want to sample from this density (aka generate data), we would apply:

$$ x_i = u_i \exp(\alpha_i) + \mu_i $$

* where $\mu_i = f_{\mu_i}(x_1, \dots, x_{i - 1})$ and $\alpha_i = f_{\alpha_i}(x_1, \dots, x_{i - 1})$. 

    - The $f_{\mu_i}$ and $f_{\alpha_i}$ functions simply compute the mean and log of the standard deviation of the $x_i$ variable. This is why they depend on the $i - 1$ variables that come before it. Not sure why literature uses $\alpha$ instead of $\sigma$, but we'll go with it.
    - the $\mathbf{u} = (u_1, \dots, u_D)$ values are sampled from a standard normal distribution. They can be thought of as "noise" variables.
* This is all in the context of thinking about $p(\mathbf{x})$ as an autoregressive model. If we look at the $x_i = u_i \exp(\alpha_i) + \mu_i$ equation however, we see that we can also think about it as $\mathbf{x} = f(\mathbf{u})$. If we define $f$ this way, then we can also obtain $f^{-1}$ easily via:

$$ \mathbf{u} = f^{-1}(\mathbf{x}) \implies u_i = (x_i - \mu_i)\exp(-\alpha_i) $$

* It's not just invertible, it's also differentiable. We can apply the $f$ function to the following quantity:

$$ \Bigg| \det \bigg( \frac{\partial f^{-1}}{\partial \mathbf{x}} \bigg) \Bigg| = \exp \Bigg( - \sum_i \alpha_i \Bigg) $$

* Since $f$ is both invertible and differentiable, the autoregressive model framework that we started with can also be interpreted as a normalizing flows framework!

**08/18/23**
- Filled out PHYS-590 research contract for upcoming semester
- got Github set up on mies

# Reading papers on RealNVP

**Masked Autoregressive Flow (MAF)**

- What we've done is rewrite the autoregressive model in the normalizing flow framework for a single function $\mathbf{x} = f(\mathbf{u})$, where:

$$ x_i = u_i \exp(\alpha_i) + \mu_i $$

* We know that normalizing flows algorithms apply many of these functions consecutively to obtain a flow. So for every function in a normalizing flow, we would need a corresponding autoregressive model at each layer of the flow.
    * Hopefully it makes sense too that the more $f$ functions we have in the normalizing flows algorithm, the more flexible it becomes.
    
* Terminology I should probably know (ultimately want to understand threads):
    * foward pass (or just pass): the flow of information starting at the input and ending at the output of a function.
    * CPU: the "brain" of the computer that carries out instructions and processes stuff
    * CPU cores: number of cores = number of tasks that can be executed at once
    * CPU Threads: a sequence of instructions given to the CPU by some program. The more threads a CPU can execute, the more it can multitask.
        * so essentially more threads doesn't automatically mean a CPU can multitask more. It just means it has more instructions to compute. I'm imagining threads in a spider web: the more threads there are, the more work needs to be done to get rid of a spider web.
* With MAF, the $f_{\mu_i}$ and $f_{\alpha_i}$ functions get calculated in a single pass where the input of the pass is $\mathbf{x} = (x_1, \dots, x_D)$ and the output of the pass is each of those functions.  
    * The reason why they use the term "masked" in MAF is because an approach called Masked Autoencoder for Distribution Estimation (MADE) covers up any parts of the input vector using boolean masks. For example, when calculating $x_i$, the quantity $x_{i + 1}$ gets masked and is not used in order to uphold the autoregressive property.
    * MADE applies this masking process for a single function. Get a bunch of layers of MADE's and you have a Masked Autoregressive Flow where the MADE's act as the individual layers of the flow.
    
**Inverse Autoregressive Flow (IAF)** 

* Inverse Autoregressive flows still use MADE's as the layers of the flow. and the $x_i = u_i \exp(\alpha_i) + \mu_i$ relation is still the same. The only difference here is how the $\alpha_i, \mu_i$ variables are defined:

$$ \alpha_i = f_{\alpha_i}(u_1, \dots, u_{i - 1}) \hspace{3ex} \mu_i = f_{\mu_i}(u_1, \dots, u_{i - 1}) $$

* Essentially, we see that the functions now depend on the $u$ variables rather than the $x$ variables. 
* MAF and IAF have different benefits/drawbacks:
    * MAF pro: it can find the density $p(\mathbf{x})$ for any data point $\mathbf{x}$ in the parameter space in a single pass.

    * MAF con: generating data points $\mathbf{x}$ from the density $p(\mathbf{x})$ requires $D$ passes
    
    * IAF pro: It can generate sets of data points $\mathbf{x}$ as well as the density $p(\mathbf{x})$ of those generated points with a single pass.
    
    * IAF con: Calculating the density $p(\mathbf{x})$ of a data point not created in the original sample requires $D$ passes to find the random numbers $\mathbf{u}$ associated with the outside data point $\mathbf{x}$.
    
**08/19/23**
# Reading papers on RealNVP

* When to use MAF versus IAF:

    * use IAF for model recognition. When you already have an established set of data points, and you're only interested in calculating the density of that sample.
    
    * use MAF for density estimation. If we wanted to estimate a density, we wouldn't have enough data points $\mathbf{x}$ to establish the density $p(\mathbf{x})$. Cause if we had the density evaluated at enough data points we would already have it, there would be no need to estimate in the first place. So even if we have a set of pre-existing data points, we it will require that we sample outside of that data set. Hence MAF is better.
    
    * an even more concise way of putting it: MAF trains quickly but samples slowly, IAF samples quickly but trains slowly.
    
* MAF and IAF are related: the inverse pass of the IAF is equivalent to the forwards pass of the MAF. 

**RealNVP** (finally!)

- RealNVP (Real Non Volume Preserving) flow is a special type of the IAF bijector. 

- With the standard IAF, here was the picture relating the data points $\mathbf{x}$ to the noise data $\mathbf{u}$:

![](https://hackmd.io/_uploads/BkZu0r-63.png)

We see that the $x_i$ data points depends on the previous $u_1, \dots, u_{i - 1}. This process occurs all the way through $x_D$. 

- With the RealNVP case however, the picture gets slightly modified:

![](https://hackmd.io/_uploads/H1__yU-6n.png)

* We now choose some $0 < d < D$ where we have $x_{d + 1}$ depend on the previous $u_1, \dots, u_d$ values, but then the twist is that $x_{d + 2}, x_{d + 3}, \dots x_D$ also depend on the same $u_1, \dots, u_d$ values. 

* The disadvantage of using IAF was that sampling an extra data point was inefficient. In other words if $x_1, \dots, x_d$ was our sample, then through the standard IAF sampling $x_{d + 1}$ should be inefficient because you would need to learn all $\alpha_1, \dots, \alpha_{d}$ and $\mu_1, \dots, \mu_d$ values first. 

* Now though if we already have $x_1, \dots, x_d$ data points then the $\alpha, \mu$ parameters are already computed. So if $x_{d + 1}, \dots, x_D$ only depend on the previously computed parameters, then we can compute the remaining external data in only a single pass!
    * Another way of saying this is that $\alpha_{d + 1}, \dots, \alpha_D$ and $\mu_{d + 1}, \dots, \mu_D$ can be computed in a single pass.
    
* Next part: specifically for RealNVP, it defines $x_i = u_i$ for $i = 1, \dots, d$. Since for both the MAF and IAF we have:

$$ x_i = u_i \exp(\alpha_i) + \mu_i $$

if we set $\alpha_i = \mu_i = 0$ then we get that $x_i = u_i$. So regardless of what the $\alpha_i, \mu_i$ depend on (whether it's the $x$'s for MAF or the $u$'s for IAF), if we set them to zero then we get the special case of the RealNVP. 
    * Basically RealNVP can be thought of as a specific case of both MAF and IAF
    
* Benefit of using RealNVP: both sampling and density estimation can be performed in a single pass, so it combines the best of both words from MAF and IAF.

**08/22/23**

* Just got code debugged for the SMF plots that takes a while to run so I'm sure that part works now. So now I'm working on two copies of the script, one which debugs the later parts of the code (but takes a while to run), and one which focuses on speeding up the slow generating part of the code.
* Within the code, there is a function called `emulator.distribution.sample(x)` which produces a sample of `x` subhalos. If we append this to an empty list, fortunately the list structure will not be a single array of size $x_1 + x_2 + \dots + x_\text{num_iterations}$, but rather nested list. The each element in the overall list of samples is itself a list of subhalo populations. So we should just be able to loop over the size of that list when applying the `norm_transform_inv` function.
* current error: once I have my list of lists (called `samples`), when I try to apply the `predict` function outside of the for loop I get an error because `predict` only acts on a single array rather than an array of arrays.
    * idea: save sizes of each individual array within `samples`, then take `samples` and reconstruct it so it's only a single array of every subhalo from each of the generated subhalo populations. Then apply `emulator.predict(samples)` so the function is applied to an array of a fixed size. Then resort elements back into their original subhalo populations since we saved the sizes as a first step.

* afternoon update: 
    * the code that takes a long time to run (called `smf_plots.py`) is about 10 hours into running. It should be done soon with hopefully no bugs. 
    * I edited the copied version of the code which is trying to perform the `predict` function outside of the for loop. I set it for only 5 runs to keep computation time short. I tried running it and it was taking over an hour so put in comments/time stamps and started an interactive script. Currently debugging that.
    * We see that applying the `sampling` function is almost instant. 
    * If I understand correctly, the time listed should be total CPU time rather than real time running, because it only took about a minute to get this part of the output message.
    
    ![](https://hackmd.io/_uploads/HkWgMRGph.png)

* The predicting of the samples seems to be taking a while. I know from previous errors that there are ~100,000 subhalos in a given iteration, so this code is predicting roughly 500,000 samples.

* We know it's purely within the `predict` part of the function, because here's the code in between time stamps:

![](https://hackmd.io/_uploads/rJllXCzTn.png)

* I tried running only a single realization of a subhalo population, and got some complicated error:

![](https://hackmd.io/_uploads/BJ2mmZXp3.png)

* I'm not sure exactly what's wrong, but it's in the part once I'm done sampling in the `predict` function outside of the loop. 


**08/23/23**

* I think I might've partially figured out why the main script was taking so long! I had this line in the code to account for if not enough data points were being sampled:

![](https://hackmd.io/_uploads/ByJGnD7a2.png)

However `sample_amount` was defined inside the for loop, so when I break to the next iteration, it goes back to the starting value, despite the fact that I updated it in the conditional. Will try reruning things and see what happens.

* I also just realized that the sampling for the `CDM_cat` model takes quite a bit longer than the `CDM` model which might be why the computation time is so long. There were multiple times that we had to increase the sample size for the Caterpillar data set.

* The original code (the one that keeps both `sampling` and `predict` inside the for loop) is fully debugged! I'm running the full script now. It will take a while but it fully executed for 2 runs so it will also execute for `countTree` runs. I will also make a timestamp to see exactly how long the full script takes. 

* In the mean time, I'll work on the copied script where `predict` is outside the for loop. Once I debug that, I'll run the same script and compare run times to see if it makes much of a difference. 

**08/24/23**

* So the main script that's supposed to take a while is still running. I knew it would take a long time, but it's never taken this long. 

    * Previously I was sampling $\text{sample_amount} \cdot N$ points where we initially set $\text{sample_amount} = 1.5$ and if not enough points were selected after clipping we would select another $1.5N$ points.
    
    * In the new iteration, I'm starting at $1.5N$ points, but then if not enough points are being sampled in *any* iteration, I increment $\text{sample_amount}$ by $0.5$. So I think a quicker alternative is to have it increment by $0.5$ for a given iteration of a subhalo population, but when we produce a new iteration we reset the starting value at $1.5$. I'm looking into other possible reasons right now
    
* Andrew and I talked over slack about some possible fixes for why the code is inefficient. To summarize, we confirmed that the fluctuations and randomized starting values of the curve were due to a low number of subhalo population iterations generated from the emulator.

* We plotted a curve directly comparing the differences in the SMF between Galacticus and the emulator:

![](https://hackmd.io/_uploads/HyVWW5B63.png)

**08/25/23**

* We updated the `darkMatterOnlySubHalosCDM_cat.xml` file so that the host halo mass was fixed rather than varying from a range of masses. When we updated the file and produced the new SMF plots, we got:

![](https://hackmd.io/_uploads/SJRjBFUp2.png)

* There doesn't seem to be a noticeable difference other than the fact that the Aquarius model now fits the Galacticus bound mass better. 
    * I thought the Aquarius model was supposed to model infall masses though? So maybe I'm missing something
    
* Current scripts running:
    * `normalizing_flows.py` which is going to relearn the weights as well as save the necessary data file so that we can get new SMF curves for the fixed caterpillar mass host halo.
    * We're running Galacticus for a $10^{13} M_\odot$ host halo mass but we're modifying how Galacticus performs sampling. In line 120 in the code, we changed the parameter `exponent` = 1 to `exponent` = 2. Once this is done running, we'll relearn the weights for this model. 
    
* goal: (Once I'm feeling less sick which is hopefully by early next week): read through arXiv abstracts for 30ish minutes a day, pick one paper to read per week and write out summary of paper here.

**08/26/23**

* currently running `normalizing_flows.py` to learn the weights for the updated Galacticus model for a $10^{13} M_\odot$ host halo mass where `exponent` = 2. 

* Here is the updated SMF plot for the Caterpillar host mass halo:

![](https://hackmd.io/_uploads/ryBgi6D62.png)

**08/27/23**

* We just made the plots for the $10^{13} M_\odot$ host halo where we set `exponent` = 2. Here are the SMF curves:![](https://hackmd.io/_uploads/HJTCuZF6h.png)

    * Especially after looking at this plot, I realized I should be saving each set of weights every time I adjust a Galacticus parameter. I say this because the weights for this case overrode the `exponent` = 1 case. So I'm gonna save the current weights that produced the above plots, and then run the code again to have the `exponent` = 1 weights so I have both sets going forwards.
    
**08/28/23**

* paper for the week: Cluster halo shapes in CDM and SIDM models: Unveiling the DM particle nature using a weak lensing approach
    * I'm going to take specific notes on the papers on my iPad because that's where I have notes for my other papers I've read. Also I feel it clutters up this space. 
    * I'll still write here about main results from paper or what portion I've read that day.
* Confirmed that the transformations from the input (non-normalized) data to the normalized data and vice versa work correctly.
* We tried to remove subampling from the Galacticus `darkMatterOnlySubHalosCDM.xml` file so that every input had the same weight. When we tried to run the `normalizing_flows.py` script, we got the following error:

![](https://hackmd.io/_uploads/Hk-TVys6h.png)

Fortunately the weights get fully learned and saved by the time this error occurs so we don't have to run the full script in order to debug.

**08/29/23**

* We ended up creating the SMF curves that do not include subsampling with a mass resolution of $10^9 M_\odot$, and here's what we got:

![](https://hackmd.io/_uploads/SJcsm9iT2.png)

* Since the mass resolution is $10^9 M _\odot$, we would expect the curves to be flat up until the $10^9$ point on the x-axis.
* We then increased the number of emulator produced realizations from 10 to 1000 to see if the vertical discrepancy goes away, and zoomed in on the plot to look at the non-horizontal parts of the curves:

![](https://hackmd.io/_uploads/Sk4q_ojph.png)

* We see that the curves match really well still aside from the vertical discrepancy that we still need to figure out. 

* just finished running the `darkMatterOnlySubHalosCDM.hdf5` file with a mass resolution of $10^8 M_\odot$. The `.xml` file took a decent amount of time to run, and the `normalizing_flows.py` script to learn the weights is also taking a while (current run time is 5.5 hours). 

* I'm reading through the halo shape paper in the meantime. I'm studying at a coffeeshop and forgot my charger so I'm only using my laptop periodically to check the code and write updates here.

* I think I can finish the paper by tonight, I'll write the summary either when I get home tonight or tomorrow morning.

**08/30/23**
* The `normalizing_flows.py` script took a little while to run but the weights got learned/saved, so now I'm running `smf_plots.py` to see the plots for if we don't sample with weights with a resolution of $10^8 M_\odot$. 

### Summary of Cluster halo shapes in CDM and SIDM models paper

* CDM and SIDM are different dark matter models, and one of the primary signatures for how the models differ is by looking at density profiles of galaxies. 
    * The SIDM curve is flatter (aka less dense) at innermost radii due to self interactions. These interactions prevent dark matter from clustering together as much.
    
* Another way of distinguishing between models (and the main topic of the paper) is by the physical shape of a dark matter halo. 

* In order to measure the physical shape of a halo, people would have previously have used a strong lensing approach.
    * The limitations of this approach are:
        * Measurements are limited to the innermost region of a halo (where the most baryonic interactions occur in order to produce strong gravitatonal lensing),
        * The strong lensing signal can get convoluted with effects produced by external baryonic interactions (interactions not necessarily contributing to strong lensing).
        
* Therefore the paper looks at the shape of halos using weak gravitational lensing. This approach allows us to use the entire halo for observational data rather than just the innermost approach.

* The signal from weak lensing is inherently weaker than from strong lensing, so the authors use a stacking technique (known as galaxy-galaxy lensing) to amplify the signal.
    * basic idea: add together weak lensing signals from halos are added together if the halos share a common parameter with one another (i.e. similar surface density, similar X-ray luminosity, etc.)
    
* The paper defines "halo shape" in a mathematical way. If you were to observe any halo from Earth, you could make a 2D plane perpendicular to the line of sight for each halo. The halo in this plane could then be represented by a semi-major axis $a$ and a semi-minor axis $b$. You can divide the two to get the semi-major ratio:

$$ q \equiv \frac{b}{a} $$

* While the $a,b$ values are fixed for a given halo, they will vary if you wish to find their value at some distance from the center of the halo. We call this distance $r$. It turns out that $q$ can be modeled as a function of $r$ as 

$$ q(r) = q_0 r^\alpha $$

for some parameters $q_0, \alpha$. One of the main plots of the paper showed the difference between $q(r)$ curves for the two dark matter models. Each of the different subplots slightly varies the $q_0,\alpha$ parameters.

![](https://hackmd.io/_uploads/ByCAFWTah.png)

The grey curve is the CDM model and the pink curve is the SIDM model. Apart from the obvious fact that in each plot the pink curve is higher than the grey curve, they make note of the fact that the pink curve is also slightly more rounded than the grey curve. This can be seen quantitatively in the differing $\alpha$ values in each subplot.

* That's pretty much the main idea: the paper says the two models have observational differences, here's what those differences will look like quantitatively, and the analysis technique for observing these differences is through weak gravitational lensing.

### End of Summary

* Next paper: Ethan's paper that came out 2 days ago. Title: Novel Conservative Methods for Adaptive Force Softening in Collisionless and Multi-Species N-Body Simulations

* useful software: plotdigitizer

**08/31/23**

* Reran Galacticus for the WDM model but this time we included no weighted subsampling and a mass resolution of $10^8 M_\odot$. We're doing this because the SMF curves seemed to match well when we did the for the CDM model

* Now running `normalizing_flows.py` for WDM to relearn the emulator weights.

* Running the script to reproduce the SMF curves for the CDM model but this time zoomed out. Right now the plots seem to match, but we're only zooming in on the high mass region of the plot:

![](https://hackmd.io/_uploads/S1XSJvCp2.png)

**09/04/23**

* I'm running a script that's comparing Galacticus density plots where one set of plots includes subsampling and one does not. 

* The reference on how the normalizing flows algorithm actually gets implemented links a paper called: "Density Estimation Using RealNVP". I'm going to go through that paper and learn about how I can modify the code to make the algorithm more flexible
    * One immediate thought in my head is that I know the deeper a neural network is (the more layers it contains), the more flexible the model becomes. I'm gonna try adding another layer to the network and learn the weights for the CDM Galacticus model with subsampling with a mass resolution of $10^6 M_\odot$ and see what happens.
    
* I'll write down any points of interest here from the paper so we both can benefit from understanding them. 

## Summary Results from "Density Estimation Using RealNVP" paper (part 1/2)

* Transformation from latent (simplified Gaussian) space to data (Galacticus) space is:

$$ p_X(x) = p_Z \big( f(x) \big) \Bigg| \det \bigg( \frac{\partial f(x)}{\partial x^T} \bigg) \Bigg| $$

* The function $f: X \to Z$ is what we're creating with the emulator, and we want this to be flexible and easy to manipulate.

* With this goal in mind for $f$, we construct $f$ by combining a bunch of simple invertible functions. These functions are referred to as "affine coupling layers" in the code.

* given an input vector $\mathbf{x}$ which is $D$ dimensional, we can break the vector into two parts.

$$ \mathbf{x} = (\underbrace{x_1, \dots, x_d}_\text{first part}, \underbrace{x_{d + 1}, \dots, x_D}_\text{second part}) $$

* When a single coupling layer acts on $\mathbf{x}$ to produce an output vector $\mathbf{y}$, the transformation is:

$$ \begin{cases}
    y_{1:d} = x_{1:d} \\
    y_{d + 1:D} = x_{d + 1:D} \cdot \exp \big(s(x_{1:d}) \big) + t(x_{1:d})\\
\end{cases}
$$

and its inverse

$$ \begin{cases}
    x_{1:d} = y_{1:d} \\
    x_{d + 1:D} = \big( y_{d + 1:D} - t(y_{1:d}) \big) \cdot \exp \big(-s(y_{1:d}) \big)
    \end{cases}
$$

* Computing coupling layer forwards and backwards requires same amount of computational time.


* The $s,t: \mathbb{R}^d \to \mathbb{R}^{D - d}$ functions are the same $s,t$ functions that show up in the `Coupling` function within our code.

* Jacobian of this `Coupling` function is:

$$ \frac{\partial y}{\partial x^T} = \begin{bmatrix}
    I_d & 0 \\
    \frac{\partial y_{d + 1:D}}{\partial x^T_{1:d}} & \text{diag} \big( \exp \big[ s(x_{1:d}) \big] \big) \\
    \end{bmatrix}
$$
 
* There's a lot of details in there, but the determinant of the matrix is quick to compute (which is why we're composing $f$ of these `Coupling` functions in the first place). Its form is:

$$ \det \bigg( \frac{\partial y}{\partial x^T} \bigg) = \exp \Bigg[ \sum_{j = d + 1}^D s_j(x_{1:d}) \Bigg] $$

* Important point: since the determinant doesn't depend on computing the Jacobian of $s$ and $t$, these functions can be arbitrarily complex without significantly increasing computational time. 
    * So we have a lot of freedom in testing different $s,t$ functions.
    
## Ending Summary results for today, will finish tomorrow

* Scripts are taking a little while to run, but at least they're running successfully. I'm running a script to look at the SMF curves now for a CDM model with subsampling, but weights learned from a deeper neural network (1 additional coupling layer). 

**09/05/23**

* still wrapping my head around last part of paper, will update when I can clearly express ideas.

* The script that produces the SMF curves for a neural networks with 1 additional coupling layer completed, but when I copied/pasted the additional layer I copied the final layer. Apparently the final layer has a different structure from all of the intermediate layers so the results didn't turn out right: 

![](https://hackmd.io/_uploads/HJPIMvBCh.png)

I'm rerunning the script now where I copied an additional intermediate layer so the results should turn out (hopefully) more accurate with the additional layer added.

* Something goes wrong with adding an additional layer that's deeper than just changing 1 or 2 lines of code. Here's the error message:

![](https://hackmd.io/_uploads/SkNUWhHA2.png)


## Summarizing results of "Density Estimation Using RealNVP" paper (part 2/2)

The masks that get applied are represented by a $D$ dimensional binary mask $\mathbf{b}$. For an input vector $\mathbf{x}$ and an output vector $\mathbf{y}$, the mask gets applied as follows:

$$ \mathbf{y} = \mathbf{b} \cdot \mathbf{x} + (1 - \mathbf{b}) \Big( \mathbf{x} \cdot \exp \big(s(\mathbf{b} \cdot \mathbf{x}) \big) + t(\mathbf{b} \cdot \mathbf{x}) \Big) $$

* The binary mask can be used to help us split how each coupling layer gets applied to the two parts of the input array $\mathbf{x}$.

* What was described earlier in this `HackMD`entry was for a single coupling layer. We now go into the details for how multiple coupling layers get applied.
    * If the overall transformation is $f$, then each coupling individual coupling layer will be denoted as $f^{(i)}$
    
* We know from how the `Coupling` function was defined that the first $d$ components of $\mathbf{x}$ stays fixed while the remaining $D - d$ components get modified. Apparently this is an issue to implement with multiple layers? (not sure why). So to fix this supposed issue, if $x_i$ stays fixed going through one layer, it will get modified in the next one, and vice versa:

![](https://hackmd.io/_uploads/HyG6KvrC3.png)

* From what I understand, layers get implemented this way in order for the determinant of the Jacobian to remain tractable.

* NOTE: This next part is slightly confusing for me because I believe they're using the term "layer" in two different contexts. If I understand correctly, layer refers to the `Coupling` functions that $f$ is composed of, and it also refers to the hidden layers within each `Coupling` function.

* The paper describes a 3 step "coupling-squeezing-coupling" process that's applied *per* layer. So I'm thinking that each $f^{(i)}$ (each `Coupling` function) is what's denoted as a layer in the neural network.

* the three step process:
    * step 1: Three coupling layers are applied using a mask $\mathbf{b}$ called a "checkerboard mask".
    * step 2: a squeezing algorithm which turns an $s \times s \times c$ object into an $s/2 \times s/2 \times 4c$ object (will provide diagram). For example, a $4\times4\times1$ object will get transformed into a $2\times2\times4$ object. Spatial size is being traded for number of channels.
    * step 3: three coupling layers are applied using a mask $\mathbf{b} called a "channel wise mask".
    
* diagram laying out these three steps. Left image is step 1 applying checkerboard mask, right image combines step 2 squeezing and step 3 applying channel wise mask. (dark means $b_i = 1$, light means $b_i = 0$): 

![](https://hackmd.io/_uploads/B1lROOrRh.png)

* The whole reason for applying this three step process in each layer is because it can take a while to pass a $D$ dimensional input vector $\mathbf{x}$ through each layer. Here's the diagram they provide to show how the number of variables decreases as $\mathbf{x}$ gets passed through increasingly more layers.

![](https://hackmd.io/_uploads/B1SnXnS03.png)

* in diagram: $x$'s are inputs, shaded $z$'s are inputs that get modeled as Gaussians, and $h$'s are hidden layer variables. As the three step process gets applied to $f^{(1)}$ then $f^{(2)}$ then $f^{(3)}$ and so on, the size of the input vector $\mathbf{x} = (x_1, \dots, x_D)$ continues to shrink and the number of hidden layers increases. 
    * I'm thinking because the size of our data vector is only 6 dimensions (for a given subhalo), maybe this three step process isn't necessarily going to significantly cut computation time?
    
**09/06/23**

* We tried modifying the `normalizing_flows.py` script so that no subsampling occurs within the algorithm itself, but rather is purely learned and we attempt to recreate the weights by adding an additional parameter to be learned (so now for each subhalo we have the 6 standard parameters plus the weight parameter)
    * the changes are made in a copied version of this script which we're calling `normalizing_flows_test.py`

* When we attempt to modify the `log_loss` function, we get some sort of error. Here is the `log_loss` function before modifying it:

```
 def log_loss(self, data):
        x = data[:,0:-1]
        w = data[:,-1]
        m = data[:,0]
        y, logdet = self(x)
        log_likelihood = (self.distribution.log_prob(y) + logdet)*w
        return -tf.reduce_mean(log_likelihood)
```

and here's the function after modifying it: 

```
def log_loss(self, x):
        y, logdet = self(x)
        log_likelihood = self.distribution.log_prob(y) + logdet
        return -tf.reduce_mean(log_likelihood)
```

* I think the issue is that before, `x` was defined as a specific part of the original data array (specifically `x = data[:,0:-1]`, whereas now we just have `x = data`). 

**09/07/23**

* Figured out the bug from yesterday. I'm continuing to debug, but I think I have it figured out adding an extra parameter (the subhalo weight) to be learned. 

* For future reference if we want to learn an $N$ parameter distribution:
    * within `class RealNVP`, change `self.distribution` so that `loc` is an $N$ sized array of 0's, and `scale_diag` is an $N$ sized array of 1's.
    * `self.masks` is a numpy array of lists whose elements alternate between 1's and 0's. For $N$ parameters we want $N$ different lists, and each list has $N$ elements.
    * right below `self.masks` there's an attribute called `self.layers_list`, which for $N$ parameters should be: `self.layers_list = [Coupling[N] for i in range(num_coupling_layers)]`
        
* I'm realizing as I'm reading through arXiv paper abstracts that it would be beneficial if I had more knowledge on galaxies in general. While I'm letting scripts run, in addition to reading 1 paper per week, I'm going to read through and take notes on Binney's Galactic Dynamics. I'll be LaTeXing the notes separately and only writing here which sections I covered that day to not make this space too cluttered.

* adding the weights as a parameter is fully debugged, and the script `normalizing_flows_test.py` is running to obtain the learned weights. Once this is finished, we'll produce the SMF curves and see what we get. 

**09/11/23**

* The weights are successfully learned from `normalizing_flows.py`.

* When I try to produce the SMF curves, I'm getting some weird error with with defining the negative binomial distribution variables. I'm working on debugging that now. 

* Finished reading/taking notes through section 1.1 of Binney's Galactic Dynamics (45 pages).

**09/12/23**

* I just realized that when I imported the `RealNVP` class into my `smf_plots.py` script, I was importing it from `normalizing_flows.py` rather than `normalizing_flows_test.py`. That might be why the code is crashing. I'm running that now to see how things change. 

* Part of the reason things were crashing is because when weights were introduced, numbers were added in the `necessary_data` file which included exponents (for example: 1.6e-06). The code crashed because it couldn't rewrite the number as a string with the "e-" in it.
    * This can get fixed by including a line at the beginning of the script right after `import numpy as np` where you include: `np.set_printoptions(suppress=True)`. This removes scientific notation from all of the floats in the script (up to a certain number of decimal places).
    
* Next issue: when we add a 7th dimension, the minimum and maximum 7D data points get saved in two columns in the `.txt` file as opposed to a single line in 6D. 
    * For now, I'm just manually editing the `.txt` file to keep debugging, but I will have to fix that at some point so that the `necessary_data.txt` file is saved in the correct format.
    
**09/13/23**

* Figured out the issue where `np.arange` had an array value error. Now the `smf_plots.py` code fully executes!
    * next: run `normalizing_flows_test.py` for 200 epochs to get the full version of the 7D weights, then run `smf_plots.py` to look at its SMF curves.
    
**09/14/23**

* We got the SMF curves for the new approach, and the results don't look ideal: ![](https://hackmd.io/_uploads/SkQHmb-yT.png)

* We're now looking at density plots which include the Galacticus subhalo weights to see if the emulator is learning the distribution correctly.

* So I'm not sure what happened, but the density plots don't look good:

![](https://hackmd.io/_uploads/r1ZvNzbk6.png)

* I checked and confirmed that the same number of points are being plotted for Galacticus and the emulator.

* All this was when I was running the `normalizing_flows_test.py` script. I'm now creating density plots using the same weights, but this time with the `normalizing_flows.py` script. The goal here is to see if there's something wrong with the test script. 
    * Nevermind, I can't apply 7D weights to the 6D script. I guess that makes sense.
    
**09/15/23**

* Had meeting with Andrew, the `normalizing_flows.py` script didn't seem to be working which was very concerning. We had thought that part had been figured out. 
    * I ended up just commenting out a line in the code, but it should work fine now.

* The density plot posted here yesterday was produced with subsampling, it looks much better without subsampling:

![](https://hackmd.io/_uploads/rkqKnNGkp.png)

* This was just a matter of removing `p = w/np.sum(w)` in the `subampling` line of the code. 

**09/18/23**

* On Friday, we found out that the emulator has a difficult time learning the subhalo weights because of a sharp peak in the histogram:

![](https://hackmd.io/_uploads/B1KZ5fU16.png)

* We tried taking the log of the weight to see if that helps, but the code crashed in the plots for some reason. We're debugging that now.
    * For some reason, `normalizing_flows_test.py` was initially crashing. I tried running `normalizing_flows.py` for 2 learned epochs and that worked fine. Then I ran `normalizing_flows_test.py` for 2 iterations and that worked. I'm not sure why. Currently running `normalizing_flows_test.py` for 200 iterations since it's hopefully working now.
    
**09/19/23**

* The updated density plots came through and the results look much better!

![](https://hackmd.io/_uploads/rydjwPDyp.png)

![](https://hackmd.io/_uploads/B1QRvvP1p.png)

* Weird bug: the `normalizing_flows_test.py` script crashes when I run it as a regular script, but it executes fine when I run it as an interactive script

* Unfortunately, while the subhalo weights look better, the SMF curves coming from `smf_plots.py` still don't look good.
    * attempt at solution: rather than apply Monte Carlo condition in `xt[clip]`, we'll include the weights directly when constructing the histograms (aka the y-axis for the SMF plots). This is how we already include the weights for Galacticus. 
    
**09/20/23**

* error when trying solution: the line that constructs the y-axis of the SMF plots is:

```
em_infall = np.cumsum(np.histogram(em_massInfall,mass,weights=max_weight*10**xt[:,-1])[0][::-1])[::-1]/num_iterations
```

right now, `em_massInfall` and `xt` are different sizes. Gonna figure out why.

**09/25/23**

* Computer parts are coming in, but I have an external keyboard so I can keep working in the meantime.

* When trying the approach of including `(r < 10**xt[:,-1])` in the clip, here's what the SMF curves look like: ![](https://hackmd.io/_uploads/BkBbvBJlp.png)

* So now we're going to try the approach where we read in the emulator weights using the same syntax that we'd use to read in the Galacticus weights.
    * When we try this, we get some weird looking SMF curves:
    
    ![](https://hackmd.io/_uploads/BySuQL1l6.png)

* When we don't include the  `(r < 10**xt[:,-1])` condition in the clip, we get essentially the same plot. This seems odd.. 

![](https://hackmd.io/_uploads/S1_RPUye6.png)

* Note to future self: Don't make density plots of large arrays, it takes a while to compute.

**09/26/23**

* I'm going to make a list of what quantities match up so I have everything written down. Within `test_2.py`:
    * Histograms match for `weightsNormalized` and `em_weights[0:len(weightNormalized)]` when `em_weights` is set to be the normalized values.![](https://hackmd.io/_uploads/SJLzOAglT.png)
    
     * The `[0:len(weightNormalized)]` is just to ensure we have the same sample sizes. 
     
* Everything matches when we raise things to the 10th power: 

![](https://hackmd.io/_uploads/HJjqfJbgp.png)

And finally, we see an agreement between `w` and `em_weights`. ![](https://hackmd.io/_uploads/BypG6JZxa.png)

* This tells us that the difference in SMF curves is not due to the weights being used. 

* Just finished reading through chapter 1 of Binney's "Galactic Dynamics". Onto Chapter 2..

* There are significantly more emulator data points than Galacticus data points. This is because we're appending 200 realizations worth of data points together. If we plot the first $N$ data points from the emulator where $N$ is the number of Galacticus data points, we get that the infall mass and bound mass histograms match:  

![](https://hackmd.io/_uploads/SyhdcI-x6.png)
![](https://hackmd.io/_uploads/Sk2qMvblp.png)
NOTE: the bottom histogram plot is for the bound mass, I just forgot to change the title!!

**09/28/23**

* We made plots showing the distribution of infall/bound masses and weights for when each subhalo realization generated by the emulator had the same number of subhalos in a Galacticus subhalo population. We got good results!

![](https://hackmd.io/_uploads/HkAh1umea.png)
![](https://hackmd.io/_uploads/SJ031O7ea.png)
![](https://hackmd.io/_uploads/r1C2J_Ql6.png)

* NOTE: The distributions here *do not* include weights. Next test is to see what happens when we include weights in the distribution. 
    
* Ok things don't work as well once we include weights in histograms for infall and bound masses:

![](https://hackmd.io/_uploads/BkjCN_7ea.png)
![](https://hackmd.io/_uploads/SJiCEO7gp.png)

**09/29/23**

* In the meeting with Andrew, we realized we were not applying the `subhalos` clip to the subhalo weights in the `normalizing_flows_test.py` script. We're going to try that to see how that fixes things.

**10/02/23**

* Laptop is finally fixed! The keyboard got replaced and everything is working great again. Very excited to get back into things normally!

* Density plots came back and look good!

![](https://hackmd.io/_uploads/S17vOd_l6.png)

* The SMF curves came back and they look great!! With the normalization constant applied, here are the results:

![](https://hackmd.io/_uploads/rJvE8CKg6.png)

**Last couple of days**

* We tried implementing the MC step, but there seemed to be a memory issue we ran into after the code had run for a sufficient amount of time. 
    * We tried only producing a single realization 
    
**10/09/23**

* We figured out how to write out 7D arrays to text file so that they're written to a single line. This is necessary in order to run `smf_plots.py` smoothly.

**10/24/23**

* It's been a while, but basically we've determined that no subsampling in the Galacicus parameter file is the quickest way to execute things. 

* We have SMF plots correctly working at each resolution

* There are some bugs with the radial distribution plots, but we think we've figured them out (for tomorrow)

**10/25/23**

* Figured out bugs and made radial distribution plots: ![](https://hackmd.io/_uploads/B1sNi1PMp.png)
![](https://hackmd.io/_uploads/S1sNi1Dzp.png)
![](https://hackmd.io/_uploads/H1oEsJPMT.png)

* Now working on code that will produce radial distribution plots and different redshifts

**10/30/23**

* I gotta get better about writing in this regularly. Today I've been updating and recompiling Galacticus as well as reading the paper talking about extending the analytic model of dark matter subhalo populations to WDM.

**10/31/23**

* Galacticus is fully updated. Now when I run Galacticus with a mass resolution of $10^8 M_\odot$ with the addition of the `tidallyTruncatedNFWFit` parameter, it takes around 58 seconds as opposed to 21 seconds. 
    * My mistake!! The 21 seconds was when we included subsampling, but the current script does not take into account subsampling so the times are consistent between runs. 
    
**11/02/23**

* We're trying to go back to Daniel Gilman's code and right now it's executing when we have the `CDM` or `CDMEmulator` classes, but crashes when we work with the `WDM` or `WDMEmulator` classes. 
    * The reason for this is because we deleted the `emulator_inference_output_WDM` directory which gets produced when running the code. In theory if the code works right, then it should create this directory and run successfully. But it's only running successfully if the directory is already created. 
    * So trying to debug right now. 
    
**11/03/23**

* I basically tried to debug stuff and nothing was really working.. I think I'm going to update my versions of `pyHalo` and `quadmodel` and start from scratch

* Basic idea: The module `pyHalo` is what gets used to generate a subhalo population, and `quadmodel` gets used to produce the $S_\text{lens}$ curves. But implementing the emulator into `pyHalo` is the first step. 
    * My branch of `pyHalo` is one branch ahead because of some changes I made in 