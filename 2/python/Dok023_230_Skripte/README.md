# Dok023_230_Skripte — FFGFT xi-scale Bell/CHSH differential

bell_xi_differential.py: the FFGFT-predicted xi-scale deviation in the two-photon
Bell correlation (source: Doc. 023; mature geometric reading: Doc. 230).
Shows that the UNIFORM (1-xi) damping is degenerate with finite source visibility
(NOT observable), and that the observable signature is the ANGLE-DEPENDENCE of the
visibility deficit: measure the correlation visibility at the QM extrema theta~pi and
theta~0 and difference the deficits (QM stationary there -> angle drift suppressed;
constant source visibility cancels). FFGFT signal = xi/D_f .. xi ~ 4e-5 .. 1.3e-4;
required statistics N ~ 1/signal^2 ~ 6e7..6e8 coincidence pairs (photonic-reachable).
numpy only. Run: python3 bell_xi_differential.py
