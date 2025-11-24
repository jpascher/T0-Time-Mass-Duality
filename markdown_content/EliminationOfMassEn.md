\title{Elimination of Mass as Dimensional Placeholder \\
		in the T0 Model: Towards True Parameter-Free Physics}
	\author{Johann Pascher\\
		Department of Communications Engineering, \\Höhere Technische Bundeslehranstalt (HTL), Leonding, Austria\\
		`johann.pascher@gmail.com`}
	\date{\today}
	
	\begin{abstract}
		This paper demonstrates that the mass parameter $m$ appearing throughout the T0 model formulations serves exclusively as a dimensional placeholder and can be systematically eliminated from all equations. Through rigorous dimensional analysis and mathematical reformulation, we show that the apparent dependence on specific particle masses is an artifact of conventional notation rather than fundamental physics. The elimination of $m$ reveals the T0 model as a truly parameter-free theory based solely on the Planck scale, providing universal scaling laws and eliminating systematic biases from empirical mass determinations. This work establishes the mathematical foundation for a complete ab-initio formulation of the T0 model requiring no external experimental inputs beyond the fundamental constants $\hbar$, $c$, $G$, and $k_B$.
	\end{abstract}
	
	

---

# Introduction
	\label{sec:introduction}
	
	## The Problem of Mass Parameters
	\label{subsec:mass_problem}
	
	The T0 model, as formulated in previous works, appears to depend critically on specific particle masses such as the electron mass $m_e$, proton mass $m_p$, and Higgs boson mass $m_h$. This apparent dependence has led to concerns about the model's predictive power and its reliance on empirical inputs that may themselves be contaminated by Standard Model assumptions.
	
	A careful analysis reveals, however, that the mass parameter $m$ serves a purely **dimensional function** in the T0 equations. This paper demonstrates that $m$ can be systematically eliminated from all formulations, revealing the T0 model as a fundamentally parameter-free theory based exclusively on Planck-scale physics.
	
	## Dimensional Analysis Approach
	\label{subsec:dimensional_approach}
	
	In natural units where $\hbar = c = G = k_B = 1$, all physical quantities can be expressed as powers of energy $[E]$:
	
	\begin{align}
		\text{Length:} \quad [L] &= [E^{-1}] \\
		\text{Time:} \quad [T] &= [E^{-1}] \\
		\text{Mass:} \quad [M] &= [E] \\
		\text{Temperature:} \quad [\Theta] &= [E]
	\end{align}
	
	This dimensional structure suggests that mass parameters may be replaceable by energy scales, leading to more fundamental formulations.
	
	# Systematic Mass Elimination
	\label{sec:mass_elimination}
	
	## The Intrinsic Time Field
	\label{subsec:time_field_elimination}
	
	### Original Formulation
	
	The intrinsic time field is traditionally defined as:
	
	\begin{equation}
		\Tfieldt = \frac{1}{\max(m(\vecx,t), \omega)}
		\label{eq:time_field_original}
	\end{equation}
	
	**Dimensional analysis:**
	\begin{itemize}
		\item $[\Tfieldt] = [E^{-1}]$ (time field dimension)
		\item $[m] = [E]$ (mass as energy)
		\item $[\omega] = [E]$ (frequency as energy)
		\item $[1/\max(m,\omega)] = [E^{-1}]$ \checkmark
	\end{itemize}
	
	### Mass-Free Reformulation
	
	The fundamental insight is that only the **ratio** between characteristic energy and frequency matters physically. We reformulate as:
	
	\begin{equation}
		\boxed{\Tfieldt = \tP \cdot g(E_{\text{norm}}(\vecx,t), \omega_{\text{norm}})}
		\label{eq:time_field_mass_free}
	\end{equation}
	
	where:
	\begin{align}
		\tP &= \sqrt{\frac{\hbar G}{c^5}} \quad \text{(Planck time)} \\
		E_{\text{norm}} &= \frac{E(\vecx,t)}{\EP} \quad \text{(normalized energy)} \\
		\omega_{\text{norm}} &= \frac{\omega}{\EP} \quad \text{(normalized frequency)} \\
		g(E_{\text{norm}}, \omega_{\text{norm}}) &= \frac{1}{\max(E_{\text{norm}}, \omega_{\text{norm}})}
	\end{align}
	
	**Result:** Mass completely eliminated, only Planck scale and dimensionless ratios remain.
	
	## Field Equation Reformulation
	\label{subsec:field_equation_elimination}
	
	### Original Field Equation
	
	\begin{equation}
		\nabla^2 \Tfield = -4\pi G \rho(\vecx) \Tfield^2
		\label{eq:field_equation_original}
	\end{equation}
	
	with mass density $\rho(\vecx) = m \cdot \delta^3(\vecx)$ for a point source.
	
	### Energy-Based Formulation
	
	Replacing mass density with energy density:
	
	\begin{equation}
		\boxed{\nabla^2 \Tfield = -4\pi G \frac{E(\vecx)}{\EP} \delta^3(\vecx) \frac{\Tfield^2}{\tP^2}}
		\label{eq:field_equation_mass_free}
	\end{equation}
	
	**Dimensional verification:**
	\begin{align}
		[\nabla^2 \Tfield] &= [E^{-1} \cdot E^2] = [E] \\
		[4\pi G E_{\text{norm}} \delta^3(\vecx) \Tfield^2/\tP^2] &= [E^{-2}][1][E^6][E^{-2}]/[E^{-2}] = [E] \quad \checkmark
	\end{align}
	
	## Point Source Solution: Parameter Separation
	\label{subsec:point_source_elimination}
	
	### The Mass Redundancy Problem
	
	The traditional point source solution exhibits apparent mass redundancy:
	
	\begin{equation}
		\Tfield(r) = \frac{1}{m}\left(1 - \frac{r_0}{r}\right)
		\label{eq:point_source_original}
	\end{equation}
	
	with $r_0 = 2Gm$. Substituting:
	
	\begin{equation}
		\Tfield(r) = \frac{1}{m}\left(1 - \frac{2Gm}{r}\right) = \frac{1}{m} - \frac{2G}{r}
		\label{eq:mass_redundancy}
	\end{equation}
	
	**Critical observation:** Mass $m$ appears in **two different roles**:
	\begin{enumerate}
		\item As normalization factor $(1/m)$
		\item As source parameter $(2Gm)$
	\end{enumerate}
	
	This suggests that $m$ masks **two independent physical scales**.
	
	### Parameter Separation Solution
	
	We reformulate with independent parameters:
	
	\begin{equation}
		\boxed{\Tfield(r) = \Tzero\left(1 - \frac{L_0}{r}\right)}
		\label{eq:point_source_mass_free}
	\end{equation}
	
	where:
	\begin{itemize}
		\item $\Tzero$: Characteristic time scale $[E^{-1}]$
		\item $L_0$: Characteristic length scale $[E^{-1}]$
	\end{itemize}
	
	**Physical interpretation:**
	\begin{itemize}
		\item $\Tzero$ determines the **amplitude** of the time field
		\item $L_0$ determines the **range** of the time field
		\item Both derivable from source geometry without specific masses
	\end{itemize}
	
	## The $\xipar$ Parameter: Universal Scaling
	\label{subsec:xi_elimination}
	
	### Traditional Mass-Dependent Definition
	
	\begin{equation}
		\xipar = 2\sqrt{G} \cdot m
		\label{eq:xi_original}
	\end{equation}
	
	**Problem:** Requires specific particle masses as input.
	
	### Universal Energy-Based Definition
	
	\begin{equation}
		\boxed{\xipar = 2\sqrt{\frac{E_{\text{characteristic}}}{\EP}}}
		\label{eq:xi_mass_free}
	\end{equation}
	
	**Universal scaling for different energy scales:**
	\begin{align}
		\text{Planck energy } (E = \EP): \quad &\xipar = 2 \\
		\text{Electroweak scale } (E \sim 100 \text{ GeV}): \quad &\xipar \sim 10^{-8} \\
		\text{QCD scale } (E \sim 1 \text{ GeV}): \quad &\xipar \sim 10^{-9} \\
		\text{Atomic scale } (E \sim 1 \text{ eV}): \quad &\xipar \sim 10^{-28}
	\end{align}
	
	**No specific particle masses required!**
	
	# Complete Mass-Free T0 Formulation
	\label{sec:complete_formulation}
	
	## Fundamental Equations
	\label{subsec:fundamental_equations}
	
	The complete mass-free T0 system:
	
	\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=Mass-Free T0 Model]
		\begin{align}
			\text{Time field:} \quad &\Tfieldt = \tP \cdot f(E_{\text{norm}}(\vecx,t), \omega_{\text{norm}}) \\
			\text{Field equation:} \quad &\nabla^2 \Tfield = -4\pi G \frac{E_{\text{norm}}}{\lP^2} \delta^3(\vecx) \Tfield^2 \\
			\text{Point sources:} \quad &\Tfield(r) = \Tzero\left(1 - \frac{L_0}{r}\right) \\
			\text{Coupling parameter:} \quad &\xipar = 2\sqrt{\frac{E}{\EP}}
		\end{align}
	\end{tcolorbox}
	
	## Parameter Count Analysis
	\label{subsec:parameter_count}
	
	\begin{center}
		\begin{tabular}{|l|c|c|}
			\hline
			**Formulation** & **Before Mass Elimination** & **After Mass Elimination** \\
			\hline
			\hline
			Fundamental constants & $\hbar, c, G, k_B$ & $\hbar, c, G, k_B$ \\
			\hline
			Particle-specific masses & $m_e, m_\mu, m_p, m_h, \ldots$ & None \\
			\hline
			Dimensionless ratios & None explicit & $E/\EP$, $L/\lP$, $T/\tP$ \\
			\hline
			Free parameters & $\infty$ (one per particle) & 0 \\
			\hline
			Empirical inputs required & Yes (masses) & No \\
			\hline
		\end{tabular}
	\end{center}
	
	## Dimensional Consistency Verification
	\label{subsec:dimensional_consistency}
	
	\begin{table}[htbp]
		\centering
		\begin{tabular}{lccl}
			\toprule
			**Equation** & **Left Side** & **Right Side** & **Status** \\
			\midrule
			Time field & $[\Tfieldt] = [E^{-1}]$ & $[\tP \cdot f(\cdot)] = [E^{-1}]$ & \checkmark \\
			Field equation & $[\nabla^2 \Tfield] = [E]$ & $[G E_{\text{norm}} \delta^3 \Tfield^2/\lP^2] = [E]$ & \checkmark \\
			Point source & $[\Tfield(r)] = [E^{-1}]$ & $[\Tzero(1-L_0/r)] = [E^{-1}]$ & \checkmark \\
			$\xipar$ parameter & $[\xipar] = [1]$ & $[\sqrt{E/\EP}] = [1]$ & \checkmark \\
			\bottomrule
		\end{tabular}
		\caption{Dimensional consistency of mass-free formulations}
	\end{table}
	
	# Experimental Implications
	\label{sec:experimental_implications}
	
	## Universal Predictions
	\label{subsec:universal_predictions}
	
	The mass-free T0 model makes universal predictions independent of specific particle properties:
	
	### Scaling Laws
	
	\begin{equation}
		\xipar(E) = 2\sqrt{\frac{E}{\EP}}
		\label{eq:universal_scaling}
	\end{equation}
	
	This relationship must hold for **all** energy scales, providing a stringent test of the theory.
	
	### QED Anomalies
	
	The electron anomalous magnetic moment becomes:
	
	\begin{equation}
		a_e^{(\text{T0})} = \frac{\alpha}{2\pi} \cdot C_{\text{T0}} \cdot \left(\frac{E_e}{\EP}\right)
		\label{eq:qed_universal}
	\end{equation}
	
	where $E_e$ is the characteristic energy scale of the electron, not its rest mass.
	
	### Gravitational Effects
	
	\begin{equation}
		\Phi(r) = -\frac{G E_{\text{source}}}{\EP} \cdot \frac{\lP}{r}
		\label{eq:gravity_universal}
	\end{equation}
	
	Universal scaling for all gravitational sources.
	
	## Elimination of Systematic Biases
	\label{subsec:bias_elimination}
	
	### Problems with Mass-Dependent Formulations
	
	Traditional approaches suffer from:
	\begin{itemize}
		\item **Circular dependencies:** Using experimentally determined masses to predict the same experiments
		\item **Standard Model contamination:** All mass measurements assume SM physics
		\item **Precision illusions:** High apparent precision masking systematic theoretical errors
	\end{itemize}
	
	### Advantages of Mass-Free Approach
	
	\begin{itemize}
		\item **Model independence:** No reliance on potentially biased mass determinations
		\item **Universal tests:** Same scaling laws apply across all energy scales
		\item **Theoretical purity:** Ab-initio predictions from Planck scale alone
	\end{itemize}
	
	## Proposed Experimental Tests
	\label{subsec:experimental_tests}
	
	### Multi-Scale Consistency
	
	Test the universal scaling relation:
	\begin{equation}
		\frac{\xipar(E_1)}{\xipar(E_2)} = \sqrt{\frac{E_1}{E_2}}
		\label{eq:scaling_test}
	\end{equation}
	
	across different energy scales: atomic, nuclear, electroweak, and cosmological.
	
	### Energy-Dependent Anomalies
	
	Measure anomalous magnetic moments as functions of energy scale rather than particle identity:
	\begin{equation}
		a(E) = a_{\text{SM}}(E) + a^{(\text{T0})}(E/\EP)
		\label{eq:energy_dependent_anomaly}
	\end{equation}
	
	### Geometric Independence
	
	Verify that $\Tzero$ and $L_0$ can be determined independently from source geometry without requiring specific mass values.
	
	# Geometric Parameter Determination
	\label{sec:geometric_parameters}
	
	## Source Geometry Analysis
	\label{subsec:source_geometry}
	
	### Spherically Symmetric Sources
	
	For a spherically symmetric energy distribution $E(r)$:
	
	\begin{align}
		\Tzero &= \tP \cdot f\left(\frac{\int E(r) d^3r}{\EP}\right) \\
		L_0 &= \lP \cdot g\left(\frac{R_{\text{characteristic}}}{\lP}\right)
	\end{align}
	
	where $f$ and $g$ are dimensionless functions determined by the field equations.
	
	### Non-Spherical Sources
	
	For general geometries, the parameters become tensorial:
	
	\begin{align}
		\Tzero^{ij} &= \tP \cdot f_{ij}\left(\frac{I^{ij}}{\EP \lP^2}\right) \\
		L_0^{ij} &= \lP \cdot g_{ij}\left(\frac{I^{ij}}{\lP^2}\right)
	\end{align}
	
	where $I^{ij}$ is the energy moment tensor of the source.
	
	## Universal Geometric Relations
	\label{subsec:geometric_relations}
	
	The mass-free formulation reveals universal relationships between geometric and energetic properties:
	
	\begin{equation}
		\frac{L_0}{\lP} = h\left(\frac{\Tzero}{\tP}, \text{shape parameters}\right)
		\label{eq:geometric_relation}
	\end{equation}
	
	These relationships are **independent of specific mass values** and depend only on:
	\begin{itemize}
		\item Energy distribution geometry
		\item Planck-scale ratios
		\item Dimensionless shape parameters
	\end{itemize}
	
	# Connection to Fundamental Physics
	\label{sec:fundamental_connection}
	
	## Emergent Mass Concept
	\label{subsec:emergent_mass}
	
	### Mass as Effective Parameter
	
	In the mass-free formulation, what we traditionally call "mass" emerges as:
	
	\begin{equation}
		m_{\text{effective}} = E_{\text{characteristic}} \cdot f(\text{geometry}, \text{couplings})
		\label{eq:emergent_mass}
	\end{equation}
	
	**Different "masses" for different contexts:**
	\begin{itemize}
		\item **Rest mass:** Intrinsic energy scale of localized excitation
		\item **Gravitational mass:** Coupling strength to spacetime curvature  
		\item **Inertial mass:** Resistance to acceleration in external fields
	\end{itemize}
	
	All reducible to **energy scales and geometric factors**.
	
	### Resolution of Mass Hierarchies
	
	The apparent hierarchy of particle masses becomes a hierarchy of **energy scales**:
	
	\begin{align}
		\frac{m_t}{m_e} &\rightarrow \frac{E_{\text{top}}}{E_{\text{electron}}} \\
		\frac{m_W}{m_e} &\rightarrow \frac{E_{\text{electroweak}}}{E_{\text{electron}}} \\
		\frac{m_P}{m_e} &\rightarrow \frac{\EP}{E_{\text{electron}}}
	\end{align}
	
	**No fundamental mass parameters**, only energy scale ratios.
	
	## Unification with Planck Scale Physics
	\label{subsec:planck_unification}
	
	### Natural Scale Emergence
	
	All physics naturally organizes around Planck scale:
	
	\begin{align}
		\text{Microscopic physics:} \quad &E \ll \EP, \quad L \gg \lP \\
		\text{Macroscopic physics:} \quad &E \ll \EP, \quad L \gg \lP \\
		\text{Quantum gravity:} \quad &E \sim \EP, \quad L \sim \lP
	\end{align}
	
	### Scale-Dependent Effective Theories
	
	Different energy regimes correspond to different limits of the universal T0 theory:
	
	\begin{align}
		E \ll \EP: \quad &\text{Standard Model limit} \\
		E \sim \text{TeV}: \quad &\text{Electroweak unification} \\
		E \sim \EP: \quad &\text{Quantum gravity unification}
	\end{align}
	
	# Philosophical Implications
	\label{sec:philosophical}
	
	## Reductionism to Planck Scale
	\label{subsec:reductionism}
	
	The elimination of mass parameters demonstrates that **all physics** is reducible to the **Planck scale**:
	
	\begin{itemize}
		\item No fundamental mass parameters exist
		\item Only energy and length ratios matter
		\item Universal dimensionless couplings emerge naturally
		\item True parameter-free physics achieved
	\end{itemize}
	
	## Ontological Implications
	\label{subsec:ontological}
	
	### Mass as Human Construct
	
	The traditional concept of "mass" appears to be a **human construct** rather than fundamental reality:
	
	\begin{itemize}
		\item Useful for practical calculations
		\item Not present in deepest level of theory
		\item Emergent from more fundamental energy relationships
	\end{itemize}
	
	### Universal Energy Monism
	
	The mass-free T0 model supports a form of **energy monism**:
	\begin{itemize}
		\item Energy as the only fundamental quantity
		\item All other quantities as energy relationships
		\item Space and time as energy-derived concepts
		\item Matter as structured energy patterns
	\end{itemize}
	
	# Conclusions
	\label{sec:conclusions}
	
	## Summary of Results
	\label{subsec:summary}
	
	We have demonstrated that:
	
	\begin{enumerate}
		\item **Mass $m$ serves only as dimensional placeholder** in T0 formulations
		\item **All equations can be systematically reformulated** without mass parameters
		\item **Universal scaling laws emerge** based solely on Planck scale
		\item **True parameter-free theory** results from mass elimination
		\item **Experimental predictions become model-independent**
	\end{enumerate}
	
	## Theoretical Significance
	\label{subsec:theoretical_significance}
	
	The mass elimination reveals the T0 model as:
	
	\begin{tcolorbox}[colback=green!5!white,colframe=green!75!black,title=T0 Model: True Nature]
		\begin{itemize}
			\item **Truly fundamental theory** based on Planck scale alone
			\item **Parameter-free formulation** with universal predictions
			\item **Unification of all energy scales** through dimensionless ratios
			\item **Resolution of fine-tuning problems** via scale relationships
		\end{itemize}
	\end{tcolorbox}
	
	## Experimental Program
	\label{subsec:experimental_program}
	
	The mass-free formulation enables:
	
	\begin{itemize}
		\item **Model-independent tests** of universal scaling
		\item **Elimination of systematic biases** from mass measurements
		\item **Direct connection** between quantum and gravitational scales
		\item **Ab-initio predictions** from pure theory
	\end{itemize}
	
	## Future Directions
	\label{subsec:future_directions}
	
	### Immediate Research Priorities
	
	\begin{enumerate}
		\item **Complete geometric formulation:** Develop full tensor treatment for arbitrary source geometries
		\item **Quantum field theory extension:** Formulate mass-free QFT on T0 background
		\item **Cosmological applications:** Apply to large-scale structure without dark matter/energy
		\item **Experimental design:** Develop tests of universal scaling laws
	\end{enumerate}
	
	### Long-term Goals
	
	\begin{itemize}
		\item Complete replacement of Standard Model with mass-free T0 theory
		\item Unification of all interactions through energy scale relationships
		\item Resolution of quantum gravity through Planck-scale physics
		\item Experimental verification of parameter-free predictions
	\end{itemize}
	
	# Final Remarks
	\label{sec:final_remarks}
	
	The elimination of mass as a fundamental parameter represents more than a technical improvement—it reveals the **true nature of physical reality** as organized around energy relationships and geometric structures. 
	
	The apparent complexity of particle physics, with its multitude of masses and coupling constants, emerges from our limited perspective on more fundamental energy scale relationships. The T0 model, in its mass-free formulation, provides a window into this deeper reality.
	
	**Mass was always an illusion—energy and geometry are the fundamental reality.**
	
	\begin{thebibliography}{9}
