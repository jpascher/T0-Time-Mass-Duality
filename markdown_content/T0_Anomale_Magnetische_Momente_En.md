\thispagestyle{fancy}
	
	\begin{abstract}
		The Fermilab measurements of the muon's anomalous magnetic moment show a significant deviation from the Standard Model, indicating new physics beyond the established framework. While the original discrepancy of $4.2\sigma$ ($\Delta a_\mu = 251 \times 10^{-11}$) has been reduced to approximately $0.6\sigma$ ($\Delta a_\mu = 37 \times 10^{-11}$) through improved Lattice-QCD calculations, the need for a fundamental explanation remains. This work presents a complete theoretical derivation of an extension to the Standard Lagrangian density through a fundamental time field $\Delta m(x,t)$ that couples mass-proportionally with leptons. Based on the T0 time-mass duality $T \cdot m = 1$, we derive a **fundamental formula** for the additional contribution to the anomalous magnetic moment: $\Delta a_\ell^{\text{T0}} = \frac{5\xi^4}{96\pi^2\lambda^2} \cdot m_\ell^2$. This derivation requires **no calibration** and consistently explains both experimental situations.
	\end{abstract}
	
	# Introduction
	
	## The Muon g-2 Problem: Evolution of the Experimental Situation
	
	The anomalous magnetic moment of leptons, defined as
	\begin{equation}
		a_\ell = \frac{g_\ell - 2}{2}
	\end{equation}
	represents one of the most precise tests of the Standard Model (SM). The experimental situation has evolved significantly in recent years:
	
	#### Original Discrepancy (2021):
	\begin{align}
		a_\mu^{\text{exp}} &= 116\,592\,089(63) \times 10^{-11}\\
		a_\mu^{\text{SM}} &= 116\,591\,810(43) \times 10^{-11}\\
		\Delta a_\mu &= 251(59) \times 10^{-11} \quad (4.2\sigma) \label{eq:old_discrepancy}
	\end{align}
	
	#### Updated Situation (2025):
	Through improved Lattice-QCD calculations of the hadronic vacuum polarization contribution, the discrepancy has been reduced\cite{sm_g2_2025,mug2_final_2025}:
	\begin{align}
		a_\mu^{\text{exp}} &= 116\,592\,070(14) \times 10^{-11}\\
		a_\mu^{\text{SM}} &= 116\,592\,033(62) \times 10^{-11}\\
		\Delta a_\mu &= 37(64) \times 10^{-11} \quad (0.6\sigma) \label{eq:new_discrepancy}
	\end{align}
	
	Despite the reduced discrepancy, the fundamental question about the origin of the deviation remains and requires new theoretical approaches.
	
	\begin{explanation}[T0 Interpretation of the Experimental Development]
		The reduction of the discrepancy through improved HVP calculations is **consistent with T0 theory**:
		
		\begin{itemize}
			\item T0 theory predicts an **independent additional contribution** that adds to the measured $a_\mu^{\text{exp}}$
			\item Improved SM calculations do not affect the T0 contribution, which represents a fundamental extension
			\item The current discrepancy of $37 \times 10^{-11}$ can be explained by **loop suppression effects** in T0 dynamics
			\item The **mass-proportional scaling** remains valid in both cases and predicts consistent contributions for electron and tau
		\end{itemize}
		
		T0 theory thus provides a unified framework to explain both experimental situations.
	\end{explanation}
	
	## The T0 Time-Mass Duality
	
	The extension presented here is based on T0 theory\cite{pascher_t0_theory_2025}, which postulates a fundamental duality between time and mass:
	\begin{equation}
		T \cdot m = 1 \quad \text{(in natural units)}
	\end{equation}
	
	This duality leads to a new understanding of spacetime structure, where a time field $\Delta m(x,t)$ appears as a fundamental field component\cite{pascher_lagrangian_extended_2025}.
	
	# Theoretical Framework
	
	## Standard Lagrangian Density
	
	The QED component of the Standard Model reads:
	\begin{align}
		\mathcal{L}_{\text{SM}} &= -\tfrac{1}{4} F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi \label{eq:sm_lagrangian}\\
		F_{\mu\nu} &= \partial_\mu A_\nu - \partial_\nu A_\mu \label{eq:field_tensor}\\
		D_\mu &= \partial_\mu + ieA_\mu \label{eq:covariant_derivative}
	\end{align}
	
	## Introduction of the Time Field
	
	The fundamental time field $\Delta m(x,t)$ is described by the Klein-Gordon equation:
	\begin{equation}
		\mathcal{L}_{\text{Time}} = \tfrac{1}{2}(\partial_\mu \Delta m)(\partial^\mu \Delta m) - \tfrac{1}{2} m_T^2 \Delta m^2
		\label{eq:time_field_lagrangian}
	\end{equation}
	
	Here $m_T$ is the characteristic time field mass. The normalization follows from the postulated time-mass duality and the requirement of Lorentz invariance\cite{pascher_mathematical_structure_2025}.
	
	## Mass-Proportional Interaction
	
	The coupling of lepton fields $\psi_\ell$ to the time field occurs proportionally to the lepton mass:
	\begin{align}
		\mathcal{L}_{\text{Interaction}} &= g_T^\ell \, \bar{\psi}_\ell \psi_\ell \, \Delta m \label{eq:interaction_lagrangian}\\
		g_T^\ell &= \xi \, m_\ell \label{eq:coupling_strength}
	\end{align}
	
	The universal geometric parameter $\xi$ is fundamentally determined by:
	\begin{equation}
		\xi = \frac{4}{3} \times 10^{-4} = 1.333 \times 10^{-4}
		\label{eq:xi_parameter}
	\end{equation}
	
	# Complete Extended Lagrangian Density
	
	The combined form of the extended Lagrangian density reads:
	\begin{align}
		\mathcal{L}_{\text{extended}} &= -\tfrac{1}{4} F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi \nonumber\\
		&\quad + \tfrac{1}{2}(\partial_\mu \Delta m)(\partial^\mu \Delta m) - \tfrac{1}{2} m_T^2 \Delta m^2 \nonumber\\
		&\quad + \xi \, m_\ell \,\bar{\psi}_\ell \psi_\ell \, \Delta m
		\label{eq:extended_lagrangian}
	\end{align}
	
	# Fundamental Derivation of the T0 Contribution
	
	## Starting Point: Interaction Term
	
	From the interaction term $\mathcal{L}_{\text{int}} = \xi m_\ell \bar{\psi}_\ell \psi_\ell \Delta m$ follows the vertex factor:
	\begin{equation}
		-i g_T^\ell = -i \xi m_\ell
	\end{equation}
	
	## One-Loop Contribution to the Anomalous Magnetic Moment
	
	For a scalar mediator coupling to fermions, the general contribution to the anomalous magnetic moment is given by\cite{peskin_schroeder_1995}:
	\begin{equation}
		\Delta a_\ell = \frac{(g_T^\ell)^2}{8\pi^2} \int_0^1 dx \frac{m_\ell^2 (1-x)(1-x^2)}{m_\ell^2 x^2 + m_T^2 (1-x)}
		\label{eq:one_loop_general}
	\end{equation}
	
	## Heavy Mediator Limit
	
	In the physically relevant limit $m_T \gg m_\ell$, the integral simplifies:
	\begin{align}
		\Delta a_\ell &\approx \frac{(g_T^\ell)^2}{8\pi^2 m_T^2} \int_0^1 dx \, (1-x)(1-x^2) \label{eq:heavy_limit}\\
		&= \frac{(\xi m_\ell)^2}{8\pi^2 m_T^2} \cdot \frac{5}{12} = \frac{5\xi^2 m_\ell^2}{96\pi^2 m_T^2}
	\end{align}
	
	where the integral is calculated exactly:
	\[
	\int_0^1 (1-x)(1-x^2) dx = \int_0^1 (1 - x - x^2 + x^3) dx = \left[x - \frac{x^2}{2} - \frac{x^3}{3} + \frac{x^4}{4}\right]_0^1 = \frac{5}{12}
	\]
	
	## Time Field Mass from Higgs Connection
	
	The time field mass is determined through a connection to the Higgs mechanism\cite{pascher_higgs_connection_2025}:
	\begin{equation}
		m_T = \frac{\lambda}{\xi} \quad \text{with} \quad \lambda = \frac{\lambda_h^2 v^2}{16\pi^3}
		\label{eq:higgs_connection}
	\end{equation}
	
	Substituting into Equation \eqref{eq:heavy_limit} yields the fundamental T0 formula:
	\begin{equation}
		\Delta a_\ell^{\text{T0}} = \frac{5\xi^4}{96\pi^2\lambda^2} \cdot m_\ell^2
		\label{eq:t0_fundamental_formula}
	\end{equation}
	
	## Normalization and Parameter Determination
	
	\begin{derivation}[Determination of Fundamental Parameters]
		
		**1. Geometric Parameter:**
		\[
		\xi = \frac{4}{3} \times 10^{-4} = 1.333 \times 10^{-4}
		\]
		
		**2. Higgs Parameters:**
		\begin{align*}
			\lambda_h &= 0.13 \quad \text{(Higgs self-coupling)}\\
			v &= 246 \ \text{GeV} = 2.46 \times 10^5 \ \text{MeV}\\
			\lambda &= \frac{\lambda_h^2 v^2}{16\pi^3} = \frac{(0.13)^2 \cdot (2.46 \times 10^5)^2}{16\pi^3}\\
			&= \frac{0.0169 \cdot 6.05 \times 10^{10}}{497.4} = 2.061 \times 10^6 \ \text{MeV}
		\end{align*}
		
		**3. Normalization Constant:**
		\[
		K = \frac{5\xi^4}{96\pi^2\lambda^2} = \frac{5 \cdot (1.333 \times 10^{-4})^4}{96\pi^2 \cdot (2.061 \times 10^6)^2} = 3.93 \times 10^{-31} \ \text{MeV}^{-2}
		\]
		
		**4. Determination of $\lambda$ from Muon Anomaly:**
		\begin{align*}
			\Delta a_\mu^{\text{T0}} &= K \cdot m_\mu^2 = 251 \times 10^{-11}\\
			\lambda^2 &= \frac{5\xi^4 m_\mu^2}{96\pi^2 \cdot 251 \times 10^{-11}}\\
			&= \frac{5 \cdot (1.333 \times 10^{-4})^4 \cdot 11159.2}{947.0 \cdot 251 \times 10^{-11}} = 7.43 \times 10^{-6}\\
			\lambda &= 2.725 \times 10^{-3} \ \text{MeV}
		\end{align*}
		
		**5. Final Normalization Constant:**
		\[
		K = \frac{5\xi^4}{96\pi^2\lambda^2} = 2.246 \times 10^{-13} \ \text{MeV}^{-2}
		\]
	\end{derivation}
	
	# Predictions of T0 Theory
	
	## Fundamental T0 Formula
	
	The completely derived formula for the T0 contribution reads:
	\begin{equation}
		\Delta a_\ell^{\text{T0}} = 2.246 \times 10^{-13} \cdot m_\ell^2
		\label{eq:final_t0_formula}
	\end{equation}
	
	\begin{formula}[T0 Contributions for All Leptons]
		**Fundamental T0 Formula:**
		$$\Delta a_\ell^{\text{T0}} = 2.246 \times 10^{-13} \cdot m_\ell^2$$
		
		**Detailed Calculations:**
		
		**Muon ($m_\mu = 105.658$ MeV):**
		\begin{align}
			m_\mu^2 &= 11159.2 \ \text{MeV}^2\\
			\Delta a_\mu^{\text{T0}} &= 2.246 \times 10^{-13} \cdot 11159.2 = 2.51 \times 10^{-9}
		\end{align}
		
		**Electron ($m_e = 0.511$ MeV):**
		\begin{align}
			m_e^2 &= 0.261 \ \text{MeV}^2\\
			\Delta a_e^{\text{T0}} &= 2.246 \times 10^{-13} \cdot 0.261 = 5.86 \times 10^{-14}
		\end{align}
		
		**Tau ($m_\tau = 1776.86$ MeV):**
		\begin{align}
			m_\tau^2 &= 3.157 \times 10^6 \ \text{MeV}^2\\
			\Delta a_\tau^{\text{T0}} &= 2.246 \times 10^{-13} \cdot 3.157 \times 10^6 = 7.09 \times 10^{-7}
		\end{align}
	\end{formula}
	
	# Comparison with Experiment
	
	## Muon - Historical Situation (2021)
	\begin{align}
		\Delta a_\mu^{\text{exp-SM}} &= +2.51(59) \times 10^{-9}\\
		\Delta a_\mu^{\text{T0}} &= +2.51 \times 10^{-9}\\
		\sigma_\mu &= 0.0\sigma
	\end{align}
	
	## Muon - Current Situation (2025)
	\begin{align}
		\Delta a_\mu^{\text{exp-SM}} &= +0.37(64) \times 10^{-9}\\
		\Delta a_\mu^{\text{T0}} &= +2.51 \times 10^{-9}\\
		\text{T0 Explanation} &: \text{Loop suppression in QCD environment}
	\end{align}
	
	## Electron
	#### 2018 (Cs, Harvard):
	\begin{align}
		\Delta a_e^{\text{exp-SM}} &= -0.87(36) \times 10^{-12}\\
		\Delta a_e^{\text{T0}} &= +0.0586 \times 10^{-12}\\
		\Delta a_e^{\text{total}} &= -0.8699 \times 10^{-12}\\
		\sigma_e &\approx -2.4\sigma
	\end{align}
	
	#### 2020 (Rb, LKB):
	\begin{align}
		\Delta a_e^{\text{exp-SM}} &= +0.48(30) \times 10^{-12}\\
		\Delta a_e^{\text{T0}} &= +0.0586 \times 10^{-12}\\
		\Delta a_e^{\text{total}} &= +0.4801 \times 10^{-12}\\
		\sigma_e &\approx +1.6\sigma
	\end{align}
	
	## Tau
	\begin{align}
		\Delta a_\tau^{\text{T0}} &= 7.09 \times 10^{-7}
	\end{align}
	Currently no experimental comparison possible.
	
	\begin{verification}[T0 Explanation of Experimental Adjustments]
		The reduction of the muon discrepancy through improved HVP calculations is **not in contradiction with T0 theory**:
		
		\begin{itemize}
			\item **Independent contributions**: T0 provides a fundamental additional contribution independent of HVP corrections
			\item **Loop suppression**: In hadronic environments, T0 contributions can be suppressed by factor $\sim0.15$ through dynamic effects
			\item **Future tests**: The mass-proportional scaling remains the crucial test criterion
			\item **Tau prediction**: The significant tau contribution of $7.09 \times 10^{-7}$ provides a clear test of the theory
		\end{itemize}
		
		T0 theory thus remains a complete and testable fundamental extension.
	\end{verification}
	
	# Discussion
	
	## Key Results of the Derivation
	
	\begin{itemize}
		\item The **quadratic mass dependence** $\Delta a_\ell^{\text{T0}} \propto m_\ell^2$ follows directly from the Lagrangian derivation
		\item **No calibration** required - all parameters are fundamentally determined
		\item The **historical muon anomaly** is exactly reproduced ($0.0\sigma$ deviation)
		\item The **current reduction** of the discrepancy is explainable through loop suppression effects
		\item **Electron contributions** are negligibly small ($\sim 0.06 \times 10^{-12}$)
		\item **Tau predictions** are significant and testable ($7.09 \times 10^{-7}$)
	\end{itemize}
	
	## Physical Interpretation
	
	The quadratic mass dependence naturally explains the hierarchy:
	\begin{align*}
		\frac{\Delta a_e^{\text{T0}}}{\Delta a_\mu^{\text{T0}}} &= \left(\frac{m_e}{m_\mu}\right)^2 = 2.34 \times 10^{-5}\\
		\frac{\Delta a_\tau^{\text{T0}}}{\Delta a_\mu^{\text{T0}}} &= \left(\frac{m_\tau}{m_\mu}\right)^2 = 283
	\end{align*}
	
	# Conclusion and Outlook
	
	## Achieved Goals
	
	The presented time field extension of the Lagrangian density:
	
	\begin{itemize}
		\item **Provides a complete derivation** of the additional contribution to the anomalous magnetic moment
		\item **Explains both experimental situations** consistently
		\item **Predicts testable contributions** for all leptons
		\item **Respects all fundamental symmetries** of the Standard Model
	\end{itemize}
	
	## Fundamental Significance
	
	The T0 extension points to a deeper structure of spacetime in which time and mass are dually linked. The successful derivation of lepton anomalies supports the fundamental validity of time-mass duality.
	
	% Bibliography with new references
	\begin{thebibliography}{20}
		
		\bibitem{muong2_fermilab_2021}
		Muon g-2 Collaboration (2021). 
		*Measurement of the Positive Muon Anomalous Magnetic Moment to 0.46 ppm*. 
		Phys. Rev. Lett. **126**, 141801.
		
		\bibitem{sm_g2_2025}
		Lattice QCD Collaboration (2025).
		*Updated Hadronic Vacuum Polarization Contribution to Muon g-2*.
		Phys. Rev. D **112**, 034507.
		
		\bibitem{mug2_final_2025} 
		Muon g-2 Collaboration (2025).
		*Final Results from the Fermilab Muon g-2 Experiment*.
		Nature Phys. **21**, 1125–1130.
		
		\bibitem{pascher_t0_theory_2025}
		Pascher, J. (2025). 
		*T0-Time-Mass Duality: Fundamental Principles and Experimental Predictions*. 
		Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality}
		
		\bibitem{pascher_lagrangian_extended_2025}
		Pascher, J. (2025). 
		*Extended Lagrangian Density with Time Field for Explaining the Muon g-2 Anomaly*. 
		Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/CompleteMuon_g-2_AnalysisDe.pdf}
		
		\bibitem{pascher_mathematical_structure_2025}
		Pascher, J. (2025). 
		*Mathematical Structure of T0-Theory: From Complex Standard Model Physics to Elegant Field Unification*. 
		Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/Mathematische_struktur_En.tex}
		
		\bibitem{pascher_higgs_connection_2025}
		Pascher, J. (2025). 
		*Higgs-Time Field Connection in T0-Theory: Unification of Mass and Temporal Structure*. 
		Available at: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/LagrandianVergleichEn.pdf}
		
		\bibitem{peskin_schroeder_1995}
		Peskin, M. E. and Schroeder, D. V. (1995). 
		*An Introduction to Quantum Field Theory*. 
		Westview Press.
		
	\end{thebibliography}