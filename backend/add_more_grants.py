"""
Add more diverse grants to database
Including disability services, social services, community development, etc.
"""

import sqlite3
from datetime import datetime, timedelta

def add_diverse_grants():
    """Add grants covering disability services, social services, and more categories"""
    
    conn = sqlite3.connect('equitybridge.db')
    cursor = conn.cursor()
    
    # Additional grants covering diverse categories
    new_grants = [
        # Disability Services Grants
        (
            "Administration for Community Living - Disability Services",
            "U.S. Department of Health and Human Services",
            "Support services for individuals with disabilities, including independent living, employment, and community integration",
            "health",  # Disability services often align with health
            50000,
            500000,
            "2026-03-01",
            "federal",
            "https://acl.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "California Department of Developmental Services - Community Services",
            "California Department of Developmental Services",
            "Grants for organizations providing services to individuals with developmental disabilities",
            "health",
            25000,
            200000,
            "2026-04-15",
            "CA",
            "https://www.dds.ca.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "Disability Rights Fund - Community Advocacy",
            "Disability Rights Fund",
            "Support disability rights organizations and advocacy initiatives",
            "health",
            10000,
            75000,
            "2026-02-28",
            "federal",
            "https://disabilityrightsfund.org/grants",
            datetime.now().isoformat()
        ),
        
        # Social Services & Community Development
        (
            "HHS Community Services Block Grant",
            "U.S. Department of Health and Human Services",
            "Support community action agencies and organizations addressing poverty and community needs",
            "health",
            100000,
            1000000,
            "2026-05-01",
            "federal",
            "https://www.acf.hhs.gov/ocs/programs/community-services-block-grant-csbg",
            datetime.now().isoformat()
        ),
        (
            "California Department of Social Services - Community Programs",
            "California Department of Social Services",
            "Grants for community-based organizations providing social services",
            "health",
            50000,
            300000,
            "2026-06-01",
            "CA",
            "https://www.cdss.ca.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "United Way Community Impact Grants",
            "United Way",
            "Support organizations addressing community needs including health, education, and economic stability",
            "both",
            25000,
            150000,
            "2026-03-15",
            "CA",
            "https://www.unitedway.org/grants",
            datetime.now().isoformat()
        ),
        
        # Housing & Economic Development
        (
            "HUD Community Development Block Grant",
            "U.S. Department of Housing and Urban Development",
            "Support community development activities including affordable housing, economic development, and public services",
            "both",
            100000,
            2000000,
            "2026-04-30",
            "federal",
            "https://www.hud.gov/program_offices/comm_planning/communitydevelopment",
            datetime.now().isoformat()
        ),
        (
            "California Housing and Community Development - Community Grants",
            "California Department of Housing and Community Development",
            "Support affordable housing and community development initiatives",
            "both",
            75000,
            500000,
            "2026-05-15",
            "CA",
            "https://www.hcd.ca.gov/grants",
            datetime.now().isoformat()
        ),
        
        # Education & Workforce
        (
            "Department of Education - Community Learning Centers",
            "U.S. Department of Education",
            "Support community learning centers providing educational and enrichment activities",
            "health",
            50000,
            250000,
            "2026-03-30",
            "federal",
            "https://www.ed.gov/21stcclc",
            datetime.now().isoformat()
        ),
        (
            "California Workforce Development Board - Community Grants",
            "California Workforce Development Board",
            "Support workforce development and job training programs in underserved communities",
            "health",
            75000,
            400000,
            "2026-04-01",
            "CA",
            "https://cwdb.ca.gov/grants",
            datetime.now().isoformat()
        ),
        
        # Food Security & Nutrition
        (
            "USDA Community Food Projects",
            "U.S. Department of Agriculture",
            "Support community food projects addressing food security and nutrition in underserved areas",
            "health",
            25000,
            300000,
            "2026-05-01",
            "federal",
            "https://www.nifa.usda.gov/grants/programs/community-food-projects-competitive-grant-program",
            datetime.now().isoformat()
        ),
        (
            "California Department of Food and Agriculture - Community Food Grants",
            "California Department of Food and Agriculture",
            "Support community food security and nutrition programs",
            "health",
            30000,
            200000,
            "2026-06-15",
            "CA",
            "https://www.cdfa.ca.gov/grants",
            datetime.now().isoformat()
        ),
        
        # Mental Health & Wellness
        (
            "SAMHSA Community Mental Health Services Block Grant",
            "Substance Abuse and Mental Health Services Administration",
            "Support community mental health services and substance abuse treatment programs",
            "health",
            100000,
            800000,
            "2026-03-01",
            "federal",
            "https://www.samhsa.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "California Mental Health Services Act - Community Programs",
            "California Department of Health Care Services",
            "Support community mental health programs and services",
            "health",
            50000,
            400000,
            "2026-04-30",
            "CA",
            "https://www.dhcs.ca.gov/mhsa",
            datetime.now().isoformat()
        ),
        
        # Environmental Health (broader category)
        (
            "NIH Environmental Health Disparities Research",
            "National Institutes of Health",
            "Support research and programs addressing environmental health disparities in underserved communities",
            "both",
            100000,
            500000,
            "2026-05-15",
            "federal",
            "https://www.nih.gov/grants",
            datetime.now().isoformat()
        ),
        (
            "California Air Resources Board - Community Air Protection",
            "California Air Resources Board",
            "Support community programs addressing air quality and environmental health",
            "both",
            50000,
            300000,
            "2026-06-01",
            "CA",
            "https://ww2.arb.ca.gov/grants",
            datetime.now().isoformat()
        ),
        
        # General Community Support
        (
            "California Community Foundation - General Community Grants",
            "California Community Foundation",
            "Support community organizations addressing a wide range of community needs",
            "both",
            10000,
            100000,
            "2026-03-15",
            "CA",
            "https://www.calfund.org/grants",
            datetime.now().isoformat()
        ),
        (
            "Riverside County Community Foundation - Local Grants",
            "Riverside County Community Foundation",
            "Support local organizations serving Riverside County communities",
            "both",
            5000,
            50000,
            "2026-04-01",
            "county:riverside",
            "https://www.rcf.org/grants",
            datetime.now().isoformat()
        ),
    ]
    
    cursor.executemany('''
        INSERT INTO grants 
        (title, funder, description, focus_area, amount_min, amount_max, 
         deadline, geographic_eligibility, website_url, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', new_grants)
    
    conn.commit()
    print(f"[OK] Added {len(new_grants)} new grants to database")
    
    # Show summary
    cursor.execute('SELECT COUNT(*) FROM grants')
    total = cursor.fetchone()[0]
    print(f"[OK] Total grants in database: {total}")
    
    conn.close()

if __name__ == "__main__":
    add_diverse_grants()