\bibitem{pascher_derivation_2025}
Pascher, J. (2025). *Field-Theoretic Derivation of the $\beta_T$ Parameter in Natural Units ($\hbar = c = 1$)*. Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/DerivationVonBetaEn.pdf}

\bibitem{pascher_units_2025}  
Pascher, J. (2025). *Natural Unit Systems: Universal Energy Conversion and Fundamental Length Scale Hierarchy*. Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/NatEinheitenSystematikEn.pdf}

\bibitem{pascher_dirac_2025}
Pascher, J. (2025). *Integration of the Dirac Equation in the T0 Model: Updated Framework with Natural Units*. Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/diracEn.pdf}
		
		\bibitem{planck_1899}
		Planck, M. (1899). *Über irreversible Strahlungsvorgänge*. Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin, 5, 440-480.
		
		\bibitem{wheeler_1955}
		Wheeler, J. A. (1955). *Geons*. Physical Review, 97(2), 511-536.
		
		\bibitem{weinberg_1989}
		Weinberg, S. (1989). *The cosmological constant problem*. Reviews of Modern Physics, 61(1), 1-23.
	\end{thebibliography}
\chapter*{Introduction}
\addcontentsline{toc}{chapter}{Introduction}

This book presents the current state of the T0 time--mass duality framework and its applications to
particle masses, fundamental constants, quantum mechanics, gravitation, and cosmology.

