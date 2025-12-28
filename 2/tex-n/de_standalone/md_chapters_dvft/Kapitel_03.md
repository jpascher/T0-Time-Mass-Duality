# Kapitel 03

FIELD EQUATIONS
This chapter derives the mathematical framework of DVFT, unifying the quantum vacuum structure with
gravitational curvature. We start from the action principle and obtain field equations through variation,
emphasizing the physical mechanism: Curvature emerges from propagating distortions in the dynamic
vacuum field.
1. Introduction
General Relativity (GR) presents gravitation as curvature of spacetime induced by energy–momentum.
Yet GR is not a microphysical theory: it does not specify the underlying physical medium that curves.
Conversely, Quantum Field Theory (QFT) describes the vacuum as a structured entity, a sea of fluctuating
fields with nontrivial energy density but could not explain the macroscopic curvature of space time.
The Dynamic Vacuum Field Theory (DVFT) attempts to bridge these two frameworks by proposing that
curvature is a macroscopic manifestation of the dynamic vacuum field. In the DVFT, spacetime is not
empty but contains a complex scalar field Φ(x), whose amplitude ρ and phase θ encode the internal state
of the vacuum. The phase evolves with intrinsic frequency μ, giving rise to a continuous dynamic vacuum
field:
Φ_vac = ρ₀ e^{-iμt}
Matter perturbs the vacuum field, distorting the dynamic vacuum field. These distortions propagate
outward at the speed of light, carrying curvature information and establishing gravitational fields.
Curvature is thus the steady-state result of dynamic vacuum field patterns interacting with matter.
2. The dynamic vacuum field medium
The vacuum field is defined as:
Φ(x) = ρ(x) e^{iθ(x)}
where ρ(x) ≥ 0 is the vacuum amplitude and θ(x) is the vacuum phase. This decomposition reflects the
internal degrees of freedom associated with the vacuum, analogous to order parameters in condensedmatter systems.
In the unperturbed state, the vacuum sits at the minimum of its potential:
Φ_vac(x) = ρ₀ e^{-iμt}
Here, μ is the intrinsic dynamic vacuum field frequency. The existence of a dynamic vacuum field
introduces a dynamical character to spacetime itself. Though Φ_vac breaks global time-translation
symmetry at the solution level, the underlying Lagrangian remains Lorentz invariant. Every observer
perceives Φ_vac as the same dynamic vacuum field state in their proper frame.
International Journal for Multidisciplinary Research (IJFMR)
E-ISSN: 2582-2160 ● Website: www.ijfmr.com ● Email: editor@ijfmr.com
IJFMR250664112 Volume 7, Issue 6, November-December 2025 7
The formal theory assumes:
1. A Lorentzian spacetime (M, g_{μν}).
2. Lorentz and diffeomorphism invariance.
3. A global U(1) symmetry θ → θ + const.
This is the minimal structure required for a physical vacuum medium.
3. Action Principle and Field Equations
The theory is governed by the action:
𝑆 = ∫ 𝑑
4𝑥 √−𝑔 [
𝑅
16𝜋𝐺 + ℒΦ + ℒ𝑚(𝜓, Φ, 𝑔)],
where R is the Ricci scalar, G is Newton's constant, ℒΦ is the vacuum Lagrangian, and ℒ𝑚 is for matter
fields ψ coupled to Φ.
The vacuum Lagrangian is:
ℒΦ = −
1
2
𝑔
𝜇𝜈 ∂𝜇𝜌 ∂𝜈𝜌 − 𝑉(𝜌) + 𝐹(𝑋),
with the kinetic invariant:
𝑋 = −
1
2
𝜌
2𝑔
𝜇𝜈 ∂𝜇𝜃 ∂𝜈𝜃.
The potential is:
𝑉(𝜌) = 𝜆(𝜌
2 − 𝜌0
2
)
2
,
ensuring a nonzero equilibrium 𝜌0. The nonlinear function is:
𝐹(𝑋) = 𝑋 +
2
3
𝑋
3/2
𝑀2
,
Here M is the vacuum response scale controlling deep-field modifications to gravity.
4. Matter–Vacuum Coupling
Matter couples via:
ℒ𝑚 ⊃ −𝑦𝜌𝜓‾𝜓,
which modifies the vacuum amplitude near matter. A more general coupling allows matter to affect the
vacuum phase through:
𝐽(𝜓) =
∂ℒ𝑚
∂Φ∗
.
Such interactions produce gradients in δρ and δθ. These gradients radiate outward, establishing the
gravitational field. This mechanism restores locality and causality: curvature arises from a physically
propagating vacuum distortion rather than an instantaneous geometric response.
5. Vacuum Stress–Energy and the Origin of Curvature
The vacuum field carries energy–momentum. Its stress–energy tensor directly enters Einstein's equation.
Thus, curvature is caused by the vacuum’s internal dynamics. Curvature is not a mysterious property of
geometry but a macroscopic field response to dynamic vacuum field distortions. The vacuum stress-energy
is:
𝑇𝜇𝜈
(Φ) = ∂𝜇Φ∗ ∂𝜈Φ + ∂𝜇Φ∂𝜈Φ∗ − 𝑔𝜇𝜈[𝑔
𝛼𝛽 ∂𝛼Φ∗ ∂𝛽Φ + 𝑉(|Φ|
2
)].
For the nonlinear phase:
𝑇𝜇𝜈
(𝜃) = 𝐹𝑋 ∂𝜇𝜃 ∂𝜈𝜃 − 𝑔𝜇𝜈𝐹(𝑋),
where 𝐹𝑋 = ∂𝐹/ ∂𝑋. Curvature arises because 𝑇𝜇𝜈
(Φ)
sources the Einstein tensor:
International Journal for Multidisciplinary Research (IJFMR)
E-ISSN: 2582-2160 ● Website: www.ijfmr.com ● Email: editor@ijfmr.com
IJFMR250664112 Volume 7, Issue 6, November-December 2025 8
𝐺𝜇𝜈 = 8𝜋𝐺(𝑇𝜇𝜈
(𝑚) + 𝑇𝜇𝜈
(Φ)
).
Thus, curvature is the macroscopic response to vacuum dynamics. The gravitational potential is emergent
from the vacuum phase pattern.
6. Field Equations
Vary S with respect to g^{μν}:
𝛿𝑆 = 0 ⟹
1
16𝜋𝐺 𝐺𝜇𝜈 + 𝑇𝜇𝜈
(Φ) + 𝑇𝜇𝜈
(𝑚) = 0.
For θ (phase equation):
𝛿𝑆
𝛿𝜃 = 0 ⟹ ∇𝜇(𝜌
2𝐹𝑋∇
𝜇𝜃) = 0.
Step-by-step: From ℒΦ, ∂ℒ/ ∂(∂𝜇𝜃) = −𝜌
2𝐹𝑋∇
𝜇𝜃, so Euler-Lagrange gives the divergence.
For ρ (amplitude equation):
𝛿𝑆
𝛿𝜌 = 0 ⟹ ▫𝜌 −
𝑑𝑉
𝑑𝜌 + 𝜌(∇𝜃)
2𝐹𝑋 = −𝑦𝜓‾𝜓.
This includes coupling terms.
7. Weak-Field Limit and Newtonian Gravity
Assume weak, static fields: θ(t, x) = μ t + φ(x).
Then X ≈ μ²/2 - (1/2)|∇φ|².
The phase equation reduces to:
∇ ⋅ (𝐹𝑋∇𝜙) = 4𝜋𝐺𝜌𝑚.
Define Newtonian potential Φ_N = - (μ / ρ_0) φ (scaling for units).
In high-acceleration limit (F_X → 1):
∇
2Φ𝑁 = 4𝜋𝐺𝜌𝑚,
recovering Poisson's equation.
8. Deep-Field (MOND-like) Regime
For small gradients, F(X) ≈ X^{3/2}/M²,
so F_X ≈ (3/2) (X^{1/2}/M²).
This yields:
𝑔
2 = 𝑎0𝑔𝑁,
with a_0 = c^4 / (G M^2) (dimensional match).
Thus galaxy rotation curves are reproduced without dark matter through the nonlinear phase response of
the vacuum.
9. Stability and Hyperbolicity
Ghost-free: F_X > 0. Sound speed:
𝑐𝑠
2 =
𝐹𝑋
𝐹𝑋 + 2𝑋𝐹𝑋𝑋
.
For F_{XX} = (3/4) (X^{-1/2}/M²), 0 < c_s^2 < 1, ensuring stability and subluminality.
10. Vacuum Disturbances and Their Propagation
Consider perturbations:
Φ = (ρ₀ + δρ) e^{i(θ₀ + δθ)}
Linearizing the vacuum equation gives:
∇^μ∇_μ δθ = 0
which describes a massless field propagating exactly at the speed of light.
International Journal for Multidisciplinary Research (IJFMR)
E-ISSN: 2582-2160 ● Website: www.ijfmr.com ● Email: editor@ijfmr.com
IJFMR250664112 Volume 7, Issue 6, November-December 2025 9
Amplitude perturbations δρ satisfy a massive Klein–Gordon equation. The phase mode δθ is the primary
carrier of gravitational information in this theory, analogous to a superfluid phase mode. Curvature signals
propagate through the vacuum by means of δθ waves.
11. Strong-Field Behavior and Black Holes
In strong gravity, near compact objects, the vacuum amplitude ρ decreases and phase gradients become
large:
|∂_r θ| → ∞ as r → r_H
where r_H is the horizon radius.
The horizon emerges naturally when:
2GM / r = 1
Near the horizon, the dynamic vacuum field slows due to redshift, leading to time dilation. The vacuum
phase becomes effectively 'frozen' at the horizon, matching GR predictions while giving a microphysical
interpretation: the horizon is a phase singularity of the vacuum field.
12. Gravitational Waves
There are two types of gravitational waves in this model:
1. Tensor gravitational waves:
□ h_{μν} = 0
These match the predictions of GR.
2. Scalar phase waves:
□ δθ = 0
These propagate at c and may produce additional polarization modes.
However, observational limits (LIGO/Virgo) constrain their coupling strength.
13. Cosmological Implications
The dynamic vacuum field contributes dynamically to cosmology. The intrinsic frequency μ may vary
with cosmic time, leading to:
• inflation-like behavior,
• dark-energy-like acceleration,
• coherent, ultralight field oscillations,
• large-scale phase structures influencing galaxy formation.
In certain regimes, ρ and θ fluctuations can act as dark-matter analogs or dark radiation.
14. Observational Tests and Predictions
The DVFT predicts:
• scalar gravitational waves,
• modified post-Newtonian parameters,
• frequency-dependent GW dispersion,
• vacuum refractive-index gradients near massive bodies,
• small corrections to Shapiro delay,
• cosmological signatures from vacuum-phase evolution.
These predictions are testable, making the theory falsifiable.
15. Dynamic vacuum field and Gravity
In DVFT, θ(t) evolves over time:
θ(t) = μ t
Gravity arises from spatial gradients of this phase:
International Journal for Multidisciplinary Research (IJFMR)
E-ISSN: 2582-2160 ● Website: www.ijfmr.com ● Email: editor@ijfmr.com
IJFMR250664112 Volume 7, Issue 6, November-December 2025 10
curvature ∝ (∂θ)²
So:
• ρ stores vacuum energy
• θ stores vacuum geometry
• ∂θ creates spacetime curvature
DVFT does not assume dynamic vacuum field arbitrarily, it derives from spontaneous symmetry breaking
vacuum stability. Thus, the dynamic vacuum field is the vacuum’s way of occupying the ground state of
its potential with minimum action. The vacuum behaves like a coherent dynamic field, even if the
underlying Planck regime is chaotic.
This is the same structure used to describe superfluid, Bose–Einstein condensates and Higgs field. Such
systems inherently possess dynamic behavior. Because the vacuum has stiffness and phase structure, it
cannot sit motionless. Therefore, spacetime naturally becomes dynamic vacuum field.
Dynamic vacuum field is a physical necessity that transforms the vacuum into a dynamic medium capable
of generating curvature, supporting waves, avoiding singularities, and mediating cosmological evolution.
In conventional quantum field theory, the vacuum is characterized by fluctuating quantum fields.
However, such fluctuations are typically treated statistically. The DVFT instead emphasizes coherent,
macroscopic vacuum oscillation represented by the temporal evolution of θ(x). This Dynamic vacuum
field is not an externally imposed motion but arises spontaneously from the form of the vacuum potential.
This potential selects a nonzero amplitude ρ(x) and thereby induces spontaneous symmetry breaking
vacuum stability. The phase θ(x) in such a broken symmetry is capable of transmitting information at c.
The vacuum's ability to support waves propagating at c links directly to the causal structure of spacetime.
In GR, gravitational influences propagate at c, as encoded by the hyperbolic nature of the Einstein
equations. DVFT reproduces this naturally identical in form to the wave equation for massless particles.
Thus, the propagation of curvature information is unified with the propagation of vacuum-phase waves.
This provides a tangible mechanism replacing Einstein’s geometric axiom with physical field dynamics.
Spacetime curvature is the macroscopic manifestation of distortions in the dynamic vacuum field 𝜙 with
an amplitude ρ and phase θ and matter acts as a local perturbation that modifies this dynamic vacuum
field. The resulting phase and amplitude gradients propagate at light speed, imprinting curvature onto
spacetime.
Dynamic vacuum field occurs in its own proper time and internal phase space, not relative to any external
background. This preserves Lorentz invariance, avoids the need for a classical ether, and integrates
smoothly with both general relativity and quantum field theory.
The phase evolves according to:
θ(τ) = μ · τ
where tau is proper time defined by the metric:
dτ2=−gμνdxμ
dxν
This ensures that every observer measures the same local Dynamic vacuum field frequency. No external
time or preferred frame exists. Rotation of theta is analogous to the phase of a quantum wavefunction or
Higgs field expectation value. No external frame is needed for this rotation.
DVFT does not require a deeper background spacetime or physical ether. Dynamic vacuum field is not
motion through space but evolution of the vacuum's internal state. Dynamic vacuum field occurs relative
to the vacuum's own internal structure and proper time. DVFT thus provides a fully consistent explanation
for Dynamic vacuum field without requiring an external reference frame.
International Journal for Multidisciplinary Research (IJFMR)
E-ISSN: 2582-2160 ● Website: www.ijfmr.com ● Email: editor@ijfmr.com
IJFMR250664112 Volume 7, Issue 6, November-December 2025 11
Conclusion
The Dynamic Vacuum Field Theory provides a full microphysical explanation for gravitational curvature.
Spacetime curvature emerges from propagating vacuum distortions generated by matter. The theory is
consistent with general relativistic phenomenology while offering new insights into vacuum structure,
quantum gravity, and cosmology.
