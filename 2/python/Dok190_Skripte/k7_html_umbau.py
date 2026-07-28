#!/usr/bin/env python3
"""K7: Umbau der vom Faktorisierungsbefund betroffenen HTML-Seiten.

Kein Hinweiskasten -- die Seiten selbst werden richtiggestellt: Rechenweg,
Beschriftung und Methodentext sagen, was der Code tut.

Zweiphasig: erst werden alle Zielstellen geprueft, geschrieben wird nur,
wenn jede genau so oft vorkommt wie erwartet.
"""
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'

E = []   # (Datei, alt, neu, Anzahl)


# ===================== 2/html/t0_shor_bigint.html =========================
# Die Resonanzbewertung waehlt nichts aus: exp(-(w-pi)^2/(4xi)) unterlaeuft
# fuer jedes angebotene xi und jedes r != 2 auf exakt 0. Die Funktion wird
# durch eine ehrliche Ordnungssuche ersetzt; xi bleibt als Diagnosewert
# sichtbar, damit man den Underflow selbst sehen kann.
E += [(
 '2/html/t0_shor_bigint.html',
 """function t0FindPeriod(a, N, maxR, xi) {
  const aN = BigInt(a), NN = BigInt(N);
  let best = null, bestRes = -1;
  let count = 0;

  for (let r = 1; r <= maxR; r++) {
    if (modPow(aN, BigInt(r), NN) === 1n) {
      // ξ-Resonanzbewertung
      const omega = 2 * Math.PI / r;
      const resonance = Math.exp(-((omega - Math.PI)**2) / (4 * Math.abs(xi)));
      if (resonance > bestRes) { bestRes = resonance; best = r; }
      count++;
      if (count >= 1000) break; // Nicht endlos sammeln
    }
  }
  return best ? { period: best, resonance: bestRes, candidates: count } : null;
}""",
 """function findOrder(a, N, maxR, xi) {
  // Multiplikative Ordnung: kleinstes r mit a^r = 1 mod N.
  const aN = BigInt(a), NN = BigInt(N);
  let order = null, count = 0;
  const res = [];   // nur zur Anzeige, geht in die Auswahl nicht ein

  for (let r = 1; r <= maxR; r++) {
    if (modPow(aN, BigInt(r), NN) === 1n) {
      if (order === null) order = r;
      const omega = 2 * Math.PI / r;
      res.push(Math.exp(-((omega - Math.PI)**2) / (4 * Math.abs(xi))));
      count++;
      if (count >= 1000) break;
    }
  }
  if (order === null) return null;
  const nonzero = res.filter(x => x > 0).length;
  return { period: order, candidates: count,
           resNonzero: nonzero, resTotal: res.length };
}""", 1),
(
 '2/html/t0_shor_bigint.html',
 """  // 5. T0-Periodensuche
  const periodRes = t0FindPeriod(a, Nnum, maxR, xi);""",
 """  // 5. Ordnungssuche
  const periodRes = findOrder(a, Nnum, maxR, xi);""", 1),
(
 '2/html/t0_shor_bigint.html',
 """      result.method = 't0_period'; result.factors = factors;
      result.period = periodRes.period; result.resonance = periodRes.resonance;""",
 """      result.method = 'order_finding'; result.factors = factors;
      result.period = periodRes.period;
      result.resNonzero = periodRes.resNonzero;
      result.resTotal = periodRes.resTotal;""", 1),
(
 '2/html/t0_shor_bigint.html',
 """  if (r.method === 't0_period')
    extra = ` | Basis=${r.base}, r=${r.period}, Res=${r.resonance.toExponential(2)}`;""",
 """  if (r.method === 'order_finding')
    extra = ` | Basis=${r.base}, Ordnung r=${r.period}` +
            ` | ξ-Resonanz ungleich 0 bei ${r.resNonzero} von ${r.resTotal} Kandidaten`;""", 1),
(
 '2/html/t0_shor_bigint.html',
 """  const cls = r.method === 't0_period' ? 'ok' :""",
 """  const cls = r.method === 'order_finding' ? 'ok' :""", 1),
(
 '2/html/t0_shor_bigint.html',
 """  <strong>Methodologie:</strong> Die T0-Periodensuche scannt r = 1 … max_r und bewertet
  jeden Treffer (a^r ≡ 1 mod N) mit der ξ-Resonanzformel
  ω = 2π/r, Resonanz = exp(−(ω−π)²/(4|ξ|)). Die Periode mit höchster Resonanz
  wird gewählt. Verglichen wird mit klassischem Trial Division bis √N.
  Alle Modular-Arithmetik exakt via BigInt.""",
 """  <strong>Methodologie:</strong> Gesucht wird die multiplikative Ordnung: das
  kleinste r mit a^r ≡ 1 (mod N). Das ist klassische Ordnungssuche, gefolgt von
  der Shor-Extraktion über ggT(a^{r/2} ± 1, N). Verglichen wird mit Trial
  Division bis √N. Alle Modular-Arithmetik exakt via BigInt.
  <br><br>
  <strong>Zur ξ-Resonanz:</strong> Die Formel ω = 2π/r,
  Resonanz = exp(−(ω−π)²/(4|ξ|)) wird weiterhin ausgewertet, geht aber in die
  Auswahl nicht ein — sie kann es nicht. Für r ≥ 2 ist |ω−π| = π(1−2/r) streng
  monoton wachsend in r, die Resonanz also streng monoton fallend; eine monotone
  Funktion verschiebt kein Maximum, unabhängig vom Wert von ξ. Für jedes hier
  anwählbare ξ unterläuft der Ausdruck zusätzlich auf exakt 0,0 für alle r ≠ 2.
  Die Anzeige „ξ-Resonanz ungleich 0 bei n von m Kandidaten“ macht das sichtbar.""", 1),
(
 '2/html/t0_shor_bigint.html',
 """      <option value="canonical">Kanonisch: 4/30000 ≈ 1.333×10⁻⁴</option>
      <option value="auto">Adaptiv (N-abhängig)</option>""",
 """      <option value="canonical">Kanonisch: 4/30000 ≈ 1.333×10⁻⁴ (Diagnose)</option>
      <option value="auto">Adaptiv, N-abhängig (Diagnose)</option>""", 1),
]

