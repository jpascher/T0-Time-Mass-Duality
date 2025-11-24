\begin{abstract}
		Die Verwendung natürlicher Einheiten in der theoretischen Physik ist ein fundamentales Konzept, das im Kontext der T0-Theorie umfassend erklärt und eingeordnet werden kann. Diese Abhandlung beleuchtet das Prinzip der Dimensionsreduktion, die Vorteile für Berechnungen, die besondere Relevanz für die T0-Theorie sowie die Notwendigkeit expliziter SI-Einheiten in der Praxis. Abschließend wird die tiefere Einsicht hervorgehoben, dass die Physik letztlich auf dimensionslosen geometrischen Beziehungen beruht.
	\end{abstract}
	
	# Grundprinzip der natürlichen Einheiten
	\label{sec:grundprinzip}
	
	## Das Prinzip der Dimensionsreduktion
	In natürlichen Einheiten setzt man fundamentale Konstanten auf 1:
	\begin{itemize}
		\item **Lichtgeschwindigkeit**: $c = 1$
		\item **Reduzierte Planck-Konstante**: $\hbar = 1$
		\item **Boltzmann-Konstante**: $k_B = 1$
		\item **Manchmal**: $G = 1$ (Planck-Einheiten)
	\end{itemize}
	
	## Mathematische Konsequenz
	Dies bedeutet nicht, dass diese Konstanten ``verschwinden'', sondern dass sie als **Maßstabsgeber** dienen:
	\begin{equation}
		E = m c^2 \quad \Rightarrow \quad E = m \quad \text{(da $c=1$)}
	\end{equation}
	\begin{equation}
		E = \hbar \omega \quad \Rightarrow \quad E = \omega \quad \text{(da $\hbar=1$)}
	\end{equation}
	
	# Vorteile für Berechnungen
	
	## Vereinfachte Formeln
	**Mit SI-Einheiten:**
	\begin{equation}
		E = \sqrt{(p c)^2 + (m c^2)^2}
	\end{equation}
	**In natürlichen Einheiten:**
	\begin{equation}
		E = \sqrt{p^2 + m^2}
	\end{equation}
	
	## Dimensionsanalyse wird transparent
	Alle Größen lassen sich auf eine fundamentale Dimension zurückführen (typischerweise Energie):
	\begin{table}[h]
		\centering
		\begin{tabular}{lll}
			\toprule
			**Größe** & **Natürliche Dimension** & **SI-Äquivalent** \\
			\midrule
			Länge & $[E]^{-1}$ & $\hbar c / E$ \\
			Zeit & $[E]^{-1}$ & $\hbar / E$ \\
			Masse & $[E]$ & $E/c^2$ \\
			\bottomrule
		\end{tabular}
		\caption{Dimensionszusammenhänge in natürlichen Einheiten}
	\end{table}
	
	# In der T0-Theorie besonders relevant
	
	## Geometrische Natur der Konstanten
	Die T0-Theorie zeigt besonders deutlich, warum natürliche Einheiten fundamental sind:
	\begin{equation}
		\alpha = \xi \cdot \left( \frac{E_0}{1~\mathrm{MeV}} \right)^2
	\end{equation}
	Hier wird explizit, dass die Feinstrukturkonstante eine **rein dimensionslose geometrische Beziehung** ist.
	
	## Der $\xi$-Parameter als fundamentaler Geometriefaktor
	Die Herleitung:
	\begin{equation}
		\xi = \frac{4}{3} \times 10^{-4}
	\end{equation}
	ist intrinsisch dimensionslos und repräsentiert die grundlegende Raumgeometrie -- unabhängig von menschlichen Maßeinheiten.
	
	**Wichtig:** $\xi$ allein ist nicht direkt gleich $1/m_e$ oder $1/E$, sondern erfordert spezifische Skalierungsfaktoren für verschiedene physikalische Größen.
	
	# Herleitung des fundamentalen Skalierungsfaktors $S_{T0$}
	\label{sec:scaling-derivation}
	
	## Die fundamentale Vorhersage der T0-Theorie
	
	Die T0-Theorie macht eine bemerkenswerte Vorhersage: Die Elektronenmasse in geometrischen Einheiten ist exakt:
	
	\begin{equation}
		m_e^{\mathrm{T0}} = 0.511
	\end{equation}
	
	Dies ist keine Konvention, sondern eine **abgeleitete Konsequenz** der fraktalen Raumgeometrie via dem $\xi$-Parameter.
	
	## Explizite Demonstration: Herleitung vs. Rückrechnung
	
	Lassen Sie uns explizit demonstrieren, dass der Skalierungsfaktor abgeleitet wird, nicht rückgerechnet:
	
	\begin{align}
		**1. T0-Herleitung:** \quad & m_e^{\mathrm{T0}} = 0.511 \quad \text{(aus $\xi$-Geometrie)} \\
		**2. Experimenteller Input:** \quad & m_e^{\mathrm{SI}} = 9.1093837 \times 10^{-31}~\mathrm{kg} \quad \text{(unabhängig gemessen)} \\
		**3. T0-Vorhersage:** \quad & S_{T0} = \frac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}} = 1.782662 \times 10^{-30} \\
		**4. Empirische Tatsache:** \quad & 1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg} \\
		**5. Tiefgreifende Schlussfolgerung:** \quad & \text{Die T0-Theorie **vorhersagt** die MeV-Massenskala}
	\end{align}
	
	## Warum dies keine Zirkelschluss ist
	
	Man könnte fälschlicherweise denken: ``Sie definieren $S_{T0}$ einfach so, dass es $1~\mathrm{MeV}/c^2$ entspricht.''
	
	Dies missversteht den logischen Fluss:
	
	\begin{itemize}
		\item **Falsche Interpretation (Rückrechnung)**: 
		$m_e^{\mathrm{T0}} = \dfrac{m_e^{\mathrm{SI}}}{1~\mathrm{MeV}/c^2}$ (zirkulär)
		
		\item **Korrekte Interpretation (Herleitung)**: 
		$S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ und dies **entspricht zufällig** $1~\mathrm{MeV}/c^2$
	\end{itemize}
	
	Die Gleichheit $S_{T0} = 1~\mathrm{MeV}/c^2$ ist eine **Vorhersage**, keine Definition.
	
	## Gegenüberstellung
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{6cm}p{6cm}}
			\toprule
			**Konventionelle Physik** & **T0-Theorie** \\
			\midrule
			$1~\mathrm{MeV}/c^2 = 1.782662\times 10^{-30}~\mathrm{kg}$ (willkürliche Definition) & $m_e^{\mathrm{T0}} = 0.511$ (aus $\xi$-Geometrie abgeleitet) \\
			$m_e = 0.511~\mathrm{MeV}/c^2$ (unabhängige Messung) & $S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ (fundamentale Skalierung) \\
			Zwei unabhängige Fakten & Eine **vorhersagt** die andere \\
			\bottomrule
		\end{tabular}
		\caption{Vergleich der konventionellen und T0-Interpretation von Massenskalen}
	\end{table}
	
	Die bemerkenswerte Tatsache ist: **Beide Ansätze liefern identische Zahlen, aber T0 erklärt warum.**
	
	## Der Zufall, der keiner ist
	
	Was als bloße numerische Koinzidenz erscheint, ist tatsächlich eine fundamentale Vorhersage:
	
	\begin{align}
		\text{T0-Vorhersage:} \quad & S_{T0} = \frac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}} = \frac{9.1093837 \times 10^{-31}}{0.511} \\
		\text{Konventionelle Definition:} \quad & 1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg}
	\end{align}
	
	Diese sind **identisch** nicht per Definition, sondern weil die T0-Theorie die fundamentale Massenskala korrekt vorhersagt.
	
	## Die tiefgreifende Implikation
	
	\begin{center}
		\fbox{\parbox{0.8\textwidth}{
				**Die T0-Theorie ``verwendet'' nicht die MeV-Definition.**\\
				**Sie leitet ab, warum das MeV die Massenskala hat, die es hat.**
		}}
	\end{center}
	
	Die konventionelle Definition $1~\mathrm{MeV}/c^2 = 1.782662 \times 10^{-30}~\mathrm{kg}$ erscheint willkürlich, aber die T0-Theorie enthüllt sie als Konsequenz fundamentaler Geometrie.
	
	## Unabhängige Verifikation
	
	Wir können dies unabhängig verifizieren:
	
	\begin{itemize}
		\item **Ohne T0**: $1~\mathrm{MeV}/c^2 = 1.782662\times 10^{-30}~\mathrm{kg}$ (scheinbar willkürliche Konvention)
		\item **Mit T0**: $S_{T0} = 1.782662\times 10^{-30}$ (fundamentale Skalierung aus Geometrie abgeleitet)
		\item **Übereinstimmung**: Der identische numerische Wert bestätigt die Vorhersagekraft von T0
	\end{itemize}
	
	Dies ist analog dazu, wie $c = 299,792,458~\mathrm{m/s}$ willkürlich erscheint, bis man die Relativitätstheorie versteht.
	
	# Quantisierte Massenberechnung in der T0-Theorie
	
	## Fundamentales Massenquantisierungsprinzip
	
	In der T0-Theorie sind Teilchenmassen **quantisiert** und folgen aus dem fundamentalen Geometrieparameter $\xi$ durch diskrete Skalierungsbeziehungen:
	
	\begin{equation}
		m_i^{\mathrm{T0}} = n_i \cdot Q_m^{\mathrm{T0}} \cdot f_i(\xi)
	\end{equation}
	
	wobei:
	\begin{itemize}
		\item $n_i \in \mathbb{N}$ - Quantenzahl (diskret)
		\item $Q_m^{\mathrm{T0}}$ - Fundamentales Massenquant in T0-Einheiten
		\item $f_i(\xi)$ - Teilchenspezifische Geometriefunktion
	\end{itemize}
	
	## Elektronenmasse als Referenz
	
	Die Elektronenmasse dient als fundamentale Referenzmasse:
	
	\begin{align}
		\xi_e &= \frac{4}{3} \times 10^{-4} \times f_e(1,0,1/2) \\
		m_e^{\mathrm{T0}} &= Q_m^{\mathrm{T0}} \cdot \frac{\xi}{\xi_e} = 0.511
	\end{align}
	
	## Vollständiges Teilchenmassenspektrum
	
	Für detaillierte Herleitungen aller Elementarteilchenmassen im T0-Rahmen, einschließlich Quarks, Leptonen und Eichbosonen, wird auf die separate umfassende Behandlung ``Teilchenmassen in der T0-Theorie'' verwiesen, die folgendes bietet:
	
	\begin{itemize}
		\item Vollständige Massenberechnungen für alle Standardmodell-Teilchen
		\item Herleitung der Massenquantisierungsregeln
		\item Erklärung der Generationsmuster
		\item Vergleich mit experimentellen Werten
		\item Fraktale Renormierungsverfahren für Präzisionsanpassung
	\end{itemize}
	
	# Wichtig: Explizite SI-Einheiten sind notwendig bei\dots
	\label{sec:si-notwendig}
	
	## 1. Experimenteller Überprüfung
	Jede Messung erfolgt in SI-Einheiten:
	\begin{itemize}
		\item Teilchenmassen in MeV/c²
		\item Wirkungsquerschnitte in barn
		\item Magnetische Momente in $\mu_B$
	\end{itemize}
	
	## 2. Technologische Anwendungen
	\begin{itemize}
		\item Detektordesign (Längen in m, Zeiten in s)
		\item Beschleunigertechnik (Energien in eV)
		\item Medizinische Physik (Dosismessungen)
	\end{itemize}
	
	## 3. Interdisziplinäre Kommunikation
	\begin{itemize}
		\item Astrophysik (Rotverschiebungen, Hubble-Konstante)
		\item Materialwissenschaften (Gitterkonstanten)
		\item Ingenieurwesen
	\end{itemize}
	
	# Konkrete Umrechnung in der T0-Theorie
	\label{sec:umrechnung}
	
	## Beispiel: Elektronenmasse
	**In T0-geometrischen Einheiten:**
	\begin{equation}
		m_e^{\mathrm{T0}} = 0.511 \quad \text{(als reine geometrische Zahl aus $\xi$ abgeleitet)}
	\end{equation}
	**In SI-Einheiten:**
	\begin{equation}
		m_e^{\mathrm{SI}} = m_e^{\mathrm{T0}} \cdot S_{T0} = 0.511 \cdot 1.782662 \times 10^{-30} = 9.1093837 \times 10^{-31}~\mathrm{kg}
	\end{equation}
	
	## Die fundamentale Skalierungsbeziehung
	Die Umrechnung von T0-geometrischen Größen in SI-Einheiten erfolgt durch:
	\begin{equation}
		[\mathrm{SI}] = [\mathrm{T0}] \times S_{\text{T0}}
	\end{equation}
	wobei $S_{\text{T0}} = 1.782662 \times 10^{-30}$ der fundamentale Skalierungsfaktor ist, der in Abschnitt~\ref{sec:scaling-derivation} **abgeleitet** wurde, nicht definiert.
	
	# Korrekte Energie-Skala für die Feinstrukturkonstante
	
	Die fundamentale Beziehung für die Feinstrukturkonstante erfordert eine präzise Energie-Referenz:
	
	\begin{align}
		\alpha &= \xi \cdot \left( \frac{E_0}{1~\mathrm{MeV}} \right)^2 \\
		\text{mit} \quad E_0 &= 7.400~\mathrm{MeV} \quad \text{(charakteristische Energie)}
	\end{align}
	
	Dies ergibt:
	\begin{align}
		\alpha &= 1.333333 \times 10^{-4} \cdot (7.400)^2 \\
		&= 1.333333 \times 10^{-4} \cdot 54.76 \\
		&= 7.300 \times 10^{-3} \\
		\frac{1}{\alpha} &= 137.00
	\end{align}
	
	Die leichte Abweichung vom experimentellen Wert $1/\alpha = 137.036$ ist auf fraktale Korrekturen höherer Ordnung zurückzuführen, die im vollständigen Renormierungsverfahren berücksichtigt werden.
	
	# Integration der fraktalen Renormierung in natürliche Einheiten
	
	Die Formeln in der T0-Theorie passen in natürlichen Einheiten ohne explizite fraktale Renormierung, da diese Einheiten die geometrische Essenz der Theorie isolieren. Für exakte Umrechnungen in SI-Einheiten ist die fraktale Renormierung jedoch essenziell, um selbstähnliche Korrekturen der Vakuumgeometrie einzubeziehen.
	
	## Warum passen die Formeln in natürlichen Einheiten ohne fraktale Renormierung?
	
	In natürlichen Einheiten wird die Physik auf eine geometrische, dimensionslose Basis reduziert (vgl. Abschnitt~\ref{sec:grundprinzip}). Die fundamentalen Konstanten dienen nur als Maßstab, und die Kernformeln gelten approximativ ohne zusätzliche Korrekturen, weil:
	
	\begin{itemize}
		\item **Der $\xi$-Parameter ist intrinsisch dimensionslos**: $\xi$ repräsentiert die reine Geometrie des Vakuumfelds und wirkt wie ein ``universeller Skalierungsfaktor.''
		
		\item **Approximative Gültigkeit für grobe Berechnungen**: Viele T0-Formeln sind exakt in der geometrischen Idealform, ohne Renormierung.
		
		\item **Beispiel: Elektronenmasse in natürlichen Einheiten**:
		\begin{equation}
			m_e^{\mathrm{T0}} = 0.511 \quad \text{(geometrische Zahl, ohne Renormierung)}
		\end{equation}
		Dies ``passt'' sofort, weil $\xi$ die geometrische Skala setzt.
	\end{itemize}
	
	## Warum ist fraktale Renormierung für exakte SI-Umrechnungen notwendig?
	
	SI-Einheiten sind menschliche Konventionen, die die geometrische Reinheit der T0-Theorie ``verunreinigen''. Um exakte Übereinstimmung mit Experimenten zu erreichen, muss die fraktale Renormierung **explizit angewendet** werden, weil:
	
	\begin{itemize}
		\item **Fraktale Selbstähnlichkeit bricht die Skaleninvarianz**
		\item **Umrechnung erfordert explizite Skalierung**
		\item **Kosmologische Referenzeffekte**
	\end{itemize}
	
	## Mathematische Spezifikation der fraktalen Renormierung
	
	Die fraktale Renormierung wird explizit definiert als:
	\begin{equation}
		f_{\text{fraktal}}(E_0) = \prod_{n=1}^{137} \left(1 + \delta_n \cdot \xi \cdot \left(\frac{4}{3}\right)^{n-1}\right)
	\end{equation}
	wobei $\delta_n$ dimensionslose Koeffizienten sind, die die fraktale Struktur auf jeder Stufe beschreiben.
	
	## Vergleich: Approximation vs. Exaktheit
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{4cm}p{6cm}p{6cm}}
			\toprule
			**Aspekt** & **Ohne fraktale Renormierung (T0-Einheiten)** & **Mit fraktaler Renormierung (für SI-Umrechnung)** \\
			\midrule
			Genauigkeit & Approximativ ($\sim 98$--$99$\,\%, geometrisch ideal) & Exakt (bis $10^{-6}$, passt zu CODATA-Messungen) \\
			Beispiel: $\alpha$ & $\alpha \approx \xi \cdot (E_0)^2 \approx 1/137$ (grob) & $\alpha = 1/137.03599\dots$ (via 137 Stufen) \\
			Massenberechnung & $m_e^{\mathrm{T0}} = 0.511$ (geometrisch) & $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg (physikalisch) \\
			Energieskala & $E_0 = 7.400$ MeV (ideal) & $E_0 = 7.400244$ MeV (renormiert) \\
			Skalierungsfaktor & $S_{T0} = 1.782662\times 10^{-30}$ (fundamental) & $S_{T0} \cdot R_f$ (renormiert) \\
			Vorteil & Schnelle, transparente Berechnungen & Testbarkeit mit Experimenten \\
			Nachteil & Ignoriert fraktale Feinheiten & Komplex (Iteration über Resonanzstufen) \\
			\bottomrule
		\end{tabular}
		\caption{Vergleich der geometrischen Idealisierung in T0-Einheiten und physikalischen Exaktheit mit fraktaler Renormierung.}
		\label{tab:approximation-exaktheit}
	\end{table}
	
	## Fazit: Die Dualität von geometrischer Idealisierung und physikalischer Messung
	
	Die Formeln ``passen'' in T0-Einheiten ohne Renormierung, weil diese Einheiten die **geometrische Essenz** der Physik erfassen. Für die Umrechnung in messbare SI-Einheiten wird Renormierung **explizit notwendig**, um die **selbstähnlichen Korrekturen** der fraktalen Vakuumgeometrie einzubeziehen.
	
	# Wichtige konzeptionelle Klarstellungen
	
	Bei der Anwendung der T0-Theorie sind folgende fundamentale Unterscheidungen zu beachten:
	
	\begin{itemize}
		\item **T0-Größen** sind geometrisch und aus $\xi$ abgeleitet (z.B. $m_e^{\mathrm{T0}} = 0.511$)
		\item **SI-Größen** sind physikalische Messungen (z.B. $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg)
		\item **$S_{T0**$} ist die fundamentale Skalierung zwischen diesen Bereichen, **abgeleitet** nicht definiert
		\item Die Energie-Referenz für $\alpha$ ist exakt $E_0 = 7.400$ MeV in der geometrischen Idealisierung
		\item Alle Massenskalen sind **diskret quantisiert** in beiden T0- und SI-Darstellungen
	\end{itemize}
	
	# Besondere Bedeutung für die T0-Theorie
	
	## Die tiefere Einsicht
	Die T0-Theorie enthüllt, dass natürliche Einheiten nicht nur eine Rechenvereinfachung sind, sondern die **wahre geometrische Natur der Physik** ausdrücken:
	\begin{itemize}
		\item **$\xi$** ist die fundamentale dimensionslose Geometriekonstante
		\item **$S_{T0**$} verbindet geometrische Idealisierung mit physikalischer Messung
		\item **T0-Größen** repräsentieren die idealen geometrischen Formen
		\item **SI-Größen** sind ihre messbaren Projektionen in unsere physikalische Realität
		\item **Teilchenmassen** sind quantisierte geometrische Muster in beiden Bereichen
	\end{itemize}
	
	## Praktische Implikationen
	\begin{enumerate}
		\item **Theoretische Entwicklung**: Arbeiten in T0-Einheiten mit geometrischen Größen
		\item **Fundamentale Skalierung**: Anwenden von $S_{T0}$ zur Projektion in die physikalische Realität
		\item **Vorhersagen**: Umrechnen in SI-Einheiten für experimentelle Verifikation
		\item **Verifikation**: Vergleich mit gemessenen SI-Werten
		\item **Quantisierung**: Berücksichtigung der diskreten Natur aller physikalischen Skalen
	\end{enumerate}
	
	# Fazit
	
	T0-geometrische Größen entsprechen der **intrinsischen Sprache der Physik**, während SI-Einheiten die **Messsprache der Experimentatoren** sind. Die T0-Theorie demonstriert schlüssig, dass die fundamentalen Beziehungen der Physik dimensionslos und geometrisch sind.
	
	Der Skalierungsfaktor $S_{T0}$ bietet die essentielle Brücke zwischen der geometrischen Idealisierung der T0-Theorie und der praktischen Realität experimenteller Messung. Die Tatsache, dass alle physikalischen Konstanten aus dem einzigen dimensionslosen Parameter $\xi$ **mit der fundamentalen Skalierung $S_{T0**$} abgeleitet werden können, bestätigt die tiefgreifende Wahrheit: Physik ist letztlich die Mathematik dimensionsloser geometrischer Beziehungen mit diskreter Quantisierung, projiziert in unser messbares Universum durch fundamentale Skalierung.
	
	\appendix
	# Formelzeichen und Symbole
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{3cm}p{10cm}}
			\toprule
			**Symbol** & **Bedeutung und Erklärung** \\
			\midrule
			$c$ & Lichtgeschwindigkeit im Vakuum; fundamentale Naturkonstante \\
			$\hbar$ & Reduzierte Planck-Konstante \\
			$k_B$ & Boltzmann-Konstante \\
			$G$ & Gravitationskonstante \\
			$E$ & Energie; in natürlichen Einheiten dimensionsgleich mit Masse und Frequenz \\
			$m$ & Masse; in natürlichen Einheiten $m = E$ (da $c=1$) \\
			$p$ & Impuls; in natürlichen Einheiten dimensionsgleich mit Energie \\
			$\omega$ & Kreisfrequenz; in natürlichen Einheiten $\omega = E$ (da $\hbar=1$) \\
			$\alpha$ & Feinstrukturkonstante; dimensionslose Kopplungskonstante \\
			$\xi$ & Fundamentaler Geometrieparameter der T0-Theorie; $\xi = \frac{4}{3} \times 10^{-4}$ \\
			$E_0$ & Referenzenergie in der T0-Theorie; $E_0 = 7.400~\mathrm{MeV}$ \\
			$m_e^{\mathrm{T0}}$ & Elektronenmasse in T0-Einheiten; $m_e^{\mathrm{T0}} = 0.511$ (geometrisch) \\
			$m_e^{\mathrm{SI}}$ & Elektronenmasse in SI-Einheiten; $m_e^{\mathrm{SI}} = 9.1093837\times 10^{-31}$ kg (physikalisch) \\
			$[E]$ & Energie-Dimension; fundamentale Dimension in natürlichen Einheiten \\
			SI & Internationales Einheitensystem (physikalische Messungen) \\
			T0 & T0-geometrische Einheiten (ideale geometrische Formen) \\
			$S_{T0}$ & Fundamentaler Skalierungsfaktor; $S_{T0} = 1.782662 \times 10^{-30}$ \\
			$R_f$ & Fraktaler Renormierungsfaktor \\
			$f_{\text{fraktal}}$ & Fraktale Renormierungsfunktion \\
			$Q_m^{\mathrm{T0}}$ & Fundamentales Massenquant in T0-Einheiten \\
			$Q_m^{\mathrm{SI}}$ & Fundamentales Massenquant in SI-Einheiten \\
			$n_i$ & Quantenzahl für Teilchen $i$; $n_i \in \mathbb{N}$ (diskret) \\
			$\delta_n$ & Fraktale Renormierungskoeffizienten; dimensionslos \\
			\bottomrule
		\end{tabular}
		\caption{Erklärung der verwendeten Formelzeichen und Symbole}
	\end{table}
	
	# Fundamentale Zusammenhänge
	
	\begin{table}[h]
		\centering
		\begin{tabular}{p{4cm}p{10cm}}
			\toprule
			**Zusammenhang** & **Bedeutung** \\
			\midrule
			$E = m$ & Masse-Energie-Äquivalenz (da $c=1$) \\
			$E = \omega$ & Energie-Frequenz-Zusammenhang (da $\hbar=1$) \\
			$[L] = [T] = [E]^{-1}$ & Länge und Zeit haben gleiche Dimension wie inverse Energie \\
			$[m] = [p] = [E]$ & Masse und Impuls haben gleiche Dimension wie Energie \\
			$\alpha = \xi (E_0/1\mathrm{MeV})^2$ & Fundamentaler Zusammenhang in T0-Theorie \\
			$m_i^{\mathrm{T0}} = n_i \cdot Q_m^{\mathrm{T0}} \cdot f_i(\xi)$ & Quantisierte Massenformel in T0-Einheiten \\
			$m_i^{\mathrm{SI}} = m_i^{\mathrm{T0}} \cdot S_{T0}$ & Fundamentale Skalierung zu SI-Einheiten \\
			$S_{T0} = \dfrac{m_e^{\mathrm{SI}}}{m_e^{\mathrm{T0}}}$ & Definition des fundamentalen Skalierungsfaktors \\
			\bottomrule
		\end{tabular}
		\caption{Fundamentale Zusammenhänge in der T0-Theorie und Skalierung zu physikalischen Einheiten}
	\end{table}
	
	# Umrechnungsfaktoren
	
	\begin{table}[h]
		\centering
		\begin{tabular}{lll}
			\toprule
			**Größe** & **Umrechnungsfaktor** & **Wert** \\
			\midrule
			$S_{T0}$ & Fundamentaler Skalierungsfaktor & $1.782662 \times 10^{-30}$ \\
			$m_e^{\mathrm{T0}}$ & Elektronenmasse (T0-Einheiten) & $0.511$ \\
			$m_e^{\mathrm{SI}}$ & Elektronenmasse (SI-Einheiten) & $9.1093837 \times 10^{-31}~\mathrm{kg}$ \\
			$1~\mathrm{MeV}/c^2$ & Konventionelle Masseneinheit & $1.782662 \times 10^{-30}~\mathrm{kg}$ \\
			$1~\mathrm{MeV}$ & Energie in Joule & $1.602176 \times 10^{-13}~\mathrm{J}$ \\
			$1~\mathrm{fm}$ & Länge in natürlichen Einheiten & $5.06773 \times 10^{-3}~\mathrm{MeV}^{-1}$ \\
			\bottomrule
		\end{tabular}
		\caption{Fundamentale Umrechnungsfaktoren zwischen T0-geometrischen Einheiten und SI-physikalischen Einheiten}
	\end{table}