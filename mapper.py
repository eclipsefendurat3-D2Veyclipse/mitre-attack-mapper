import json
import sys

def load_attack_data(filepath):
    with open(filepath) as f:
        return json.load(f)

def search_technique(data, keyword):
    results = []
    for obj in data['objects']:
        if obj.get('type') == 'attack-pattern':
            name = obj.get('name', '')
            desc = obj.get('description', '')
            if keyword.lower() in name.lower() or keyword.lower() in desc.lower():
                results.append(obj)
    return results

def display_result(technique):
    print(f"\nTechnique:   {technique.get('name')}")
    ext = technique.get('external_references', [{}])[0]
    print(f"ID:          {ext.get('external_id', 'N/A')}")
    print(f"Reference:   {ext.get('url', 'N/A')}")
    desc = technique.get('description', '')
    print(f"Description: {desc[:300]}...")

if __name__ == '__main__':
    keyword = sys.argv[1] if len(sys.argv) > 1 else 'phishing'
    print(f"Loading dataset...")
    data = load_attack_data('data/attack.json')
    total = len([o for o in data['objects'] if o.get('type') == 'attack-pattern'])
    print(f"Dataset loaded. Attack patterns found: {total}")
    print(f"Searching for: {keyword}")
    results = search_technique(data, keyword)
    print(f"Found {len(results)} technique(s) matching: {keyword}")
    for r in results[:5]:
        display_result(r)
