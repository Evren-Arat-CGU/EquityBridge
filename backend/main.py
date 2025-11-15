"""
EquityBridge Backend API
CGU Hackathon - November 15, 2025

Geographic grant matching for health & environmental equity organizations.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from datetime import datetime
import os

# Initialize FastAPI app
app = FastAPI(
    title="EquityBridge API",
    description="Grant discovery for health & environmental equity",
    version="1.0.0"
)

# CORS middleware for frontend access
# In production, update CORS_ORIGINS environment variable
cors_origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins if cors_origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# DATA MODELS
# =============================================================================

class OrganizationProfile(BaseModel):
    """Organization information for grant matching"""
    name: str
    zip_code: str
    county: Optional[str] = None
    mission: str
    focus_area: str  # "health", "environment", "both"
    annual_budget: int
    staff_size: str  # "1-5", "6-20", "21-50", "50+"
    
class GrantMatch(BaseModel):
    """Grant matching result"""
    grant_id: int
    title: str
    funder: str
    amount: str
    deadline: str
    match_score: float
    match_reason: str
    eligibility: str

# =============================================================================
# DATABASE FUNCTIONS
# =============================================================================

def get_db_connection():
    """Get database connection"""
    db_path = os.path.join(os.path.dirname(__file__), 'equitybridge.db')
    return sqlite3.connect(db_path)

def query_grants(focus_area: Optional[str] = None, geographic_filter: Optional[str] = None):
    """Query grants from database"""
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row  # Enable column access by name
    cursor = conn.cursor()
    
    query = "SELECT * FROM grants WHERE 1=1"
    params = []
    
    if focus_area:
        if focus_area == "both":
            # Match grants that are health, environment, or both
            query += " AND (focus_area = 'health' OR focus_area = 'environment' OR focus_area = 'both')"
        else:
            query += " AND (focus_area = ? OR focus_area = 'both')"
            params.append(focus_area)
    
    if geographic_filter:
        # Simple geographic matching: federal grants match all, state/county need exact match
        query += " AND (geographic_eligibility = 'federal' OR geographic_eligibility = ? OR geographic_eligibility LIKE ?)"
        params.extend([geographic_filter, f"%{geographic_filter}%"])
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def calculate_match_score(grant: dict, profile: OrganizationProfile) -> float:
    """Calculate match score for a grant (0-100)"""
    score = 0.0
    
    # Focus area match (40 points)
    if grant['focus_area'] == profile.focus_area:
        score += 40
    elif grant['focus_area'] == 'both' or profile.focus_area == 'both':
        score += 30
    elif (grant['focus_area'] == 'health' and profile.focus_area == 'environment') or \
         (grant['focus_area'] == 'environment' and profile.focus_area == 'health'):
        score += 10
    
    # Geographic match (30 points)
    geo_eligibility = grant.get('geographic_eligibility', '')
    if geo_eligibility == 'federal':
        score += 30
    elif 'CA' in geo_eligibility or 'California' in geo_eligibility:
        score += 25
    elif profile.county and profile.county.lower() in geo_eligibility.lower():
        score += 30
    else:
        score += 15  # Partial match
    
    # Budget fit (20 points)
    grant_min = grant.get('amount_min', 0)
    grant_max = grant.get('amount_max', float('inf'))
    org_budget = profile.annual_budget
    
    if grant_min <= org_budget <= grant_max:
        score += 20
    elif org_budget < grant_min:
        # Organization is smaller than grant minimum - still eligible but lower score
        score += 10
    else:
        # Organization is larger - still eligible
        score += 15
    
    # Mission keyword matching (10 points) - simple check
    mission_lower = profile.mission.lower()
    description = grant.get('description', '').lower()
    title = grant.get('title', '').lower()
    
    keywords = ['health', 'community', 'equity', 'environment', 'justice', 'disparities']
    matches = sum(1 for keyword in keywords if keyword in mission_lower and (keyword in description or keyword in title))
    score += min(10, matches * 2)
    
    return min(100.0, score)

def generate_match_reason(grant: dict, profile: OrganizationProfile, score: float) -> str:
    """Generate human-readable match reason"""
    reasons = []
    
    # Focus area
    if grant['focus_area'] == profile.focus_area:
        reasons.append(f"Perfect focus area match ({profile.focus_area})")
    elif grant['focus_area'] == 'both':
        reasons.append("Grant supports both health and environmental initiatives")
    
    # Geographic
    geo = grant.get('geographic_eligibility', '')
    if geo == 'federal':
        reasons.append("Nationally available grant")
    elif 'CA' in geo or 'California' in geo:
        reasons.append("California-eligible grant")
    elif profile.county and profile.county.lower() in geo.lower():
        reasons.append(f"Specifically available in {profile.county} County")
    
    # Budget
    grant_min = grant.get('amount_min', 0)
    grant_max = grant.get('amount_max', float('inf'))
    if grant_min <= profile.annual_budget <= grant_max:
        reasons.append("Grant amount aligns with your organization size")
    
    if not reasons:
        reasons.append("Relevant grant opportunity")
    
    return ". ".join(reasons) + "."

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "EquityBridge API",
        "version": "1.0.0"
    }

@app.post("/api/match-grants")
async def match_grants(profile: OrganizationProfile):
    """
    Match grants to organization profile
    
    Queries database for relevant grants and scores them based on:
    - Focus area match (health/environment/both)
    - Geographic eligibility
    - Budget fit
    - Mission alignment
    """
    
    try:
        # Determine geographic filter (simplified: use CA for now, can enhance with zip code lookup)
        geographic_filter = "CA"  # Default to California
        
        # Query grants from database
        grants = query_grants(
            focus_area=profile.focus_area,
            geographic_filter=geographic_filter
        )
        
        if not grants:
            # If no grants found, try without geographic filter
            grants = query_grants(focus_area=profile.focus_area)
        
        # Calculate match scores for each grant
        scored_grants = []
        for grant in grants:
            score = calculate_match_score(grant, profile)
            scored_grants.append({
                'grant': grant,
                'score': score
            })
        
        # Sort by score (highest first) and take top 5
        scored_grants.sort(key=lambda x: x['score'], reverse=True)
        top_grants = scored_grants[:5]
        
        # Convert to GrantMatch format
        matches = []
        for item in top_grants:
            grant = item['grant']
            score = item['score']
            
            # Format amount
            amount_min = grant.get('amount_min', 0)
            amount_max = grant.get('amount_max', 0)
            if amount_max:
                amount_str = f"${amount_min:,} - ${amount_max:,}"
            else:
                amount_str = f"${amount_min:,}+"
            
            matches.append(GrantMatch(
                grant_id=grant['id'],
                title=grant['title'],
                funder=grant['funder'],
                amount=amount_str,
                deadline=grant.get('deadline', 'TBD'),
                match_score=round(score, 1),
                match_reason=generate_match_reason(grant, profile, score),
                eligibility=grant.get('geographic_eligibility', 'Not specified')
            ))
        
        return {
            "organization": profile.name,
            "matches_found": len(matches),
            "grants": matches
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error matching grants: {str(e)}")

@app.get("/api/grants")
async def get_grants(focus_area: Optional[str] = None, state: Optional[str] = "CA"):
    """
    Get available grants
    
    Returns all grants matching the filters:
    - focus_area: 'health', 'environment', or 'both'
    - state: Geographic filter (default: 'CA')
    """
    try:
        grants = query_grants(focus_area=focus_area, geographic_filter=state)
        
        # Format grants for response
        formatted_grants = []
        for grant in grants:
            amount_min = grant.get('amount_min', 0)
            amount_max = grant.get('amount_max', 0)
            if amount_max:
                amount_str = f"${amount_min:,} - ${amount_max:,}"
            else:
                amount_str = f"${amount_min:,}+"
            
            formatted_grants.append({
                "id": grant['id'],
                "title": grant['title'],
                "funder": grant['funder'],
                "description": grant.get('description', ''),
                "focus_area": grant['focus_area'],
                "amount": amount_str,
                "deadline": grant.get('deadline', 'TBD'),
                "geographic_eligibility": grant.get('geographic_eligibility', ''),
                "website_url": grant.get('website_url', '')
            })
        
        return {
            "total": len(formatted_grants),
            "grants": formatted_grants
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching grants: {str(e)}")

# =============================================================================
# DATABASE SETUP (Run on startup)
# =============================================================================

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    # Check if database exists, if not create it
    db_path = os.path.join(os.path.dirname(__file__), 'equitybridge.db')
    if not os.path.exists(db_path):
        # Import and run database creation
        from database import create_database
        create_database()
        print("[OK] Database initialized on startup")
    else:
        print("[OK] Database found, ready to serve")

# =============================================================================
# RUN SERVER
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
