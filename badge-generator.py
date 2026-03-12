#!/usr/bin/env python3
"""
AURORA-ZK Badge Generator
Generates badges for all project files with proper formatting
"""

class AuroraBadgeGenerator:
    def __init__(self):
        self.banner = """
┌──────────────────────────────────────────────┐
│          AURORA‑ZK CRYPTOGRAPHIC BANNER      │
└──────────────────────────────────────────────┘

[ HyperSpeed ] [ Quantum‑Shield ] [ zk‑Identity ]
[ Aurora Engine ] [ AI‑Circuitry ] [ Parallel Prover ]
[ Compliance ] [ Multi‑Language ] [ Cross‑Chain Warp ]

──────────────  Ecosystem Badges  ──────────────
[ Developer ] [ Contributor ] [ Governance ] [ Auditor ]

──────────────  Special Edition  ───────────────
[ 2035‑Ready ] [ Quantum‑Proof ] [ Aurora‑Speed ]
"""
    
    def core_badge(self, component, version, status):
        return f"""
┌──────────────────────────────────────────────┐
│     🔷 AURORA-ZK CORE · {component.upper():<20} │
└──────────────────────────────────────────────┘

[ HyperSpeed ] [ Quantum‑Shield ] [ zk‑Identity ]
[ Version: {version} ] [ Status: {status} ]

──────────  Security Classification  ───────────
[ {'CRITICAL' if status == 'production' else 'BETA'} ] [ {status.upper()} ] [ {'AUDITED' if status == 'production' else 'PENDING'} ]
"""
    
    def contract_badge(self, name, network, audited):
        return f"""
┌──────────────────────────────────────────────┐
│     📜 AURORA-ZK CONTRACT · {name.upper():<21} │
└──────────────────────────────────────────────┘

[ Cross‑Chain Warp ] [ Quantum‑Proof ] { '[ Audited ]' if audited else '[ Pending Audit ]' }
[ Solidity v0.8.20 ] [ Gas Optimized ]

──────────  Contract Verification  ─────────────
[ Verified: {network} ] [ Address: TBD ]
"""
    
    def template_badge(self, template_type, language):
        return f"""
┌──────────────────────────────────────────────┐
│     📋 AURORA-ZK TEMPLATE · {template_type.upper():<17} │
└──────────────────────────────────────────────┘

[ Developer ] [ Quick‑Start ] [ Best Practices ]
[ Language: {language} ] [ Framework: Aurora ]

──────────  Template Features  ─────────────────
[ Pre‑Audited ] [ Gas‑Efficient ] [ Modular ]
"""
    
    def docs_badge(self, title, audience, last_updated):
        return f"""
┌──────────────────────────────────────────────┐
│     📚 AURORA-ZK DOCS · {title.upper():<23} │
└──────────────────────────────────────────────┘

[ {audience} ] [ Governance ] [ Technical ]
[ Last Updated: {last_updated} ] [ Version: 1.0.0 ]

────────────  Document Status  ─────────────────
[ Complete ] [ Reviewed ] [ Approved ]
"""
    
    def legal_badge(self, doc_type, jurisdiction):
        return f"""
┌──────────────────────────────────────────────┐
│     ⚖️ AURORA-ZK LEGAL · {doc_type.upper():<22} │
└──────────────────────────────────────────────┘

[ Compliance ] [ Auditor ] [ Governance ]
[ Jurisdiction: {jurisdiction} ] [ Enforceable: Yes ]

──────────  Legal Status  ──────────────────────
[ Final Version ] [ Legally Binding ] [ Notarized ]
"""
    
    def github_app_badge(self, app_name, features):
        features_str = ' '.join([f'[{f}]' for f in features])
        return f"""
┌──────────────────────────────────────────────┐
│     🤖 AURORA-ZK APP · {app_name.upper():<23} │
└──────────────────────────────────────────────┘

{features_str}
[ Version: 2.0.0 ] [ Active ]

──────────  Integration Status  ────────────────
[ GitHub Actions ] [ Webhooks ] [ API v2 ]
"""
    
    def milestone_badge(self, name, progress, due_date):
        progress_bar = self._progress_bar(progress)
        return f"""
┌──────────────────────────────────────────────┐
│     🎯 MILESTONE · {name.upper():<28} │
├──────────────────────────────────────────────┤
│  Progress: {progress_bar} {progress}%          │
│  Due: {due_date}                                │
│  Status: {self._status_from_progress(progress)}                              │
└──────────────────────────────────────────────┘
"""
    
    def achievement_badge(self, level, title, requirement):
        icons = {'🥇': 'GOLD', '🥈': 'SILVER', '🥉': 'BRONZE', '🔰': 'FIRST PR', '🐛': 'BUG HUNTER', '📖': 'DOCS HERO'}
        return f"""
┌──────────────────────────────────────────────┐
│     {icons[level]} {title.upper():<31} │
├──────────────────────────────────────────────┤
│  Requirement: {requirement}                     │
│  Recipients: [List of names]                   │
└──────────────────────────────────────────────┘
"""
    
    def security_badge(self, badge_type, description):
        icons = {'🛡️': 'QUANTUM-PROOF', '🔒': 'AUDITED', '⚡': 'HYPERSPEED', '✅': 'VERIFIED'}
        return f"""
┌──────────────────────────────────────────────┐
│     {icons[badge_type]} {description.upper():<32} │
├──────────────────────────────────────────────┤
│  Validation: [PASSED]                          │
│  Certificate: [AURORA-{badge_type}-2024]        │
└──────────────────────────────────────────────┘
"""
    
    def _progress_bar(self, progress):
        filled = int(progress / 10)
        return '█' * filled + '░' * (10 - filled)
    
    def _status_from_progress(self, progress):
        if progress >= 100:
            return '✅ COMPLETE'
        elif progress >= 75:
            return '🟡 NEAR COMPLETE'
        elif progress >= 50:
            return '🟡 IN PROGRESS'
        elif progress >= 25:
            return '🟡 JUST STARTED'
        else:
            return '⚪ NOT STARTED'

# Generate all badges
generator = AuroraBadgeGenerator()

# Save badges to files
badges = {
    'main-banner.txt': generator.banner,
    'core-badge.txt': generator.core_badge('Aurora Engine', '1.0.0', 'production'),
    'contract-badge.txt': generator.contract_badge('Verifier', 'Mainnet', True),
    'template-badge.txt': generator.template_badge('Contract Template', 'Solidity'),
    'docs-badge.txt': generator.docs_badge('Architecture Guide', 'Developer', '2024-03-15'),
    'legal-badge.txt': generator.legal_badge('Contributor Agreement', 'Global'),
    'github-app-badge.txt': generator.github_app_badge('Audit-Bot', ['Security', 'Automation', 'CI/CD']),
    'milestone-badge.txt': generator.milestone_badge('Core Engine MVP', 100, '2024-04-15'),
    'achievement-badge.txt': generator.achievement_badge('🥇', 'Gold Contributor', '500+ commits'),
    'security-badge.txt': generator.security_badge('🛡️', 'Quantum-Proof')
}

for filename, content in badges.items():
    with open(f'badges/{filename}', 'w') as f:
        f.write(content)

print("✅ All badges generated in /badges directory")
