# Phase 2 — Analyse des vulnérabilités

## Outils utilisés
- OpenVAS 22.x (Greenbone) — scan automatisé de tous les hôtes
- Scoring CVSS v3.1 (scores Base, Temporel, Environnemental)
- Élimination manuelle des faux positifs

## Résultats

Les résultats complets de cette phase sont documentés dans le 
rapport technique (Rapport_d_audit.pdf) — Chapitre IV :
- 5 vulnérabilités identifiées et validées manuellement
- 0 % de faux positifs sur les vulnérabilités DMZ
- Tableau de risques priorisé (matrice impact × probabilité)
- 5 fiches CVSS v3.1 détaillées (scores Base + Temporel + Environnemental)

## Vulnérabilités identifiées (synthèse)

| ID   | Titre                        | Score Base | Sévérité |
|------|------------------------------|------------|----------|
| V-01 | OS End-of-Life Debian 9      | 10.0       | Critique |
| V-02 | Cookie sans HttpOnly         | 5.0        | Moyen    |
| V-03 | Transmission en clair        | 4.8        | Moyen    |
| V-04 | TCP Timestamps DMZ           | 2.6        | Faible   |
| V-05 | ICMP Timestamp LAN           | 2.1        | Faible   |

## Note sur les artefacts

Les rapports XML/JSON bruts d'OpenVAS ont été générés dans un 
environnement de laboratoire isolé. Les résultats sont 
intégralement retranscrits dans le rapport technique.