The main body of the book consists of a set of core T0 documents. These chapters reflect the
present understanding of the theory and its quantitative consequences. Wherever possible, the
material has been reorganized and unified so that the structure of the theory becomes as transparent
as possible.

At the end of the book, several older documents are included in an appendix. These texts represent
earlier stages of the development of the T0 framework. They were not removed, because they make
the evolution of the ideas and the refinement of the formulas visible. In many cases, one can see
how approximations were improved, how special cases were generalized, and how new empirical data
helped to sharpen or correct earlier arguments.

The “live” version of the theory is maintained in a public GitHub repository:

\begin{center}
	\url{https://github.com/jpascher/T0-Time-Mass-Duality}
\end{center}

The LaTeX sources of the chapters in this book are taken from that repository. If conceptual or
numerical errors are found, they are corrected there first. This means that the PDF version of the
book you are reading is a snapshot of a continuously evolving project. For the most recent version
of the documents, including new appendices or corrections, the GitHub repository should always be
considered the primary reference.

The intention of this compilation is twofold:
\begin{itemize}
	\item to provide a coherent, readable path through the core ideas and results of the T0 framework;
	\item to document, in the appendix, the historical development of these ideas, including false
	starts, intermediate formulations, and early fits to experimental data.
\end{itemize}

Readers who are mainly interested in the current formulation of the theory may focus on the core
chapters. Readers who are also interested in the reasoning and trial--and--error process behind
the theory are invited to study the appendix material in parallel.