# ===================== 2/html/t0_xi_num_algebraisch.html ===================
# Das Kriterium |log10 xi_num - log10 xi^N| < 0.3 kann nie ansprechen:
# xi_num = lcm(p-1,q-1)/(pq) < 1/2 fuer jedes Semiprim, das naechste Fenster
# beginnt bei 10^-0.3 = 0.5012. Das Ergebnis wird entsprechend berichtet.
E += [(
 '2/html/t0_xi_num_algebraisch.html',
 """  let verdict, vtext;
  if(matches.length>=2){
    verdict='confirm';
    vtext=`\u2713 ${matches.length} \u03be_num-Cluster liegen nahe an FFGFT-Stufenwerten.
    Zahlenraum und physikalischer Raum teilen m\u00f6glicherweise analoge Resonanzstrukturen \u2014
    nicht identisch (verschiedene Geometrien), aber strukturell \u00e4hnlich.`;
  } else if(matches.length===1){
    verdict='neutral';
    vtext=`\u2248 1 Cluster nahe einer FFGFT-Stufe \u2014 Zufall nicht ausgeschlossen. Mehr Stichproben n\u00f6tig.`;
  } else {
    verdict='neutral';
    vtext=`\u2248 Keine klare Entsprechung zu FFGFT-Stufen gefunden. Die Strukturen sind verschieden \u2014 
    wie erwartet: Zahlenraum \u2260 physikalischer 3D-Raum.`;
  }""",
 """  // Reichweitenpruefung des Kriteriums, bevor das Ergebnis gedeutet wird.
  // xi_num = lcm(p-1,q-1)/(p*q) < 1/2 fuer JEDES Semiprim. Das naechst-
  // gelegene Fenster (N=0, xi^0=1) beginnt bei 10^-0.3 = 0.5012, das
  // naechste (N=1) endet bei 10^(log10(xi)+0.3). Liegt der erreichbare
  // Bereich vollstaendig dazwischen, kann das Kriterium nicht ansprechen.
  const winLo = Math.pow(10, -0.3);
  const winHi = Math.pow(10, Math.log10(ffgftLevels[1]) + 0.3);
  const erreichbar = { lo: Math.min(...xiAll), hi: Math.max(...xiAll) };
  const testTot = erreichbar.hi < winLo && erreichbar.lo > winHi;

  logLine('logC', `<br>Reichweite des Kriteriums:`);
  logLine('logC', `  \u03be_num liegt in [${erreichbar.lo.toExponential(3)}; ${erreichbar.hi.toExponential(3)}]`
    + ` \u2014 obere Schranke 1/2, da \u03be_num = lcm(p\u22121,q\u22121)/(pq)`);
  logLine('logC', `  N=0-Fenster beginnt bei ${winLo.toFixed(4)}, N=1-Fenster endet bei ${winHi.toExponential(3)}`);
  logLine('logC', testTot
    ? `  \u2192 der erreichbare Bereich liegt vollst\u00e4ndig in der L\u00fccke: das Kriterium kann nicht ansprechen`
    : `  \u2192 der erreichbare Bereich \u00fcberlappt mit mindestens einem Fenster: das Kriterium ist anwendbar`);

  let verdict, vtext;
  if(testTot){
    verdict='neutral';
    vtext=`Der Test ist in diesem Wertebereich nicht aussagekräftig.
    \u03be_num = lcm(p\u22121,q\u22121)/(pq) ist f\u00fcr jedes Semiprim kleiner als 1/2, w\u00e4hrend das
    n\u00e4chstgelegene Toleranzfenster erst bei 10^\u22120,3 = 0,5012 beginnt und das n\u00e4chste
    bei ${winHi.toExponential(3)} endet. Der gesamte erreichbare Bereich liegt in der L\u00fccke,
    ein Treffer ist also unabh\u00e4ngig von den Daten ausgeschlossen. Ein Negativergebnis
    ist deshalb keine Aussage \u00fcber die Stufenhypothese, sondern eine Eigenschaft des
    Testaufbaus. Eine belastbare Pr\u00fcfung br\u00e4uchte ein Kriterium, dessen Fenster den
    erreichbaren Bereich schneidet.`;
  } else if(matches.length>=2){
    verdict='confirm';
    vtext=`\u2713 ${matches.length} \u03be_num-Cluster liegen nahe an FFGFT-Stufenwerten.
    Zahlenraum und physikalischer Raum teilen m\u00f6glicherweise analoge Resonanzstrukturen \u2014
    nicht identisch (verschiedene Geometrien), aber strukturell \u00e4hnlich.`;
  } else if(matches.length===1){
    verdict='neutral';
    vtext=`\u2248 1 Cluster nahe einer FFGFT-Stufe \u2014 Zufall nicht ausgeschlossen. Mehr Stichproben n\u00f6tig.`;
  } else {
    verdict='neutral';
    vtext=`\u2248 Keine klare Entsprechung zu FFGFT-Stufen gefunden \u2014 bei anwendbarem Kriterium.`;
  }""", 1),
]

