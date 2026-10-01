@echo off
rem Im Repo-Wurzelverzeichnis ausfuehren. Loescht die ueberzaehligen Dateien.
if exist "2\python\Doc315_Skripte\euler_spirale_7limit.py" del "2\python\Doc315_Skripte\euler_spirale_7limit.py"
if exist "2\python\Doc315_Skripte\pruefrechnung_kfrak_form.py" del "2\python\Doc315_Skripte\pruefrechnung_kfrak_form.py"
if exist "2\python\Doc315_Skripte\pruefrechnung_p_identitaet.py" del "2\python\Doc315_Skripte\pruefrechnung_p_identitaet.py"
if exist "2\python\Doc315_Skripte\pruefrechnung_rest_0p1xi.py" del "2\python\Doc315_Skripte\pruefrechnung_rest_0p1xi.py"
if exist "2\python\bell_2025_sherbrooke_fit.py" del "2\python\bell_2025_sherbrooke_fit.py"
if exist "2\python\bell_73qubit_FIXED.py" del "2\python\bell_73qubit_FIXED.py"
if exist "2\python\bell_73qubit_fit.py" del "2\python\bell_73qubit_fit.py"
if exist "2\python\dune_t0_predictions.py" del "2\python\dune_t0_predictions.py"
if exist "2\python\fractal_vs_fit_compare.py" del "2\python\fractal_vs_fit_compare.py"
if exist "2\python\qft_neutrino_xi_fit.py" del "2\python\qft_neutrino_xi_fit.py"
if exist "2\python\xi_sensitivity_test.py" del "2\python\xi_sensitivity_test.py"
if exist "2\python\Doc315_Skripte\README_315.md" del "2\python\Doc315_Skripte\README_315.md"
if exist "2\python\Doc315_Skripte" rmdir "2\python\Doc315_Skripte"
echo Fertig.
