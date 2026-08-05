# SIDM parametric model checks

The code implements the Yang et al. fits for `Vmax_NFW`/`Rmax_NFW` (lines 668, 649) and their derivatives `dvmaxt`/`drmaxt` (lines 608, 627):
$$V_\mathrm{max}^\mathrm{SIDM}(t) = V_\mathrm{max}^\mathrm{CDM}(t)\cdot F_V(\tau), \qquad R_\mathrm{max}^\mathrm{SIDM}(t) = R_\mathrm{max}^\mathrm{CDM}(t)\cdot F_R(\tau)$$

The metaproperty `VmaxSIDMID` stores the difference $S_V$ ≡ `VmaxSIDM` − `VmaxCDM`, because everywhere the full value is reconstructed as stored + VmaxCDM(t) (lines 519, 539, 403). So by design:
$$S_V(t) = V_\mathrm{max}^\mathrm{CDM}(t) \big(F_V(\tau)-1\big).$$

S_V is an evolvable ODE variable; its rate is set on line 536 as dvdt = dvmaxt(τ,VmaxCDM)·dτ/dt, i.e.
$$\left.\frac{\mathrm{d}S_V}{\mathrm{d}t}\right|\text{code} = V\mathrm{max}^\mathrm{CDM},F_V'(\tau),\dot\tau.$$
  
  But differentiating the correct S_V gives two terms:                                                  
                                                    
  $$\frac{\mathrm{d}S_V}{\mathrm{d}t} = \underbrace{V_\mathrm{max}^\mathrm{CDM},F_V'(\tau),\dot\tau}_{\text{kept}} + \underbrace{\dot V\mathrm{max}^\mathrm{CDM},\big(F_V(\tau)-1\big)}_{\textbf{omitted}}.$$

  The code keeps only the τ-evolution term and drops the term from the time-dependence of the CDM halo itself. Equivalently, the missing piece is S_V · d(ln VmaxCDM)/dt — the stored offset should grow in lock-step with the fractional growth of the CDM halo, and currently doesn't. Same omission for RmaxSIDM on line 537.
  
This problem:
- Vanishes at τ=0 (F_V−1=0) and for non-accreting halos (V̇maxCDM=0), so early times and static subhalos are fine.
- It occurs when a halo is simultaneously accreting and SIDM-evolved. F_V−1 reaches ~0.06 at τ=0.5 and ~0.21 at τ=1, so with significant CDM growth the reconstructed VmaxSIDM can drift at the ~5–20% level.
- It propagates into the profile: Vmax_NFW(VmaxSIDM,τ) is supposed to recover VmaxCDM exactly (since VmaxSIDM/F_V = VmaxCDM); with the drift it doesn't, so the derived rho_s, r_s, r_c (the actual profile, set in SolveAnalytics) are off.