# ===================== 2/html/t0_Shore_simulator.html ======================
# Gleiche Entartung wie in t0_shor_bigint: baseResonance unterlaeuft fuer
# jedes r != 2 auf 0, der Zusatzfaktor (1+xi/r^2)^2.5 faellt ebenfalls
# monoton in r. Der reduce() ueber eine Nullliste liefert das erste Element,
# also die kleinste Periode. Ersetzt durch eine benannte Ordnungssuche;
# die Resonanzwerte bleiben als Diagnose erhalten.

E += [
 ('2/html/t0_Shore_simulator.html',
  """      pureT0PeriodFinding(a) {
        const maxPeriod = Math.min(this.rsaN, 75000);
        const periods = [];

        for (let r = 1; r < maxPeriod; r++) {
          if (this.modPow(a, r, this.rsaN) === 1) {
            const omega = 2 * Math.PI / r;
            const E1 = 1.0, E2 = 1.0, r12 = Math.max(1, r);
            const ECorr = this.xi * (E1 * E2) / (r12 * r12);
            const baseResonance = Math.exp(-((omega - Math.PI) * (omega - Math.PI)) / (4 * Math.abs(this.xi)));
            const totalResonance = baseResonance * Math.pow(1 + ECorr, 2.5);
            
            periods.push([r, totalResonance]);
            
            if (periods.length > 800) break;
          }
        }

        if (periods.length > 0) {
          const best = periods.reduce((max, current) => current[1] > max[1] ? current : max);
          return { period: best[0], resonance: best[1] };
        }
        return null;
      }""",
  """      findOrder(a) {
        // Multiplikative Ordnung: kleinstes r mit a^r = 1 mod N.
        const maxPeriod = Math.min(this.rsaN, 75000);
        let order = null;
        const res = [];   // nur Diagnose, geht in die Auswahl nicht ein

        for (let r = 1; r < maxPeriod; r++) {
          if (this.modPow(a, r, this.rsaN) === 1) {
            if (order === null) order = r;
            const omega = 2 * Math.PI / r;
            const ECorr = this.xi / (Math.max(1, r) * Math.max(1, r));
            const base = Math.exp(-((omega - Math.PI) * (omega - Math.PI)) / (4 * Math.abs(this.xi)));
            res.push(base * Math.pow(1 + ECorr, 2.5));
            if (res.length > 800) break;
          }
        }

        if (order === null) return null;
        return { period: order,
                 resNonzero: res.filter(x => x > 0).length,
                 resTotal: res.length };
      }""", 1),
 ('2/html/t0_Shore_simulator.html',
  """        // T0-Phase
        const periodResult = this.pureT0PeriodFinding(a);""",
  """        // Ordnungssuche
        const periodResult = this.findOrder(a);""", 1),
 ('2/html/t0_Shore_simulator.html',
  """            this.lastSuccessMethod = 'pure_t0_physics';
            return {
              success: true,
              method: 'pure_t0_physics',
              factors: factors,
              period: periodResult.period,
              resonance: periodResult.resonance,""",
  """            this.lastSuccessMethod = 'order_finding';
            return {
              success: true,
              method: 'order_finding',
              factors: factors,
              period: periodResult.period,
              resNonzero: periodResult.resNonzero,
              resTotal: periodResult.resTotal,""", 1),
 ('2/html/t0_Shore_simulator.html',
  """        if (result.method === 'pure_t0_physics') {
          appendResult(lang, `\\n\U0001f389 PURE T0-PHYSIK ERFOLG! / PURE T0-PHYSICS SUCCESS!`);
          appendResult(lang, `  Keine klassischen Fallback-Methoden verwendet`);
          appendResult(lang, `  No classical fallback methods used`);""",
  """        if (result.method === 'order_finding') {
          appendResult(lang, `\\nOrdnungssuche erfolgreich / order finding succeeded`);
          appendResult(lang, `  Kein klassischer Fallback verwendet; \u03be-Resonanz ungleich 0 bei ${result.resNonzero} von ${result.resTotal} Kandidaten`);
          appendResult(lang, `  No classical fallback used; \u03be resonance non-zero for ${result.resNonzero} of ${result.resTotal} candidates`);""", 1),
 ('2/html/t0_Shore_simulator.html',
  """        if (result.method === 'pure_t0_physics') {
          score += 25; // Bonus f\u00fcr echte T0-Physik""",
  """        if (result.method === 'order_finding') {
          score += 25; // Bonus fuer den Ordnungssuche-Weg (statt Fallback)""", 1),
 ('2/html/t0_Shore_simulator.html',
  "        if (method === 'pure_t0_physics') bonus += 15;",
  "        if (method === 'order_finding') bonus += 15;", 1),
]


