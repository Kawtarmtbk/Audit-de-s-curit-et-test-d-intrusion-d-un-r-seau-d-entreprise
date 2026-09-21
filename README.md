# 🛡️ Audit de Sécurité & Test d'Intrusion — Réseau d'Entreprise Simulé

**Méthodologie :** PTES (Penetration Testing Execution Standard)

## 📋 Résumé

Audit de sécurité complet d'un réseau d'entreprise hybride simulé en laboratoire : DMZ
conteneurisée (Docker/DVWA) + domaine Active Directory Windows Server 2019, segmentés
par un pare-feu pfSense. Le projet intègre une dimension **Performance Engineering** :
corrélation en temps réel entre outils offensifs et impact système via Prometheus/Grafana/cAdvisor

## 🎯 Objectifs

- Identifier les vulnérabilités d'une infrastructure hybride Docker + Active Directory
- Suivre la méthodologie PTES de bout en bout (7 phases)
- Quantifier l'empreinte système des outils offensifs (CPU/RAM/réseau) via monitoring temps réel
- Formuler des recommandations de remédiation priorisées

## 🏗️ Topologie du laboratoire

| Zone | Machine / Service | IP | Rôle |
|------|--------------------|-----|------|
| WAN | Kali Linux | 192.168.10.50 | Machine attaquante |
| DMZ | Hôte Docker | 192.168.50.128 | DVWA + monitoring |
| LAN | Contrôleur de domaine | 192.168.145.10 | Windows Server 2019 / AD / DNS |
| LAN | Client | 192.168.145.20 | Windows 10 (domaine mylab.local) |
| — | Pare-feu | 192.168.10.1 / .50.1 / .145.1 | pfSense (3 interfaces) |

## 🗂️ Structure du dépôt

## ✅ Phases réalisées (méthodologie PTES)

| Phase PTES | Description | Outils clés | Statut |
|---|---|---|---|
| 1. Pré-engagement | Architecture, segmentation réseau | pfSense, Docker, AD | ✅ |
| 2. Collecte d'informations | OSINT passif | theHarvester, Maltego CE | ✅ |
| 3. Modélisation des menaces | Surfaces d'attaque, vecteurs | Cartographie réseau | ✅ |
| 4. Analyse de vulnérabilités | Scan, CVSS | Nmap, GVM/OpenVAS | ✅ |
| 5. Exploitation | PoC contrôlés | Metasploit, Impacket, DVWA | ✅ |
| 6. Post-exploitation | Mouvement latéral, escalade AD | PtH, DCSync, Golden Ticket, BloodHound | ✅ |
| 7. Rapport | KPI, remédiation | Prometheus, Grafana, Git | ✅ |

## 📊 KPIs de Performance Engineering — Résultats clés

| KPI | Baseline | Max attaque | Delta |
|---|---|---|---|
| CPU Kali (attaquante) | 5.9% | 99.6% | +93.7 pts |
| CPU Windows 10 (cible) | 11.2% | 100% | +88.8 pts |
| Débit réseau Kali | 11.7 B/s | 600 kB/s | ×51 282 |
| Score CVSS moyen | — | 8.9/10 | — |
| Taux d'exploitation | — | 100% | 3/3 CVE |

## 🧰 Stack technique

- **Attaque :** Kali Linux, Nmap, Metasploit, Impacket, LinPEAS/WinPEAS, BloodHound, CrackMapExec
- **OSINT :** theHarvester 4.10.1, Maltego CE 4.11.3
- **Vulnérabilités :** Greenbone Vulnerability Management (GVM/OpenVAS)
- **Infrastructure :** pfSense 2.9-BETA, Docker/Docker Compose, Windows Server 2019 (AD DS), Windows 10
- **Monitoring :** Prometheus 2.x, Grafana 9.x, cAdvisor, node_exporter, windows_exporter

## ⚠️ Avertissement légal

Cet audit a été conduit exclusivement dans un environnement de laboratoire isolé,
dans le cadre d'un projet académique supervisé. Aucune technique décrite ici n'a été
appliquée à un système tiers ou de production. Toute reproduction de ces techniques
doit se faire uniquement avec une autorisation écrite explicite du propriétaire du système ciblé.

