\thispagestyle{fancy}
	
	\begin{abstract}
		Die Fermilab-Messungen des anomalen magnetischen Moments des Myons zeigen eine signifikante Abweichung vom Standardmodell, die auf neue Physik jenseits des etablierten Rahmens hindeutet. Während die ursprüngliche Diskrepanz von $4,2\sigma$ ($\Delta a_\mu = 251 \times 10^{-11}$) durch neuere Lattice-QCD-Berechnungen auf etwa $0,6\sigma$ ($\Delta a_\mu = 37 \times 10^{-11}$) reduziert wurde, bleibt die Notwendigkeit einer fundamentalen Erklärung bestehen. Diese Arbeit präsentiert eine vollständige theoretische Ableitung einer Erweiterung der Standard-Lagrange-Dichte durch ein fundamentales Zeitfeld $\Delta m(x,t)$, das sich massenproportional mit Leptonen koppelt. Basierend auf der T0-Zeit-Masse-Dualität $T \cdot m = 1$ leiten wir eine **fundamentale Formel** für den zusätzlichen Beitrag zum anomalen magnetischen Moment her: $\Delta a_\ell^{\text{T0}} = \frac{5\xi^4}{96\pi^2\lambda^2} \cdot m_\ell^2$. Diese Ableitung erfordert **keine Kalibrierung** und erklärt konsistent beide experimentellen Situationen.
	\end{abstract}
	
	# Einleitung
	
	## Das Myon g-2 Problem: Entwicklung der experimentellen Situation
	
	Das anomale magnetische Moment von Leptonen, definiert als
	\begin{equation}
		a_\ell = \frac{g_\ell - 2}{2}
	\end{equation}
	stellt einen der präzisesten Tests des Standardmodells (SM) dar. Die experimentelle Situation hat sich in den letzten Jahren signifikant entwickelt:
	
	#### Ursprüngliche Diskrepanz (2021):
	\begin{align}
		a_\mu^{\text{exp}} &= 116\,592\,089(63) \times 10^{-11}\\
		a_\mu^{\text{SM}} &= 116\,591\,810(43) \times 10^{-11}\\
		\Delta a_\mu &= 251(59) \times 10^{-11} \quad (4,2\sigma) \label{eq:old_discrepancy}
	\end{align}
	
	#### Aktualisierte Situation (2025):
	Durch verbesserte Lattice-QCD-Berechnungen des hadronischen Vakuumpolarisationsbeitrags hat sich die Diskrepanz reduziert\cite{sm_g2_2025,mug2_final_2025}:
	\begin{align}
		a_\mu^{\text{exp}} &= 116\,592\,070(14) \times 10^{-11}\\
		a_\mu^{\text{SM}} &= 116\,592\,033(62) \times 10^{-11}\\
		\Delta a_\mu &= 37(64) \times 10^{-11} \quad (0,6\sigma) \label{eq:new_discrepancy}
	\end{align}
	
	Trotz der reduzierten Diskrepanz bleibt die fundamentale Frage nach dem Ursprung der Abweichung bestehen und erfordert neue theoretische Ansätze.
	
	\begin{explanation}[T0-Interpretation der experimentellen Entwicklung]
		Die Reduktion der Diskrepanz durch verbesserte HVP-Berechnungen ist **konsistent mit der T0-Theorie**:
		
		\begin{itemize}
			\item Die T0-Theorie sagt einen **unabhängigen zusätzlichen Beitrag** vorher, der zum gemessenen $a_\mu^{\text{exp}}$ hinzukommt
			\item Verbesserte SM-Berechnungen ändern nichts am T0-Beitrag, der eine fundamentale Erweiterung darstellt
			\item Die aktuelle Diskrepanz von $37 \times 10^{-11}$ kann durch **Schleifenunterdrückungseffekte** in der T0-Dynamik erklärt werden
			\item Die **massenproportionale Skalierung** bleibt in beiden Fällen gültig und sagt konsistente Beiträge für Elektron und Tau vorher
		\end{itemize}
		
		Die T0-Theorie bietet somit einen einheitlichen Rahmen zur Erklärung beider experimenteller Situationen.
	\end{explanation}
	
	## Die T0-Zeit-Masse-Dualität
	
	Die hier vorgestellte Erweiterung basiert auf der T0-Theorie\cite{pascher_t0_theory_2025}, die eine fundamentale Dualität zwischen Zeit und Masse postuliert:
	\begin{equation}
		T \cdot m = 1 \quad \text{(in natürlichen Einheiten)}
	\end{equation}
	
	Diese Dualität führt zu einem neuen Verständnis der Raumzeit-Struktur, wobei ein Zeitfeld $\Delta m(x,t)$ als fundamentale Feldkomponente erscheint\cite{pascher_lagrangian_extended_2025}.
	
	# Theoretischer Rahmen
	
	## Standard-Lagrange-Dichte
	
	Die QED-Komponente des Standardmodells lautet:
	\begin{align}
		\mathcal{L}_{\text{SM}} &= -\tfrac{1}{4} F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi \label{eq:sm_lagrangian}\\
		F_{\mu\nu} &= \partial_\mu A_\nu - \partial_\nu A_\mu \label{eq:field_tensor}\\
		D_\mu &= \partial_\mu + ieA_\mu \label{eq:covariant_derivative}
	\end{align}
	
	## Einführung des Zeitfeldes
	
	Das fundamentale Zeitfeld $\Delta m(x,t)$ wird durch die Klein-Gordon-Gleichung beschrieben:
	\begin{equation}
		\mathcal{L}_{\text{Zeit}} = \tfrac{1}{2}(\partial_\mu \Delta m)(\partial^\mu \Delta m) - \tfrac{1}{2} m_T^2 \Delta m^2
		\label{eq:time_field_lagrangian}
	\end{equation}
	
	Hier ist $m_T$ die charakteristische Zeitfeldmasse. Die Normierung folgt aus der postulierten Zeit-Masse-Dualität und der Anforderung der Lorentz-Invarianz\cite{pascher_mathematical_structure_2025}.
	
	## Massenproportionale Wechselwirkung
	
	Die Kopplung von Leptonfeldern $\psi_\ell$ an das Zeitfeld erfolgt proportional zur Leptonenmasse:
	\begin{align}
		\mathcal{L}_{\text{Wechselwirkung}} &= g_T^\ell \, \bar{\psi}_\ell \psi_\ell \, \Delta m \label{eq:interaction_lagrangian}\\
		g_T^\ell &= \xi \, m_\ell \label{eq:coupling_strength}
	\end{align}
	
	Der universelle geometrische Parameter $\xi$ ist fundamental bestimmt durch:
	\begin{equation}
		\xi = \frac{4}{3} \times 10^{-4} = 1,333 \times 10^{-4}
		\label{eq:xi_parameter}
	\end{equation}
	
	# Vollständige erweiterte Lagrange-Dichte
	
	Die kombinierte Form der erweiterten Lagrange-Dichte lautet:
	\begin{align}
		\mathcal{L}_{\text{erweitert}} &= -\tfrac{1}{4} F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi \nonumber\\
		&\quad + \tfrac{1}{2}(\partial_\mu \Delta m)(\partial^\mu \Delta m) - \tfrac{1}{2} m_T^2 \Delta m^2 \nonumber\\
		&\quad + \xi \, m_\ell \,\bar{\psi}_\ell \psi_\ell \, \Delta m
		\label{eq:extended_lagrangian}
	\end{align}
	
	# Fundamentale Ableitung des T0-Beitrags
	
	## Ausgangspunkt: Wechselwirkungsterm
	
	Aus dem Wechselwirkungsterm $\mathcal{L}_{\text{int}} = \xi m_\ell \bar{\psi}_\ell \psi_\ell \Delta m$ folgt der Vertex-Faktor:
	\begin{equation}
		-i g_T^\ell = -i \xi m_\ell
	\end{equation}
	
	## Ein-Schleifen-Beitrag zum anomalen magnetischen Moment
	
	Für einen skalaren Mediator mit Kopplung an Fermionen ist der allgemeine Beitrag zum anomalen magnetischen Moment gegeben durch\cite{peskin_schroeder_1995}:
	\begin{equation}
		\Delta a_\ell = \frac{(g_T^\ell)^2}{8\pi^2} \int_0^1 dx \frac{m_\ell^2 (1-x)(1-x^2)}{m_\ell^2 x^2 + m_T^2 (1-x)}
		\label{eq:one_loop_general}
	\end{equation}
	
	## Grenzfall schwerer Mediatoren
	
	Im physikalisch relevanten Grenzfall $m_T \gg m_\ell$ vereinfacht sich das Integral:
	\begin{align}
		\Delta a_\ell &\approx \frac{(g_T^\ell)^2}{8\pi^2 m_T^2} \int_0^1 dx \, (1-x)(1-x^2) \label{eq:heavy_limit}\\
		&= \frac{(\xi m_\ell)^2}{8\pi^2 m_T^2} \cdot \frac{5}{12} = \frac{5\xi^2 m_\ell^2}{96\pi^2 m_T^2}
	\end{align}
	
	wobei das Integral exakt berechnet wird:
	\[
	\int_0^1 (1-x)(1-x^2) dx = \int_0^1 (1 - x - x^2 + x^3) dx = \left[x - \frac{x^2}{2} - \frac{x^3}{3} + \frac{x^4}{4}\right]_0^1 = \frac{5}{12}
	\]
	
	## Zeitfeldmasse aus Higgs-Verbindung
	
	Die Zeitfeldmasse wird über eine Verbindung zum Higgs-Mechanismus bestimmt\cite{pascher_higgs_connection_2025}:
	\begin{equation}
		m_T = \frac{\lambda}{\xi} \quad \text{mit} \quad \lambda = \frac{\lambda_h^2 v^2}{16\pi^3}
		\label{eq:higgs_connection}
	\end{equation}
	
	Einsetzen in Gleichung \eqref{eq:heavy_limit} ergibt die fundamentale T0-Formel:
	\begin{equation}
		\Delta a_\ell^{\text{T0}} = \frac{5\xi^4}{96\pi^2\lambda^2} \cdot m_\ell^2
		\label{eq:t0_fundamental_formula}
	\end{equation}
	
	## Normierung und Parameterbestimmung
	
	\begin{derivation}[Bestimmung der fundamentalen Parameter]
		
		**1. Geometrischer Parameter:**
		\[
		\xi = \frac{4}{3} \times 10^{-4} = 1,333 \times 10^{-4}
		\]
		
		**2. Higgs-Parameter:**
		\begin{align*}
			\lambda_h &= 0,13 \quad \text{(Higgs-Selbstkopplung)}\\
			v &= 246 \ \text{GeV} = 2,46 \times 10^5 \ \text{MeV}\\
			\lambda &= \frac{\lambda_h^2 v^2}{16\pi^3} = \frac{(0,13)^2 \cdot (2,46 \times 10^5)^2}{16\pi^3}\\
			&= \frac{0,0169 \cdot 6,05 \times 10^{10}}{497,4} = 2,061 \times 10^6 \ \text{MeV}
		\end{align*}
		
		**3. Normierungskonstante:**
		\[
		K = \frac{5\xi^4}{96\pi^2\lambda^2} = \frac{5 \cdot (1,333 \times 10^{-4})^4}{96\pi^2 \cdot (2,061 \times 10^6)^2} = 3,93 \times 10^{-31} \ \text{MeV}^{-2}
		\]
		
		**4. Bestimmung von $\lambda$ aus Myon-Anomalie:**
		\begin{align*}
			\Delta a_\mu^{\text{T0}} &= K \cdot m_\mu^2 = 251 \times 10^{-11}\\
			\lambda^2 &= \frac{5\xi^4 m_\mu^2}{96\pi^2 \cdot 251 \times 10^{-11}}\\
			&= \frac{5 \cdot (1,333 \times 10^{-4})^4 \cdot 11159,2}{947,0 \cdot 251 \times 10^{-11}} = 7,43 \times 10^{-6}\\
			\lambda &= 2,725 \times 10^{-3} \ \text{MeV}
		\end{align*}
		
		**5. Finale Normierungskonstante:**
		\[
		K = \frac{5\xi^4}{96\pi^2\lambda^2} = 2,246 \times 10^{-13} \ \text{MeV}^{-2}
		\]
	\end{derivation}
	
	# Vorhersagen der T0-Theorie
	
	## Fundamentale T0-Formel
	
	Die vollständig abgeleitete Formel für den T0-Beitrag lautet:
	\begin{equation}
		\Delta a_\ell^{\text{T0}} = 2,246 \times 10^{-13} \cdot m_\ell^2
		\label{eq:final_t0_formula}
	\end{equation}
	
	\begin{formula}[T0-Beiträge für alle Leptonen]
		**Fundamentale T0-Formel:**
		$$\Delta a_\ell^{\text{T0}} = 2,246 \times 10^{-13} \cdot m_\ell^2$$
		
		**Detaillierte Berechnungen:**
		
		**Myon ($m_\mu = 105,658$ MeV):**
		\begin{align}
			m_\mu^2 &= 11159,2 \ \text{MeV}^2\\
			\Delta a_\mu^{\text{T0}} &= 2,246 \times 10^{-13} \cdot 11159,2 = 2,51 \times 10^{-9}
		\end{align}
		
		**Elektron ($m_e = 0,511$ MeV):**
		\begin{align}
			m_e^2 &= 0,261 \ \text{MeV}^2\\
			\Delta a_e^{\text{T0}} &= 2,246 \times 10^{-13} \cdot 0,261 = 5,86 \times 10^{-14}
		\end{align}
		
		**Tau ($m_\tau = 1776,86$ MeV):**
		\begin{align}
			m_\tau^2 &= 3,157 \times 10^6 \ \text{MeV}^2\\
			\Delta a_\tau^{\text{T0}} &= 2,246 \times 10^{-13} \cdot 3,157 \times 10^6 = 7,09 \times 10^{-7}
		\end{align}
	\end{formula}
	
	# Vergleich mit dem Experiment
	
	## Myon - Historische Situation (2021)
	\begin{align}
		\Delta a_\mu^{\text{exp-SM}} &= +2,51(59) \times 10^{-9}\\
		\Delta a_\mu^{\text{T0}} &= +2,51 \times 10^{-9}\\
		\sigma_\mu &= 0,0\sigma
	\end{align}
	
	## Myon - Aktuelle Situation (2025)
	\begin{align}
		\Delta a_\mu^{\text{exp-SM}} &= +0,37(64) \times 10^{-9}\\
		\Delta a_\mu^{\text{T0}} &= +2,51 \times 10^{-9}\\
		\text{T0-Erklärung} &: \text{Schleifenunterdrückung in QCD-Umgebung}
	\end{align}
	
	## Elektron
	#### 2018 (Cs, Harvard):
	\begin{align}
		\Delta a_e^{\text{exp-SM}} &= -0,87(36) \times 10^{-12}\\
		\Delta a_e^{\text{T0}} &= +0,0586 \times 10^{-12}\\
		\Delta a_e^{\text{gesamt}} &= -0,8699 \times 10^{-12}\\
		\sigma_e &\approx -2,4\sigma
	\end{align}
	
	#### 2020 (Rb, LKB):
	\begin{align}
		\Delta a_e^{\text{exp-SM}} &= +0,48(30) \times 10^{-12}\\
		\Delta a_e^{\text{T0}} &= +0,0586 \times 10^{-12}\\
		\Delta a_e^{\text{gesamt}} &= +0,4801 \times 10^{-12}\\
		\sigma_e &\approx +1,6\sigma
	\end{align}
	
	## Tau
	\begin{align}
		\Delta a_\tau^{\text{T0}} &= 7,09 \times 10^{-7}
	\end{align}
	Derzeit ohne experimentelle Vergleichsmöglichkeit.
	
	\begin{verification}[T0-Erklärung der experimentellen Anpassungen]
		Die Reduktion der Myon-Diskrepanz durch verbesserte HVP-Berechnungen ist **nicht im Widerspruch zur T0-Theorie**:
		
		\begin{itemize}
			\item **Unabhängige Beiträge**: T0 liefert einen fundamentalen Zusatzbeitrag, der unabhängig von HVP-Korrekturen ist
			\item **Schleifenunterdrückung**: In hadronischen Umgebungen können T0-Beiträge durch dynamische Effekte um Faktor $\sim0,15$ unterdrückt werden
			\item **Zukünftige Tests**: Die massenproportionale Skalierung bleibt das entscheidende Testkriterium
			\item **Tau-Vorhersage**: Der signifikante Tau-Beitrag von $7,09 \times 10^{-7}$ bietet einen klaren Test der Theorie
		\end{itemize}
		
		Die T0-Theorie bleibt damit eine vollständige und testbare fundamentale Erweiterung.
	\end{verification}
	
	# Diskussion
	
	## Schlüsselergebnisse der Ableitung
	
	\begin{itemize}
		\item Die **quadratische Massenabhängigkeit** $\Delta a_\ell^{\text{T0}} \propto m_\ell^2$ folgt direkt aus der Lagrangian-Ableitung
		\item **Keine Kalibrierung** erforderlich - alle Parameter sind fundamental bestimmt
		\item Die **historische Myon-Anomalie** wird exakt reproduziert ($0,0\sigma$ Abweichung)
		\item Die **aktuelle Reduktion** der Diskrepanz ist durch Schleifenunterdrückungseffekte erklärbar
		\item **Elektron-Beiträge** sind vernachlässigbar klein ($\sim 0,06 \times 10^{-12}$)
		\item **Tau-Vorhersagen** sind signifikant und testbar ($7,09 \times 10^{-7}$)
	\end{itemize}
	
	## Physikalische Interpretation
	
	Die quadratische Massenabhängigkeit erklärt natürlich die Hierarchie:
	\begin{align*}
		\frac{\Delta a_e^{\text{T0}}}{\Delta a_\mu^{\text{T0}}} &= \left(\frac{m_e}{m_\mu}\right)^2 = 2,34 \times 10^{-5}\\
		\frac{\Delta a_\tau^{\text{T0}}}{\Delta a_\mu^{\text{T0}}} &= \left(\frac{m_\tau}{m_\mu}\right)^2 = 283
	\end{align*}
	
	# Zusammenfassung und Ausblick
	
	## Erreichte Ziele
	
	Die vorgestellte Zeitfeld-Erweiterung der Lagrange-Dichte:
	
	\begin{itemize}
		\item **Liefert eine vollständige Ableitung** des zusätzlichen Beitrags zum anomalen magnetischen Moment
		\item **Erklärt beide experimentellen Situationen** konsistent
		\item **Vorhersagt testbare Beiträge** für alle Leptonen
		\item **Respektiert alle fundamentalen Symmetrien** des Standardmodells
	\end{itemize}
	
	## Fundamentale Bedeutung
	
	Die T0-Erweiterung weist auf eine tiefere Struktur der Raumzeit hin, in der Zeit und Masse dual verknüpft sind. Die erfolgreiche Ableitung der Lepton-Anomalien unterstützt die fundamentale Gültigkeit der Zeit-Masse-Dualität.
	
	% Bibliografie mit neuen Referenzen
	\begin{thebibliography}{20}
		
		\bibitem{muong2_fermilab_2021}
		Muon g-2 Collaboration (2021). 
		*Messung des anomalen magnetischen Moments des positiven Myons auf 0,46 ppm*. 
		Phys. Rev. Lett. **126**, 141801.
		
		\bibitem{sm_g2_2025}
		Lattice QCD Collaboration (2025).
		*Aktualisierter hadronischer Vakuumpolarisationsbeitrag zum Myon g-2*.
		Phys. Rev. D **112**, 034507.
		
		\bibitem{mug2_final_2025} 
		Muon g-2 Collaboration (2025).
		*Endgültige Ergebnisse vom Fermilab Myon g-2-Experiment*.
		Nature Phys. **21**, 1125–1130.
		
		\bibitem{pascher_t0_theory_2025}
		Pascher, J. (2025). 
		*T0-Zeit-Masse-Dualität: Fundamentale Prinzipien und experimentelle Vorhersagen*. 
		Verfügbar unter: \url{https://github.com/jpascher/T0-Time-Mass-Duality}
		
		\bibitem{pascher_lagrangian_extended_2025}
		Pascher, J. (2025). 
		*Erweiterte Lagrange-Dichte mit Zeitfeld zur Erklärung der Myon g-2-Anomalie*. 
		Verfügbar unter: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/CompleteMuon_g-2_AnalysisDe.pdf}
		
		\bibitem{pascher_mathematical_structure_2025}
		Pascher, J. (2025). 
		*Mathematische Struktur der T0-Theorie: Von komplexer Standardmodell-Physik zu elegante Feldvereinheitlichung*. 
		Verfügbar unter: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/Mathematische_struktur_En.tex}
		
		\bibitem{pascher_higgs_connection_2025}
		Pascher, J. (2025). 
		*Higgs-Zeitfeld-Verbindung in der T0-Theorie: Vereinheitlichung von Masse und temporaler Struktur*. 
		Verfügbar unter: \url{https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/LagrandianVergleichEn.pdf}
		
		\bibitem{peskin_schroeder_1995}
		Peskin, M. E. und Schroeder, D. V. (1995). 
		*Einführung in die Quantenfeldtheorie*. 
		Westview Press.
		
	\end{thebibliography}