# ===================== rsa/ Textseiten ====================================
# Korrigiert werden: die nicht gemessenen Erfolgsquoten, die Methoden-
# bezeichnungen (was faktorisiert, ist Ordnungssuche bzw. Probedivision)
# und der Import eines Moduls, das es nicht gibt. Die Spalte "Speicher"
# bleibt unangetastet -- sie ist zutreffend.

E += [
 ('rsa/libraries-benchmarks-de.html',
  '<span class="feature-icon">\u2713</span>83.8% Erfolgsquote bei Semiprimes',
  '<span class="feature-icon">\u2713</span>Erfolg abh\u00e4ngig davon, ob die Ordnung innerhalb der Suchgrenze liegt', 1),
 ('rsa/libraries-benchmarks-de.html',
  '<span class="feature-icon">\u2713</span>Periodenbewertung und Resonanzberechnung',
  '<span class="feature-icon">\u2713</span>Ordnungssuche: kleinstes r mit a^r \u2261 1 (mod N)', 1),
 ('rsa/libraries-benchmarks-de.html',
  '<td><strong>T0 Optimiert</strong></td>\n            <td>Periodenfindung</td>\n            <td class="good-performance">0.0025s</td>\n            <td class="good-performance">83.8%</td>',
  '<td><strong>Ordnungssuche</strong></td>\n            <td>kleinstes r mit a^r \u2261 1 (mod N)</td>\n            <td class="good-performance">0.0025s</td>\n            <td class="moderate-performance">abh\u00e4ngig von der Ordnung</td>', 1),
 ('rsa/libraries-benchmarks-de.html',
  '<td><strong>Harmonic Hierarchisch</strong></td>\n            <td>Verh\u00e4ltnissuche</td>\n            <td class="good-performance">0.8ms</td>\n            <td class="good-performance">97.1%</td>',
  '<td><strong>Harmonic-Bibliothek</strong></td>\n            <td>Probedivision, danach harmonische Benennung</td>\n            <td class="good-performance">0.8ms</td>\n            <td class="good-performance">100%</td>', 1),
 ('rsa/libraries-benchmarks-de.html',
  'from t0_period_finding import RelativeT0',
  'from t0_rational_optimized import T0RationalSimulatorOptimized', 2),
 ('rsa/libraries-benchmarks-de.html',
  't0 = RelativeT0()',
  't0 = T0RationalSimulatorOptimized(N)', 2),
 ('rsa/libraries-benchmarks-de.html',
  '# T0 Periodenfindung mit adaptiven \u03be-Strategien',
  '# Ordnungssuche (BSGS und lineare Suche, rationale Arithmetik)', 1),
 ('rsa/libraries_benchmarks_en.html',
  '<span class="feature-icon">\u2713</span>83.8% success rate on semiprimes',
  '<span class="feature-icon">\u2713</span>success depends on whether the order lies within the search bound', 1),
 ('rsa/libraries_benchmarks_en.html',
  '<td><strong>T0 Optimized</strong></td>',
  '<td><strong>Order finding</strong></td>', 1),
 ('rsa/libraries_benchmarks_en.html',
  '<td class="good-performance">83.8%</td>',
  '<td class="moderate-performance">depends on the order</td>', 1),
 ('rsa/libraries_benchmarks_en.html',
  '<td class="good-performance">97.1%</td>',
  '<td class="good-performance">100%</td>', 1),
 ('rsa/libraries_benchmarks_en.html',
  'from t0_period_finding import RelativeT0',
  'from t0_rational_optimized import T0RationalSimulatorOptimized', 2),
 ('rsa/libraries_benchmarks_en.html',
  't0 = RelativeT0()',
  't0 = T0RationalSimulatorOptimized(N)', 1),
 ('rsa/libraries_benchmarks_en.html',
  '# T0 period finding with adaptive \u03be-strategies',
  '# Order finding (BSGS and linear search, rational arithmetic)', 1),
 ('rsa/period-finding-de.html',
  '<strong>Erfolgsquote:</strong> 83.8% bei systematischen Tests',
  '<strong>Erfolg:</strong> abh\u00e4ngig davon, ob die Ordnung innerhalb der Suchgrenze liegt', 1),
 ('rsa/period-finding-en.html',
  '<strong>Success rate:</strong> 83.8% on systematic tests',
  '<strong>Success:</strong> depends on whether the order lies within the search bound', 1),
 ('rsa/index.html',
  'data-de="83.8% Erfolgsquote bei Semiprimes" data-en="83.8% success rate on semiprimes">83.8% Erfolgsquote bei Semiprimes',
  'data-de="Erfolg abh\u00e4ngig von der Ordnung" data-en="success depends on the order">Erfolg abh\u00e4ngig von der Ordnung', 1),
 ('rsa/index-0.html',
  'data-de="83.8% Erfolgsquote bei Semiprimes" data-en="83.8% success rate on semiprimes">83.8% Erfolgsquote bei Semiprimes',
  'data-de="Erfolg abh\u00e4ngig von der Ordnung" data-en="success depends on the order">Erfolg abh\u00e4ngig von der Ordnung', 1),
 ('rsa/harmonic-factorization-de.html',
  '<th>Methode</th>\n            <th>Erfolge</th>\n            <th>Rate</th>',
  '<th>Toleranz</th>\n            <th>Zuordnungen</th>\n            <th>Zuordnungsquote</th>', 1),
 ('rsa/harmonic-factorization-en.html',
  '<th>Method</th>\n            <th>Successes</th>\n            <th>Rate</th>',
  '<th>Tolerance</th>\n            <th>Classifications</th>\n            <th>Classification rate</th>', 1),
]


def lies(p):
    return open(p, encoding='utf-8', errors='replace').read()


def main():
    os.chdir(ROOT)
    puffer = {}
    for p, alt, neu, n in E:
        t = puffer.get(p) or lies(p)
        c = t.count(alt)
        if c != n:
            raise SystemExit(f'ABBRUCH, nichts geschrieben -- {p}: '
                             f'{alt[:60]!r} kommt {c}x vor, erwartet {n}x')
        puffer[p] = t.replace(alt, neu)
    for p, t in puffer.items():
        open(p, 'w', encoding='utf-8').write(t)
    print(f'{len(E)} Ersetzungen in {len(puffer)} Dateien')
    for p in sorted(puffer):
        print('   ' + p)


if __name__ == '__main__':
    main()
