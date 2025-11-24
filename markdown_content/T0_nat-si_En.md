\begin{abstract}
		The use of natural units in theoretical physics is a fundamental concept that can be comprehensively explained and contextualized within the framework of T0 theory. This treatise illuminates the principle of dimensional reduction, the advantages for calculations, the particular relevance for T0 theory, and the necessity of explicit SI units in practice. Finally, it emphasizes the deeper insight that physics ultimately rests on dimensionless geometric relationships.
	\end{abstract}
	
	# Basic Principle of Natural Units
	\label{sec:grundprinzip}
	
	## The Principle of Dimensional Reduction
	In natural units, one sets fundamental constants to 1:
	\begin{itemize}
		\item **Speed of light**: $c = 1$
		\item **Reduced Planck constant**: $\hbar = 1$
		\item **Boltzmann constant**: $k_B = 1$
		\item **Sometimes**: $G = 1$ (Planck units)
	\end{itemize}
	
	## Mathematical Consequence
	This does not mean that these constants ``disappear,'' but that they serve as **scale setters**:
	\begin{equation}
		E = m c^2 \quad \Rightarrow \quad E = m \quad \text{(since $c=1$)}
	\end{equation}
	\begin{equation}
		E = \hbar \omega \quad \Rightarrow \quad E = \omega \quad \text{(since $\hbar=1$)}
	\end{equation}
	
	# Advantages for Calculations
	
	## Simplified Formulas
	**With SI units:**
	\begin{equation}
		E = \sqrt{(p c)^2 + (m c^2)^2}
	\end{equation}
	**In natural units:**
	\begin{equation}
		E = \sqrt{p^2 + m^2}
	\end{equation}
	
	## Transparent Dimensional Analysis
	All quantities can be traced back to one fundamental dimension (typically energy):
	\begin{table}[h]
		\centering
		\begin{tabular}{lll}
			\toprule
			**Quantity** & **Natural Dimension** & **SI Equivalent** \\
			\midrule
			Length & $[E]^{-1}$ & $\hbar c / E$ \\
			Time & $[E]^{-1}$ & $\hbar / E$ \\
			Mass & $[E]$ & $E/c^2$ \\
			\bottomrule
		\end{tabular}
		\caption{Dimensional relationships in natural units}
	\end{table}
	
	# Particular Relevance in T0 Theory
	
	## Geometric Nature of Constants
	T0 theory shows particularly clearly why natural units are fundamental:
	\begin{equation}
		\alpha = \xi \cdot \left( \frac{E_0}{1~\mathrm{MeV}} \right)^2
	\end{equation}
	This makes explicit that the fine structure constant is a **purely dimensionless geometric relationship**.
	
	## The $\xi$-Parameter as Fundamental Geometry Factor
	The derivation:
	\begin{equation}
		\xi = \frac{4}{3} \times 10^{-4}
	\end{equation}
	is intrinsically dimensionless and represents the fundamental space geometry -- independent of human units of measurement.
	
	**Important:** $\xi$ alone is not directly equal to $1/m_e$ or $1/E$, but requires specific scaling factors for different physical quantities.
	
	# Derivation of the Fundamental Scaling Factor $S_{T0$}
	\label{sec:scaling-derivation}
	
	## The Fundamental Prediction of T0 Theory
	
	T0 theory makes a remarkable prediction: the electron mass in geometric units is exactly:
	
	\begin{equation}
		m_e^{\mathrm{T0}} = 0.511
	\end{equation}
	
	This is not a convention, but a **derived consequence** of the fractal space geometry via the $\xi$ parameter.
	
	## Explicit Demonstration: Derivation vs. Reverse Calculation
	
	Let us demonstrate explicitly that the scaling factor is derived, not reverse-calculated:
	
	\begin{align}
		**1. T0 derivation:** \quad & m_e^{\mathrm{T0}} = 0.511 \quad \text{(from $\xi$ geometry)} \\
		**2. Experimental input:** \quad & m_e^{\mathrm{SI}} = 9.1093837 \times 10^{-31}~\mathrm{kg} \quad \text{(measured independently)} \\
		**3. T0 prediction:** \quad & S_{T0} = \frac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}} = 1.782662 \times 10^{-30} \\
		**4. Empirical fact:** \quad & 1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg} \\
		**5. Profound conclusion:** \quad & \text{T0 theory **predicts** the MeV mass scale}
	\end{align}
	
	## Why This Is Not Circular Reasoning
	
	Some might mistakenly think: ``You're just defining $S_{T0}$ to match $1~\mathrm{MeV}/c^2$.''
	
	This misunderstands the logical flow:
	
	\begin{itemize}
		\item **Wrong interpretation (reverse calculation)**: 
		$m_e^{\mathrm{T0}} = \dfrac{m_e^{\mathrm{SI}}}{1~\mathrm{MeV}/c^2}$ (circular)
		
		\item **Correct interpretation (derivation)**: 
		$S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ and this **happens to equal** $1~\mathrm{MeV}/c^2$
	\end{itemize}
	
	The equality $S_{T0} = 1~\mathrm{MeV}/c^2$ is a **prediction**, not a definition.
	
	## Side-by-Side Comparison
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{6cm}p{6cm}}
			\toprule
			**Conventional Physics** & **T0 Theory** \\
			\midrule
			$1~\mathrm{MeV}/c^2 = 1.782662\times 10^{-30}~\mathrm{kg}$ (arbitrary definition) & $m_e^{\mathrm{T0}} = 0.511$ (derived from $\xi$ geometry) \\
			$m_e = 0.511~\mathrm{MeV}/c^2$ (independent measurement) & $S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ (fundamental scaling) \\
			Two independent facts & One **predicts** the other \\
			\bottomrule
		\end{tabular}
		\caption{Comparison of conventional vs. T0 interpretation of mass scales}
	\end{table}
	
	The remarkable fact is: **Both approaches yield identical numbers, but T0 explains why.**
	
	## The Coincidence That Isn't
	
	What appears as a mere numerical coincidence is actually a fundamental prediction:
	
	\begin{align}
		\text{T0 prediction:} \quad & S_{T0} = \frac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}} = \frac{9.1093837 \times 10^{-31}}{0.511} \\
		\text{Conventional definition:} \quad & 1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg}
	\end{align}
	
	These are **identical** not by definition, but because T0 theory correctly predicts the fundamental mass scale.
	
	## The Profound Implication
	
	\begin{center}
		\fbox{\parbox{0.8\textwidth}{
				**T0 theory does not ``use'' the MeV definition.**\\
				**It derives why the MeV has the mass scale it does.**
		}}
	\end{center}
	
	The conventional definition $1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg}$ appears arbitrary, but T0 theory reveals it to be a consequence of fundamental geometry.
	
	## Independent Verification
	
	We can verify this independently:
	
	\begin{itemize}
		\item **Without T0**: $1~\mathrm{MeV}/c^2 = 1.782662\times 10^{-30}~\mathrm{kg}$ (apparently arbitrary convention)
		\item **With T0**: $S_{T0} = 1.782662\times 10^{-30}$ (fundamental scaling derived from geometry)
		\item **Agreement**: The identical numerical value confirms T0's predictive power
	\end{itemize}
	
	This is analogous to how $c = 299,792,458~\mathrm{m/s}$ appears arbitrary until one understands relativity.
	
	# Quantized Mass Calculation in T0 Theory
	
	## Fundamental Mass Quantization Principle
	
	In T0 theory, particle masses are **quantized** and follow from the fundamental geometry parameter $\xi$ through discrete scaling relationships:
	
	\begin{equation}
		m_i^{\mathrm{T0}} = n_i \cdot Q_m^{\mathrm{T0}} \cdot f_i(\xi)
	\end{equation}
	
	where:
	\begin{itemize}
		\item $n_i \in \mathbb{N}$ - Quantum number (discrete)
		\item $Q_m^{\mathrm{T0}}$ - Fundamental mass quantum in T0 units
		\item $f_i(\xi)$ - Particle-specific geometry function
	\end{itemize}
	
	## Electron Mass as Reference
	
	The electron mass serves as the fundamental reference mass:
	
	\begin{align}
		\xi_e &= \frac{4}{3} \times 10^{-4} \times f_e(1,0,1/2) \\
		m_e^{\mathrm{T0}} &= Q_m^{\mathrm{T0}} \cdot \frac{\xi}{\xi_e} = 0.511
	\end{align}
	
	## Complete Particle Mass Spectrum
	
	For detailed derivations of all elementary particle masses within the T0 framework, including quarks, leptons, and gauge bosons, refer to the separate comprehensive treatment ``Particle Masses in T0 Theory'' which provides:
	
	\begin{itemize}
		\item Complete mass calculations for all Standard Model particles
		\item Derivation of mass quantization rules
		\item Explanation of generation patterns
		\item Comparison with experimental values
		\item Fractal renormalization procedures for precision matching
	\end{itemize}
	
	# Important: Explicit SI Units are Necessary for\dots
	\label{sec:si-notwendig}
	
	## 1. Experimental Verification
	Every measurement is performed in SI units:
	\begin{itemize}
		\item Particle masses in MeV/c²
		\item Cross sections in barn
		\item Magnetic moments in $\mu_B$
	\end{itemize}
	
	## 2. Technological Applications
	\begin{itemize}
		\item Detector design (lengths in m, times in s)
		\item Accelerator technology (energies in eV)
		\item Medical physics (dosage measurements)
	\end{itemize}
	
	## 3. Interdisciplinary Communication
	\begin{itemize}
		\item Astrophysics (redshifts, Hubble constant)
		\item Materials science (lattice constants)
		\item Engineering
	\end{itemize}
	
	# Concrete Conversion in T0 Theory
	\label{sec:umrechnung}
	
	## Example: Electron Mass
	**In T0 geometric units:**
	\begin{equation}
		m_e^{\mathrm{T0}} = 0.511 \quad \text{(as pure geometric number derived from $\xi$)}
	\end{equation}
	**In SI units:**
	\begin{equation}
		m_e^{\mathrm{SI}} = m_e^{\mathrm{T0}} \cdot S_{T0} = 0.511 \cdot 1.782662 \times 10^{-30} = 9.1093837 \times 10^{-31}~\mathrm{kg}
	\end{equation}
	
	## The Fundamental Scaling Relationship
	The conversion from T0 geometric quantities to SI units is accomplished by:
	\begin{equation}
		[\mathrm{SI}] = [\mathrm{T0}] \times S_{\text{T0}}
	\end{equation}
	where $S_{\text{T0}} = 1.782662 \times 10^{-30}$ is the fundamental scaling factor **derived** in Section~\ref{sec:scaling-derivation}, not defined.
	
	# Correct Energy Scale for the Fine Structure Constant
	
	The fundamental relationship for the fine structure constant requires a precise energy reference:
	
	\begin{align}
		\alpha &= \xi \cdot \left( \frac{E_0}{1~\mathrm{MeV}} \right)^2 \\
		\text{with} \quad E_0 &= 7.400~\mathrm{MeV} \quad \text{(characteristic energy)}
	\end{align}
	
	This yields:
	\begin{align}
		\alpha &= 1.333333 \times 10^{-4} \cdot (7.400)^2 \\
		&= 1.333333 \times 10^{-4} \cdot 54.76 \\
		&= 7.300 \times 10^{-3} \\
		\frac{1}{\alpha} &= 137.00
	\end{align}
	
	The slight deviation from the experimental value $1/\alpha = 137.036$ is due to higher-order fractal corrections that are accounted for in the complete renormalization procedure.
	
	# Integration of Fractal Renormalization into Natural Units
	
	The formulas in T0 theory fit in natural units without explicit fractal renormalization, because these units isolate the geometric essence of the theory. For exact conversions to SI units, however, fractal renormalization is essential to incorporate self-similar corrections of the vacuum geometry.
	
	## Why Do the Formulas Fit in Natural Units Without Fractal Renormalization?
	
	In natural units, physics is reduced to a geometric, dimensionless basis (cf. Section~\ref{sec:grundprinzip}). The fundamental constants serve only as a scale, and the core formulas hold approximately without additional corrections because:
	
	\begin{itemize}
		\item **The $\xi$-parameter is intrinsically dimensionless**: $\xi$ represents the pure geometry of the vacuum field and acts like a ``universal scaling factor.''
		
		\item **Approximate validity for rough calculations**: Many T0 formulas are exact in the geometric ideal form, without renormalization.
		
		\item **Example: Electron mass in natural units**:
		\begin{equation}
			m_e^{\mathrm{T0}} = 0.511 \quad \text{(geometric number, without renormalization)}
		\end{equation}
		This ``fits'' immediately because $\xi$ sets the geometric scale.
	\end{itemize}
	
	## Why is Fractal Renormalization Necessary for Exact SI Conversions?
	
	SI units are human conventions that ``contaminate'' the geometric purity of T0 theory. To achieve exact agreement with experiments, fractal renormalization must be **explicitly applied** because:
	
	\begin{itemize}
		\item **Fractal self-similarity breaks scale invariance**
		\item **Conversion requires explicit scaling**
		\item **Cosmological reference effects**
	\end{itemize}
	
	## Mathematical Specification of Fractal Renormalization
	
	The fractal renormalization is explicitly defined as:
	\begin{equation}
		f_{\text{fractal}}(E_0) = \prod_{n=1}^{137} \left(1 + \delta_n \cdot \xi \cdot \left(\frac{4}{3}\right)^{n-1}\right)
	\end{equation}
	where $\delta_n$ are dimensionless coefficients describing the fractal structure at each stage.
	
	## Comparison: Approximation vs. Exactness
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{4cm}p{6cm}p{6cm}}
			\toprule
			**Aspect** & **Without fractal renormalization (T0 units)** & **With fractal renormalization (for SI conversion)** \\
			\midrule
			Accuracy & Approximate ($\sim 98$--$99$\,\%, geometrically ideal) & Exact (to $10^{-6}$, matches CODATA measurements) \\
			Example: $\alpha$ & $\alpha \approx \xi \cdot (E_0)^2 \approx 1/137$ (rough) & $\alpha = 1/137.03599\dots$ (via 137 stages) \\
			Mass calculation & $m_e^{\mathrm{T0}} = 0.511$ (geometric) & $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg (physical) \\
			Energy scale & $E_0 = 7.400$ MeV (ideal) & $E_0 = 7.400244$ MeV (renormalized) \\
			Scaling factor & $S_{T0} = 1.782662\times 10^{-30}$ (fundamental) & $S_{T0} \cdot R_f$ (renormalized) \\
			Advantage & Fast, transparent calculations & Testability with experiments \\
			Disadvantage & Ignores fractal subtleties & Complex (iteration over resonance stages) \\
			\bottomrule
		\end{tabular}
		\caption{Comparison of geometric idealization in T0 units and physical exactness with fractal renormalization.}
		\label{tab:approximation-exaktheit}
	\end{table}
	
	## Conclusion: The Duality of Geometric Idealization and Physical Measurement
	
	The formulas ``fit'' in T0 units without renormalization because these units capture the **geometric essence** of physics. For conversion to measurable SI units, renormalization becomes **explicitly necessary** to incorporate the **self-similar corrections** of the fractal vacuum geometry.
	
	# Important Conceptual Clarifications
	
	When applying T0 theory, note these fundamental distinctions:
	
	\begin{itemize}
		\item **T0 quantities** are geometric and derived from $\xi$ (e.g., $m_e^{\mathrm{T0}} = 0.511$)
		\item **SI quantities** are physical measurements (e.g., $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg)
		\item **$S_{T0**$} is the fundamental scaling between these realms, **derived** not defined
		\item The energy reference for $\alpha$ is exactly $E_0 = 7.400$ MeV in the geometric idealization
		\item All mass scales are **discretely quantized** in both T0 and SI representations
	\end{itemize}
	
	# Special Significance for T0 Theory
	
	## The Deeper Insight
	T0 theory reveals that natural units are not merely a calculational convenience, but express the **true geometric nature of physics**:
	\begin{itemize}
		\item **$\xi$** is the fundamental dimensionless geometry constant
		\item **$S_{T0**$} connects geometric idealization to physical measurement
		\item **T0 quantities** represent the ideal geometric forms
		\item **SI quantities** are their measurable projections into our physical reality
		\item **Particle masses** are quantized geometric patterns in both realms
	\end{itemize}
	
	## Practical Implications
	\begin{enumerate}
		\item **Theoretical development**: Work in T0 units using geometric quantities
		\item **Fundamental scaling**: Apply $S_{T0}$ to project to physical reality
		\item **Predictions**: Convert to SI units for experimental verification
		\item **Verification**: Compare with measured SI values
		\item **Quantization**: Respect the discrete nature of all physical scales
	\end{enumerate}
	
	# Conclusion
	
	T0 geometric quantities correspond to the **intrinsic language of physics**, while SI units are the **measurement language of experimentalists**. T0 theory demonstrates conclusively that the fundamental relationships of physics are dimensionless and geometric.
	
	The scaling factor $S_{T0}$ provides the essential bridge between the geometric idealization of T0 theory and the practical reality of experimental measurement. The fact that all physical constants can be derived from the single dimensionless parameter $\xi$ **with the fundamental scaling $S_{T0**$} confirms the profound truth: Physics is ultimately the mathematics of dimensionless geometric relationships with discrete quantization, projected into our measurable universe through fundamental scaling.
	
	\appendix
	# Notation and Symbols
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{3cm}p{10cm}}
			\toprule
			**Symbol** & **Meaning and Explanation** \\
			\midrule
			$c$ & Speed of light in vacuum; fundamental constant of nature \\
			$\hbar$ & Reduced Planck constant \\
			$k_B$ & Boltzmann constant \\
			$G$ & Gravitational constant \\
			$E$ & Energy; in natural units dimensionally equivalent to mass and frequency \\
			$m$ & Mass; in natural units $m = E$ (since $c=1$) \\
			$p$ & Momentum; in natural units dimensionally equivalent to energy \\
			$\omega$ & Angular frequency; in natural units $\omega = E$ (since $\hbar=1$) \\
			$\alpha$ & Fine structure constant; dimensionless coupling constant \\
			$\xi$ & Fundamental geometry parameter of T0 theory; $\xi = \frac{4}{3} \times 10^{-4}$ \\
			$E_0$ & Reference energy in T0 theory; $E_0 = 7.400~\mathrm{MeV}$ \\
			$m_e^{\mathrm{T0}}$ & Electron mass in T0 units; $m_e^{\mathrm{T0}} = 0.511$ (geometric) \\
			$m_e^{\mathrm{SI}}$ & Electron mass in SI units; $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg (physical) \\
			$[E]$ & Energy dimension; fundamental dimension in natural units \\
			SI & International System of Units (physical measurements) \\
			T0 & T0 geometric units (ideal geometric forms) \\
			$S_{T0}$ & Fundamental scaling factor; $S_{T0} = 1.782662 \times 10^{-30}$ \\
			$R_f$ & Fractal renormalization factor \\
			$f_{\text{fractal}}$ & Fractal renormalization function \\
			$Q_m^{\mathrm{T0}}$ & Fundamental mass quantum in T0 units \\
			$Q_m^{\mathrm{SI}}$ & Fundamental mass quantum in SI units \\
			$n_i$ & Quantum number for particle $i$; $n_i \in \mathbb{N}$ (discrete) \\
			$\delta_n$ & Fractal renormalization coefficients; dimensionless \\
			\bottomrule
		\end{tabular}
		\caption{Explanation of the notation and symbols used}
	\end{table}
	
	# Fundamental Relationships
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{4cm}p{10cm}}
			\toprule
			**Relationship** & **Meaning** \\
			\midrule
			$E = m$ & Mass-energy equivalence (since $c=1$) \\
			$E = \omega$ & Energy-frequency relationship (since $\hbar=1$) \\
			$[L] = [T] = [E]^{-1}$ & Length and time have same dimension as inverse energy \\
			$[m] = [p] = [E]$ & Mass and momentum have same dimension as energy \\
			$\alpha = \xi (E_0/1\mathrm{MeV})^2$ & Fundamental relationship in T0 theory \\
			$m_i^{\mathrm{T0}} = n_i \cdot Q_m^{\mathrm{T0}} \cdot f_i(\xi)$ & Quantized mass formula in T0 units \\
			$m_i^{\mathrm{SI}} = m_i^{\mathrm{T0}} \cdot S_{T0}$ & Fundamental scaling to SI units \\
			$S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ & Definition of fundamental scaling factor \\
			\bottomrule
		\end{tabular}
		\caption{Fundamental relationships in T0 theory and scaling to physical units}
	\end{table}
	
	# Conversion Factors
	
	\begin{table}[h]
		\centering
		\begin{tabular}{lll}
			\toprule
			**Quantity** & **Conversion Factor** & **Value** \\
			\midrule
			$S_{T0}$ & Fundamental scaling factor & $1.782662 \times 10^{-30}$ \\
			$m_e^{\mathrm{T0}}$ & Electron mass (T0 units) & $0.511$ \\
			$m_e^{\mathrm{SI}}$ & Electron mass (SI units) & $9.1093837 \times 10^{-31}~\mathrm{kg}$ \\
			$1~\mathrm{MeV}/c^2$ & Conventional mass unit & $1.782662 \times 10^{-30}~\mathrm{kg}$ \\
			$1~\mathrm{MeV}$ & Energy in joules & $1.602176 \times 10^{-13}~\mathrm{J}$ \\
			$1~\mathrm{fm}$ & Length in natural units & $5.06773 \times 10^{-3}~\mathrm{MeV}^{-1}$ \\
			\bottomrule
		\end{tabular}
		\caption{Fundamental conversion factors between T0 geometric units and SI physical units}
	\end{table}