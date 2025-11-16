/**
 * EquityBridge Frontend Logic
 * Handles form submission and API communication
 */

// API endpoint (update when backend is deployed)
// For production: Update this URL to your Railway backend URL
// Or set via window.API_URL if injected by build process
const API_URL = window.API_URL || 'http://localhost:8000';

// Wait for DOM to be ready
let profileForm, resultsSection, resultsContent, formTab, chatTab, formPanel, chatPanel;

function initForm() {
    // Get form and results elements
    profileForm = document.getElementById('profile-form');
    resultsSection = document.getElementById('results');
    resultsContent = document.getElementById('results-content');

    // Tab switching for AI Chat/Form (AI-first approach)
    formTab = document.getElementById('form-tab');
    chatTab = document.getElementById('chat-tab');
    formPanel = document.getElementById('form-panel');
    chatPanel = document.getElementById('chat-panel');
    
    if (!profileForm || !formTab || !chatTab) {
        console.error('Form elements not found');
        return;
    }
    
    setupFormHandlers();
}

function setupFormHandlers() {

    // Handle tab switching - AI Chat is default/primary
    chatTab.addEventListener('click', () => {
    chatTab.classList.add('active');
    chatTab.setAttribute('aria-selected', 'true');
    formTab.classList.remove('active');
    formTab.setAttribute('aria-selected', 'false');
    chatPanel.classList.remove('hidden');
    chatPanel.setAttribute('aria-hidden', 'false');
    formPanel.classList.add('hidden');
    formPanel.setAttribute('aria-hidden', 'true');
});

    formTab.addEventListener('click', () => {
        formTab.classList.add('active');
        formTab.setAttribute('aria-selected', 'true');
        chatTab.classList.remove('active');
        chatTab.setAttribute('aria-selected', 'false');
        formPanel.classList.remove('hidden');
        formPanel.setAttribute('aria-hidden', 'false');
        chatPanel.classList.add('hidden');
        chatPanel.setAttribute('aria-hidden', 'true');
    });

    // Handle form submission
    profileForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(profileForm);
    const profile = {
        name: formData.get('name'),
        zip_code: formData.get('zip_code'),
        county: formData.get('county') || null,  // Optional field
        mission: formData.get('mission'),
        focus_area: formData.get('focus_area'),
        annual_budget: parseInt(formData.get('annual_budget')),
        staff_size: formData.get('staff_size')
    };
    
    // Show loading state
    resultsSection.classList.remove('hidden');
    resultsContent.innerHTML = '<div class="loading">Finding matching grants...</div>';
    
    // Initialize map if not already done
    if (window.initializeMap && !window.mapInitialized) {
        window.initializeMap();
        window.mapInitialized = true;
    }
    
    try {
        // Call backend API
        const response = await fetch(`${API_URL}/api/match-grants`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(profile)
        });
        
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Failed to fetch grants: ${response.status} ${errorText}`);
        }
        
        const data = await response.json();
        
        // Display results
        displayResults(data);
        
        // Initialize map if not already done
        if (window.initializeMap && !window.mapInitialized) {
            window.initializeMap();
            window.mapInitialized = true;
        }
        
        // Highlight matching grants on map
        if (window.highlightMatchingGrants && data.grants) {
            window.highlightMatchingGrants(data.grants);
        }
        
        // Show user location
        if (window.showUserLocation && profile.zip_code) {
            window.showUserLocation(profile.zip_code);
        }
        
    } catch (error) {
        console.error('Error:', error);
        resultsContent.innerHTML = `
            <div class="error">
                <p><strong>Error finding grants.</strong></p>
                <p>Please check that the backend server is running at ${API_URL}</p>
            </div>
        `;
    }
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForm);
} else {
    initForm();
}

/**
 * Display grant matching results
 * Exported for use by chat.js
 */
window.displayResults = function displayResults(data) {
    // Get elements if not already set
    if (!resultsSection) resultsSection = document.getElementById('results');
    if (!resultsContent) resultsContent = document.getElementById('results-content');
    
    if (!resultsSection || !resultsContent) {
        console.error('Results elements not found');
        return;
    }
    
    if (!data.grants || data.grants.length === 0) {
        resultsContent.innerHTML = '<p>No matching grants found. Try adjusting your criteria.</p>';
        resultsSection.classList.remove('hidden');
        return;
    }
    
    const grantsHTML = data.grants.map(grant => `
        <article class="grant-card">
            <h3>${escapeHtml(grant.title)}</h3>
            <p><strong>Funder:</strong> ${escapeHtml(grant.funder)}</p>
            <div class="grant-meta">
                <span><strong>Amount:</strong> ${escapeHtml(grant.amount)}</span>
                <span><strong>Deadline:</strong> ${escapeHtml(grant.deadline)}</span>
            </div>
            <p><span class="match-score">${grant.match_score.toFixed(0)}% Match</span></p>
            <p><strong>Why this matches:</strong> ${escapeHtml(grant.match_reason)}</p>
            <p><strong>Eligibility:</strong> ${escapeHtml(grant.eligibility)}</p>
        </article>
    `).join('');
    
    resultsContent.innerHTML = `
        <p><strong>${data.matches_found} grant${data.matches_found === 1 ? '' : 's'} found for ${escapeHtml(data.organization)}</strong></p>
        ${grantsHTML}
    `;
    
    resultsSection.classList.remove('hidden');
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
};

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(unsafe) {
    if (!unsafe) return '';
    return unsafe
        .toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// Keyboard accessibility: Trap focus in modal if needed
// Add more interactive features as needed during hackathon
