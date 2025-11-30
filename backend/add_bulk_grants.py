"""
Bulk add grants to EquityBridge database
Target: 100+ grants for demo purposes
"""

import sqlite3
from datetime import datetime, timedelta
import random

def generate_bulk_grants():
    """Generate diverse grants across multiple categories"""
    
    grants = []
    
    # LA County-specific funders
    la_funders = [
        ("LA County Department of Public Health", "LA County", "health"),
        ("LA County Arts Commission", "LA County", "both"),
        ("LA County Chief Sustainability Office", "LA County", "environment"),
        ("City of Los Angeles Housing Department", "LA County", "both"),
        ("LA County Office of Education", "LA County", "health"),
        ("LA County Department of Mental Health", "LA County", "health"),
        ("Metro Los Angeles", "LA County", "environment"),
        ("LA County Department of Parks and Recreation", "LA County", "environment"),
    ]
    
    # California state funders
    ca_funders = [
        ("California Department of Public Health", "CA", "health"),
        ("CalEPA", "CA", "environment"),
        ("California Arts Council", "CA", "both"),
        ("California Strategic Growth Council", "CA", "environment"),
        ("California Department of Aging", "CA", "health"),
        ("California Office of Health Equity", "CA", "health"),
        ("California Natural Resources Agency", "CA", "environment"),
        ("California Department of Conservation", "CA", "environment"),
        ("California Department of Community Services", "CA", "both"),
        ("California Tax Credit Allocation Committee", "CA", "both"),
    ]
    
    # Federal funders
    federal_funders = [
        ("CDC", "federal", "health"),
        ("EPA", "federal", "environment"),
        ("HHS Administration for Community Living", "federal", "health"),
        ("USDA Rural Development", "federal", "both"),
        ("HUD", "federal", "both"),
        ("Department of Energy", "federal", "environment"),
        ("National Endowment for the Arts", "federal", "both"),
        ("AmeriCorps", "federal", "both"),
        ("HRSA", "federal", "health"),
        ("NIH", "federal", "health"),
        ("NOAA", "federal", "environment"),
        ("Department of Labor", "federal", "health"),
    ]
    
    # Foundation funders
    foundation_funders = [
        ("The California Endowment", "CA", "health"),
        ("California Wellness Foundation", "CA", "health"),
        ("California Community Foundation", "CA", "both"),
        ("Sierra Health Foundation", "CA", "health"),
        ("Blue Shield of California Foundation", "CA", "health"),
        ("Kaiser Permanente", "CA", "health"),
        ("The James Irvine Foundation", "CA", "both"),
        ("Weingart Foundation", "CA", "both"),
        ("Annenberg Foundation", "CA", "both"),
        ("California HealthCare Foundation", "CA", "health"),
        ("David and Lucile Packard Foundation", "CA", "environment"),
        ("Gordon and Betty Moore Foundation", "CA", "environment"),
        ("William and Flora Hewlett Foundation", "CA", "environment"),
        ("Resources Legacy Fund", "CA", "environment"),
        ("Energy Foundation", "CA", "environment"),
        ("Kresge Foundation", "federal", "both"),
        ("Robert Wood Johnson Foundation", "federal", "health"),
        ("W.K. Kellogg Foundation", "federal", "health"),
        ("Ford Foundation", "federal", "both"),
        ("MacArthur Foundation", "federal", "both"),
    ]
    
    # Grant program templates
    health_programs = [
        "Community Health Worker Initiative",
        "Health Equity Innovation Fund",
        "Primary Care Access Program",
        "Maternal and Child Health Grant",
        "Chronic Disease Prevention Initiative",
        "Mental Health Services Expansion",
        "Substance Abuse Prevention Program",
        "Health Literacy Initiative",
        "Community Clinic Support Grant",
        "Telehealth Expansion Program",
        "Senior Health Services Grant",
        "Youth Wellness Initiative",
        "Disability Services Enhancement",
        "Immigrant Health Access Program",
        "Rural Health Outreach Grant",
        "Health Workforce Development",
        "Community Health Assessment Grant",
        "Preventive Care Initiative",
        "Health Information Technology Grant",
        "Patient Navigation Program",
    ]
    
    environment_programs = [
        "Urban Greening Initiative",
        "Clean Air Communities Program",
        "Water Quality Improvement Grant",
        "Climate Resilience Fund",
        "Environmental Justice Initiative",
        "Renewable Energy Access Program",
        "Zero Waste Community Grant",
        "Urban Forestry Program",
        "Watershed Protection Initiative",
        "Clean Transportation Grant",
        "Sustainable Communities Fund",
        "Green Infrastructure Program",
        "Brownfield Remediation Grant",
        "Environmental Education Initiative",
        "Climate Action Planning Grant",
        "Energy Efficiency Program",
        "Community Solar Initiative",
        "Habitat Restoration Grant",
        "Stormwater Management Program",
        "Air Quality Monitoring Grant",
    ]
    
    both_programs = [
        "Community Development Block Grant",
        "Neighborhood Revitalization Fund",
        "Social Determinants of Health Initiative",
        "Place-Based Investment Program",
        "Community Resilience Fund",
        "Healthy Communities Initiative",
        "Equity Innovation Grant",
        "Community Capacity Building Program",
        "Cross-Sector Partnership Fund",
        "Systems Change Initiative",
    ]
    
    # Amount ranges by funder type
    amount_ranges = {
        "LA County": [(10000, 50000), (25000, 100000), (50000, 200000)],
        "CA": [(25000, 100000), (50000, 250000), (100000, 500000)],
        "federal": [(50000, 250000), (100000, 500000), (250000, 1000000)],
    }
    
    # Generate grants
    all_funders = la_funders + ca_funders + federal_funders + foundation_funders
    
    for funder_name, geo, focus in all_funders:
        # Determine which programs to use
        if focus == "health":
            programs = health_programs
        elif focus == "environment":
            programs = environment_programs
        else:
            programs = health_programs + environment_programs + both_programs
        
        # Generate 2-4 grants per funder
        num_grants = random.randint(2, 4)
        selected_programs = random.sample(programs, min(num_grants, len(programs)))
        
        for program in selected_programs:
            # Determine amounts
            if geo in amount_ranges:
                amount_min, amount_max = random.choice(amount_ranges[geo])
            else:
                amount_min, amount_max = random.choice([(25000, 150000), (50000, 300000)])
            
            # Generate deadline (60-180 days out)
            days_out = random.randint(60, 180)
            deadline = (datetime.now() + timedelta(days=days_out)).strftime('%Y-%m-%d')
            
            # Build grant
            grant = {
                'title': f"{funder_name} - {program}",
                'funder': funder_name,
                'description': f"Grant program supporting {program.lower()} initiatives in {'Los Angeles County' if geo == 'LA County' else 'California' if geo == 'CA' else 'communities nationwide'}.",
                'focus_area': focus if focus != "both" else random.choice(["health", "environment"]),
                'amount_min': amount_min,
                'amount_max': amount_max,
                'deadline': deadline,
                'geographic_eligibility': geo,
                'website_url': f"https://example.com/grants/{funder_name.lower().replace(' ', '-')}",
                'created_at': datetime.now().isoformat()
            }
            
            grants.append(grant)
    
    return grants

