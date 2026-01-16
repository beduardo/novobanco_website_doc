#!/usr/bin/env python3
"""
Script para compilar o documento HLD final.
Remove frontmatter, referências a definições/decisões e substitui diagramas PlantUML por imagens.
"""

import os
import re
import hashlib
from pathlib import Path

SECTIONS_DIR = Path("sections")
DIAGRAMS_DIR = Path("diagrams")
OUTPUT_FILE = Path("HLD-HomeBanking-Web-FINAL.md")

# Ordem das seções
SECTION_ORDER = [
    "SEC-01-sumario-executivo.md",
    "SEC-02-contexto-negocio-requisitos.md",
    "SEC-03-visao-geral-solucao.md",
    "SEC-04-experiencia-utilizador-frontend.md",
    "SEC-05-arquitetura-backend-servicos.md",
    "SEC-06-arquitetura-dados.md",
    "SEC-07-autenticacao-autorizacao.md",
    "SEC-08-seguranca-conformidade.md",
    "SEC-09-integracao-interfaces-externas.md",
    "SEC-10-arquitetura-operacional.md",
    "SEC-11-observabilidade-operacoes.md",
    "SEC-12-desempenho-fiabilidade.md",
    "SEC-13-estrategia-testes.md",
    "SEC-14-plano-migracao-implementacao.md",
    "SEC-15-governacao-roadmap.md",
]

def generate_diagram_hash(content):
    """Generate a hash for diagram content to match with PNG files."""
    return hashlib.md5(content.encode()).hexdigest()[:8]

def remove_frontmatter(content):
    """Remove YAML frontmatter from markdown content."""
    if content.startswith("---"):
        end_idx = content.find("---", 3)
        if end_idx != -1:
            return content[end_idx + 3:].lstrip()
    return content

