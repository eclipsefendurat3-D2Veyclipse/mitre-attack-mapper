import json
import sys
import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

def load_attack_data(filepath):
    with open(filepath) as f:
        return json.load(f)

def get_technique_id(technique):
    refs = technique.get('external_references', [])
    for ref in refs:
        if ref.get('source_name') == 'mitre-attack':
            return ref.get('external_id', 'N/A'), ref.get('url', 'N/A')
    return 'N/A', 'N/A'

def get_tactic(technique):
    phases = technique.get('kill_chain_phases', [])
    if phases:
        return phases[0].get('phase_name', 'Unknown').replace('-', ' ').title()
    return 'Unknown'

def search_by_keyword(data, keyword):
    results = []
    for obj in data['objects']:
        if obj.get('type') == 'attack-pattern':
            name = obj.get('name', '')
            desc = obj.get('description', '')
            if keyword.lower() in name.lower() or keyword.lower() in desc.lower():
                results.append(obj)
    return results

def search_by_id(data, technique_id):
    for obj in data['objects']:
        if obj.get('type') == 'attack-pattern':
            tid, _ = get_technique_id(obj)
            if tid.upper() == technique_id.upper():
                return [obj]
    return []

def display_results(results, keyword):
    if not results:
        console.print(f"\n[red]No techniques found matching: {keyword}[/red]\n")
        return

    console.print(f"\n[bold green]Found {len(results)} technique(s) matching:[/bold green] [yellow]{keyword}[/yellow]\n")

    for i, technique in enumerate(results[:5], 1):
        tid, url = get_technique_id(technique)
        tactic = get_tactic(technique)
        name = technique.get('name', 'Unknown')
        desc = technique.get('description', '')[:250]

        panel_content = (
            f"[bold]ID:[/bold]          {tid}\n"
            f"[bold]Tactic:[/bold]      {tactic}\n"
            f"[bold]Reference:[/bold]   {url}\n"
            f"[bold]Description:[/bold] {desc}..."
        )

        console.print(Panel(
            panel_content,
            title=f"[bold cyan]{i}. {name}[/bold cyan]",
            border_style="blue",
            box=box.ROUNDED
        ))

def export_results(results, keyword, filepath):
    with open(filepath, 'w') as f:
        f.write(f"# MITRE ATT&CK Mapper — Search Results\n\n")
        f.write(f"**Search query:** {keyword}\n")
        f.write(f"**Techniques found:** {len(results)}\n\n")
        f.write("---\n\n")
        for i, technique in enumerate(results[:10], 1):
            tid, url = get_technique_id(technique)
            tactic = get_tactic(technique)
            name = technique.get('name', 'Unknown')
            desc = technique.get('description', '')[:400]
            f.write(f"## {i}. {name}\n\n")
            f.write(f"| Field | Value |\n")
            f.write(f"|---|---|\n")
            f.write(f"| **ID** | {tid} |\n")
            f.write(f"| **Tactic** | {tactic} |\n")
            f.write(f"| **Reference** | {url} |\n\n")
            f.write(f"**Description:** {desc}...\n\n")
            f.write("---\n\n")
    console.print(f"\n[green]Report saved to:[/green] {filepath}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='MITRE ATT&CK Mapper — map keywords to ATT&CK techniques'
    )
    parser.add_argument('keyword', help='Keyword or technique ID to search')
    parser.add_argument('--output', help='Save results to markdown file')
    parser.add_argument('--data', default='data/attack.json', help='Path to ATT&CK dataset')
    args = parser.parse_args()

    console.print("[bold blue]Loading ATT&CK dataset...[/bold blue]")
    data = load_attack_data(args.data)
    total = len([o for o in data['objects'] if o.get('type') == 'attack-pattern'])
    console.print(f"[green]Dataset loaded — {total} attack patterns[/green]")

    if args.keyword.upper().startswith('T') and args.keyword[1:].replace('.','').isdigit():
        results = search_by_id(data, args.keyword)
    else:
        results = search_by_keyword(data, args.keyword)

    display_results(results, args.keyword)

    if args.output:
        export_results(results, args.keyword, args.output)