def save_grants(grants):
    """Save grants to database"""
    
    conn = sqlite3.connect('equitybridge.db')
    cursor = conn.cursor()
    
    # Check existing count
    cursor.execute('SELECT COUNT(*) FROM grants')
    existing = cursor.fetchone()[0]
    print(f"Existing grants: {existing}")
    
    saved = 0
    for grant in grants:
        try:
            cursor.execute('''
                INSERT INTO grants 
                (title, funder, description, focus_area, amount_min, amount_max,
                 deadline, geographic_eligibility, website_url, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                grant['title'],
                grant['funder'],
                grant['description'],
                grant['focus_area'],
                grant['amount_min'],
                grant['amount_max'],
                grant['deadline'],
                grant['geographic_eligibility'],
                grant['website_url'],
                grant['created_at']
            ))
            saved += 1
        except sqlite3.IntegrityError:
            # Skip duplicates
            continue
    
    conn.commit()
    
    # Final count
    cursor.execute('SELECT COUNT(*) FROM grants')
    total = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"Added: {saved} new grants")
    print(f"Total grants now: {total}")
    
    return saved

if __name__ == "__main__":
    print("=" * 50)
    print("BULK GRANT GENERATOR")
    print("=" * 50)
    
    grants = generate_bulk_grants()
    print(f"Generated {len(grants)} grants")
    
    saved = save_grants(grants)
    
    print("=" * 50)
    print("DONE - Now push to GitHub to deploy")
    print("git add . && git commit -m 'Add bulk grants' && git push")
    print("=" * 50)