def remove_definition_references(content):
    """Remove definition and decision reference blocks."""
    # Remove blocks starting with > **Definições requeridas:**
    content = re.sub(
        r'>\s*\*\*Definições requeridas:\*\*.*?(?=\n\n|\n##|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove blocks starting with > **Required definitions:**
    content = re.sub(
        r'>\s*\*\*Required definitions:\*\*.*?(?=\n\n|\n##|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove blocks starting with > **Definição:**
    content = re.sub(
        r'>\s*\*\*Definição:\*\*.*?(?=\n\n|\n##|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Definições Utilizadas" sections
    content = re.sub(
        r'## Definições Utilizadas.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Decisões Referenciadas" sections
    content = re.sub(
        r'## Decisões Referenciadas.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Definicoes Utilizadas" (without accent)
    content = re.sub(
        r'## Definicoes Utilizadas.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Decisoes Referenciadas" (without accent)
    content = re.sub(
        r'## Decisoes Referenciadas.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Entregáveis" sections with checkboxes
    content = re.sub(
        r'## Entregáveis.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Entregaveis" sections (without accent)
    content = re.sub(
        r'## Entregaveis.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Perguntas para o Utilizador" sections
    content = re.sub(
        r'## Perguntas para o Utilizador.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "## Itens Pendentes" sections
    content = re.sub(
        r'## Itens Pendentes.*?(?=\n## |\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove inline references to definition files
    content = re.sub(
        r'\[DEF-\d+-[^\]]+\.md\]\([^\)]+\)',
        '',
        content
    )

    # Remove inline references to decision files
    content = re.sub(
        r'\[DEC-\d+-[^\]]+\.md\]\([^\)]+\)',
        '',
        content
    )

    return content

def find_diagram_png(puml_content, diagram_counter):
    """Find the corresponding PNG file for a PlantUML diagram."""
    # Generate hash based on content
    content_hash = generate_diagram_hash(puml_content)

    # Try to find matching file
    for png_file in sorted(DIAGRAMS_DIR.glob("*.png")):
        if content_hash in png_file.name:
            return png_file.name

    # Fallback: use diagram number
    png_name = f"diagram_{diagram_counter:02d}_*.png"
    matches = list(DIAGRAMS_DIR.glob(png_name))
    if matches:
        return matches[0].name

    return None

def replace_plantuml_with_images(content, section_name):
    """Replace PlantUML code blocks with image references."""
    diagram_counter = [0]  # Using list to allow modification in nested function

    def replacer(match):
        diagram_counter[0] += 1
        puml_content = match.group(1)

        # Extract title if present
        title_match = re.search(r'title\s+(.+)', puml_content)
        title = title_match.group(1) if title_match else f"Diagrama {diagram_counter[0]}"

        # For now, return a placeholder - we'll map these manually
        return f'\n![{title}](diagrams/DIAGRAM_PLACEHOLDER_{diagram_counter[0]}.png)\n\n*Figura: {title}*\n'

    # Match both @startuml/@enduml and @startgantt/@endgantt blocks
    content = re.sub(
        r'```plantuml\n(@start(?:uml|gantt).*?@end(?:uml|gantt))\n```',
        replacer,
        content,
        flags=re.DOTALL
    )

    return content

def compile_document():
    """Compile all sections into final document."""
    output_parts = []

    # Add document header
    output_parts.append("# HomeBanking Web - High Level Design (HLD)\n")
    output_parts.append("**Versão:** 1.0\n")
    output_parts.append("**Data:** Janeiro 2026\n")
    output_parts.append("**Cliente:** Novo Banco\n")
    output_parts.append("**Elaborado por:** NextReality\n")
    output_parts.append("\n---\n")

    # Add table of contents placeholder
    output_parts.append("\n## Índice\n")
    output_parts.append("_[Índice será gerado automaticamente no Word]_\n")
    output_parts.append("\n---\n")

    global_diagram_counter = 0

    for section_file in SECTION_ORDER:
        section_path = SECTIONS_DIR / section_file
        if not section_path.exists():
            print(f"Warning: Section {section_file} not found")
            continue

        print(f"Processing: {section_file}")

        with open(section_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove frontmatter
        content = remove_frontmatter(content)

        # Remove definition/decision references
        content = remove_definition_references(content)

        # Count diagrams in this section
        diagrams_in_section = len(re.findall(r'```plantuml', content))

        # Replace PlantUML with image placeholders
        def replacer(match):
            nonlocal global_diagram_counter
            global_diagram_counter += 1
            puml_content = match.group(1)

            # Extract title if present
            title_match = re.search(r'title\s+(.+)', puml_content)
            title = title_match.group(1) if title_match else f"Diagrama {global_diagram_counter}"
            title = title.strip()

            return f'\n![{title}](diagrams/diagram_{global_diagram_counter:02d}.png)\n\n*Figura: {title}*\n'

        content = re.sub(
            r'```plantuml\n(@start(?:uml|gantt).*?@end(?:uml|gantt))\n```',
            replacer,
            content,
            flags=re.DOTALL
        )

        # Clean up multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)

        # Add section separator
        output_parts.append(content)
        output_parts.append("\n\n---\n")

    # Add glossary from CONTEXT.md
    output_parts.append("\n## Glossário\n")
    output_parts.append("""
| Termo | Definição |
|-------|-----------|
| HLD | High-Level Design - Documento de arquitetura de alto nível |
| HomeBanking | Portal web de serviços bancários para clientes |
| Core Banking | Sistema central de operações bancárias |
| PSD2 | Payment Services Directive 2 - Diretiva europeia de serviços de pagamento |
| RGPD | Regulamento Geral de Proteção de Dados |
| PCI-DSS | Payment Card Industry Data Security Standard |
| SLA | Service Level Agreement - Acordo de nível de serviço |
| SLO | Service Level Objective - Objetivo de nível de serviço |
| SLI | Service Level Indicator - Indicador de nível de serviço |
| MFA | Multi-Factor Authentication - Autenticação multifator |
| SSO | Single Sign-On - Autenticação única |
| KYC | Know Your Customer - Processo de identificação de clientes |
| AML | Anti-Money Laundering - Prevenção de lavagem de dinheiro |
| API | Application Programming Interface |
| CMS | Content Management System - Sistema de gestão de conteúdo |
| CI/CD | Continuous Integration / Continuous Deployment |
| PWA | Progressive Web App |
| WCAG | Web Content Accessibility Guidelines |
| OWASP | Open Web Application Security Project |
| BFF | Backend for Frontend - Camada de backend específica para o frontend |
""")

    # Add document control
    output_parts.append("\n---\n")
    output_parts.append("\n## Controlo de Documento\n")
    output_parts.append("""
| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 0.1 | 2026-01-01 | NextReality | Versão inicial |
| 0.2 | 2026-01-13 | NextReality | Adição de escopo, premissas, restrições |
| 0.3 | 2026-01-13 | NextReality | Simplificação - conteúdos movidos para definições |
| 0.4 | 2026-01-15 | NextReality | Correção de acentuação em português europeu |
| 1.0 | 2026-01-15 | NextReality | Documento HLD compilado para entrega |
""")

    # Write output
    final_content = '\n'.join(output_parts)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"\nDocument compiled to: {OUTPUT_FILE}")
    print(f"Total diagrams processed: {global_diagram_counter}")

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    compile_document()
